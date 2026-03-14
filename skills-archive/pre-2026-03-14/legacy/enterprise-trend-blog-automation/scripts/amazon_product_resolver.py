#!/usr/bin/env python3
import argparse
import datetime
import hashlib
import json
import re
import sqlite3
from pathlib import Path
from urllib.parse import urlparse

import requests

ROOT = Path('/home/openclaw/.openclaw/workspace')
ENV_PATH_SERPAPI = ROOT / '.secrets/serpapi.env'
ENV_PATH_SERPER = ROOT / '.secrets/serperapi.env'
DB_PATH = ROOT / 'state/serp_product_cache.db'
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

SERPAPI_URL = 'https://serpapi.com/search.json'
SERPER_URL = 'https://google.serper.dev/search'
SHOPPING_URL = 'https://google.serper.dev/shopping'
DAILY_CALL_BUDGET = 60
CACHE_TTL_DAYS = 10


def now_utc() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)


def load_env(path: Path):
    vals = {}
    if not path.exists():
        return vals
    for line in path.read_text().splitlines():
        if '=' in line and not line.strip().startswith('#'):
            k, v = line.split('=', 1)
            vals[k.strip()] = v.strip().strip('"').strip("'")
    return vals


def db():
    c = sqlite3.connect(DB_PATH)
    c.execute('''CREATE TABLE IF NOT EXISTS cache (
        key TEXT PRIMARY KEY,
        value_json TEXT NOT NULL,
        created_at TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS usage (
        day TEXT PRIMARY KEY,
        calls INTEGER NOT NULL
    )''')
    c.commit()
    return c


def usage_allowed(conn, add_calls: int = 1):
    day = now_utc().strftime('%Y-%m-%d')
    cur = conn.execute('SELECT calls FROM usage WHERE day=?', (day,))
    row = cur.fetchone()
    used = int(row[0]) if row else 0
    return (used + add_calls) <= DAILY_CALL_BUDGET, used


def increment_usage(conn, n: int):
    day = now_utc().strftime('%Y-%m-%d')
    cur = conn.execute('SELECT calls FROM usage WHERE day=?', (day,))
    row = cur.fetchone()
    used = int(row[0]) if row else 0
    if row:
        conn.execute('UPDATE usage SET calls=? WHERE day=?', (used + n, day))
    else:
        conn.execute('INSERT INTO usage(day,calls) VALUES(?,?)', (day, n))
    conn.commit()


def cache_get(conn, key: str):
    cur = conn.execute('SELECT value_json, created_at FROM cache WHERE key=?', (key,))
    row = cur.fetchone()
    if not row:
        return None
    value_json, created_at = row
    dt = datetime.datetime.fromisoformat(created_at)
    if now_utc() - dt > datetime.timedelta(days=CACHE_TTL_DAYS):
        return None
    return json.loads(value_json)


def cache_set(conn, key: str, value: dict):
    conn.execute(
        'INSERT OR REPLACE INTO cache(key,value_json,created_at) VALUES(?,?,?)',
        (key, json.dumps(value, ensure_ascii=False), now_utc().isoformat())
    )
    conn.commit()


def key_for(query: str):
    return hashlib.sha256(query.strip().lower().encode()).hexdigest()


def best_amazon_result(candidates, query):
    q_tokens = set(re.findall(r'[a-z0-9]+', query.lower()))
    best = None
    best_score = -1
    for c in candidates:
        link = c.get('link') or c.get('url') or c.get('product_link') or ''
        if 'amazon.' not in link:
            continue
        title_raw = c.get('title') or c.get('product_title') or ''
        title = title_raw.lower()
        t_tokens = set(re.findall(r'[a-z0-9]+', title))
        overlap = len(q_tokens.intersection(t_tokens))
        score = overlap
        if '/dp/' in link:
            score += 3
        if 'sponsored' not in title:
            score += 1
        if c.get('thumbnail') or c.get('serpapi_thumbnail') or c.get('image'):
            score += 1
        # Penalize accessory-only results when searching for primary product
        if any(x in title for x in ['case', 'cover', 'strap', 'band', 'protector', 'charger']):
            score -= 3
        if score > best_score:
            best_score = score
            best = {'link': link, 'title': title_raw, 'thumbnail': c.get('thumbnail') or c.get('serpapi_thumbnail') or c.get('image')}
    return best


def canonical_dp(url: str):
    m = re.search(r'/dp/([A-Z0-9]{10})', url)
    if not m:
        return url
    asin = m.group(1)
    host = urlparse(url).netloc or 'www.amazon.com'
    return f'https://{host}/dp/{asin}/'


def extract_og_image(html: str):
    m = re.search(r'property=["\']og:image["\']\s+content=["\']([^"\']+)', html, re.I)
    if m:
        return m.group(1)
    m = re.search(r'content=["\']([^"\']+)\s*["\']\s+property=["\']og:image["\']', html, re.I)
    if m:
        return m.group(1)
    return None


def extract_title(html: str):
    m = re.search(r'<title>(.*?)</title>', html, re.I | re.S)
    if not m:
        return None
    return re.sub(r'\s+', ' ', m.group(1)).strip()


def call_serper(api_key: str, endpoint: str, query: str):
    headers = {'X-API-KEY': api_key, 'Content-Type': 'application/json'}
    payload = {'q': query, 'gl': 'us', 'hl': 'en'}
    r = requests.post(endpoint, headers=headers, json=payload, timeout=25)
    if r.status_code >= 400:
        return {'_error': f'http_{r.status_code}', '_endpoint': endpoint}
    try:
        return r.json()
    except Exception:
        return {'_error': 'invalid_json', '_endpoint': endpoint}


def call_serpapi(api_key: str, query: str, shopping: bool = False):
    params = {
        'engine': 'google',
        'q': query,
        'hl': 'en',
        'gl': 'us',
        'api_key': api_key,
    }
    if shopping:
        params['tbm'] = 'shop'
    r = requests.get(SERPAPI_URL, params=params, timeout=25)
    if r.status_code >= 400:
        return {'_error': f'http_{r.status_code}', '_endpoint': 'serpapi'}
    try:
        return r.json()
    except Exception:
        return {'_error': 'invalid_json', '_endpoint': 'serpapi'}


def resolve(query: str, dry_run: bool = False):
    conn = db()
    ckey = key_for(query)

    cached = cache_get(conn, ckey)
    if cached:
        cached['source'] = 'cache'
        return cached

    ok, used = usage_allowed(conn, add_calls=2)
    if not ok and not dry_run:
        return {'error': 'daily_serper_budget_exceeded', 'used_today': used, 'budget': DAILY_CALL_BUDGET}

    if dry_run:
        return {'query': query, 'source': 'dry_run', 'note': 'no external calls executed'}

    env_serpapi = load_env(ENV_PATH_SERPAPI)
    env_serper = load_env(ENV_PATH_SERPER)

    cand = []
    errors = []

    # Prefer SerpApi (user-confirmed key), fallback to Serper if needed.
    serpapi_key = env_serpapi.get('SERPAPI_KEY')
    if serpapi_key:
        data1 = call_serpapi(serpapi_key, query + ' amazon', shopping=True)
        data2 = call_serpapi(serpapi_key, query + ' amazon product', shopping=False)
        increment_usage(conn, 2)

        if isinstance(data1, dict) and not data1.get('_error'):
            cand.extend(data1.get('shopping_results', []) if isinstance(data1.get('shopping_results'), list) else [])
            cand.extend(data1.get('organic_results', []) if isinstance(data1.get('organic_results'), list) else [])
        if isinstance(data2, dict) and not data2.get('_error'):
            cand.extend(data2.get('organic_results', []) if isinstance(data2.get('organic_results'), list) else [])

        if isinstance(data1, dict) and data1.get('_error'):
            errors.append({'endpoint': 'serpapi_shop', 'error': data1.get('_error')})
        if isinstance(data2, dict) and data2.get('_error'):
            errors.append({'endpoint': 'serpapi_search', 'error': data2.get('_error')})

    elif env_serper.get('SERPER_API_KEY'):
        api_key = env_serper.get('SERPER_API_KEY')
        data1 = call_serper(api_key, SHOPPING_URL, query)
        data2 = call_serper(api_key, SERPER_URL, query + ' amazon')
        increment_usage(conn, 2)

        if isinstance(data1, dict) and not data1.get('_error'):
            cand.extend(data1.get('shopping', []) if isinstance(data1.get('shopping'), list) else [])
        if isinstance(data2, dict) and not data2.get('_error'):
            cand.extend(data2.get('organic', []) if isinstance(data2.get('organic'), list) else [])

        if isinstance(data1, dict) and data1.get('_error'):
            errors.append({'endpoint': 'serper_shopping', 'error': data1.get('_error')})
        if isinstance(data2, dict) and data2.get('_error'):
            errors.append({'endpoint': 'serper_search', 'error': data2.get('_error')})
    else:
        return {'error': 'missing_SERPAPI_KEY_or_SERPER_API_KEY'}

    best = best_amazon_result(cand, query)
    if not best:
        out = {'query': query, 'error': 'no_amazon_result_found', 'serper_errors': errors}
        cache_set(conn, ckey, out)
        return out

    product_url = canonical_dp(best['link'])

    image = best.get('thumbnail')
    title = best.get('title')
    page_fetch_status = 'not_fetched'
    try:
        r = requests.get(product_url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=30)
        page_fetch_status = f'http_{r.status_code}'
        if r.status_code == 200:
            html = r.text
            image = extract_og_image(html) or image
            title = extract_title(html) or title
    except Exception:
        page_fetch_status = 'fetch_error'

    out = {
        'query': query,
        'product_url': product_url,
        'product_title': title,
        'product_image': image,
        'source': 'serpapi+amazon' if serpapi_key else 'serper+amazon',
        'page_fetch_status': page_fetch_status,
        'serper_errors': errors
    }
    cache_set(conn, ckey, out)
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Resolve accurate Amazon product URL/image with smart Serper API usage + cache')
    ap.add_argument('--query', required=True)
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()
    print(json.dumps(resolve(args.query, dry_run=args.dry_run), ensure_ascii=False, indent=2))
