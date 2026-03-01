#!/usr/bin/env python3
import argparse
import json
import re
from urllib.parse import urljoin

import requests

CANON_RE = re.compile(r'<link[^>]+rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', re.I)
META_DESC_RE = re.compile(r'<meta[^>]+name=["\']description["\'][^>]*content=["\']([^"\']*)', re.I)
JSONLD_RE = re.compile(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>', re.I)
TAG_RE = re.compile(r'<[^>]+>')


def text_len(html: str) -> int:
    t = TAG_RE.sub(' ', html)
    t = re.sub(r'\s+', ' ', t).strip()
    return len(t)


def audit_url(url: str, timeout: int = 20):
    out = {
        'url': url,
        'status': None,
        'final_url': None,
        'canonical': None,
        'canonical_self_match': False,
        'jsonld_count': 0,
        'meta_description': None,
        'meta_description_len': 0,
        'text_length': 0,
        'errors': [],
    }
    try:
        r = requests.get(url, timeout=timeout, headers={'User-Agent': 'OpenClaw-WP-Audit/1.0'})
        out['status'] = r.status_code
        out['final_url'] = r.url
        html = r.text

        c = CANON_RE.search(html)
        if c:
            canon = c.group(1).strip()
            canon = urljoin(r.url, canon)
            out['canonical'] = canon
            out['canonical_self_match'] = canon.rstrip('/') == r.url.rstrip('/')

        out['jsonld_count'] = len(JSONLD_RE.findall(html))

        d = META_DESC_RE.search(html)
        if d:
            md = d.group(1).strip()
            out['meta_description'] = md
            out['meta_description_len'] = len(md)

        out['text_length'] = text_len(html)

    except Exception as e:
        out['errors'].append(str(e))
    return out


def load_urls(args):
    urls = []
    if args.url:
        urls.extend(args.url)
    if args.urls_file:
        with open(args.urls_file, 'r', encoding='utf-8') as f:
            for line in f:
                u = line.strip()
                if u and not u.startswith('#'):
                    urls.append(u)
    # stable unique
    seen = set()
    dedup = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            dedup.append(u)
    return dedup


def summarize(rows):
    total = len(rows)
    ok_200 = sum(1 for r in rows if r.get('status') == 200)
    canon_ok = sum(1 for r in rows if r.get('canonical_self_match'))
    with_schema = sum(1 for r in rows if (r.get('jsonld_count') or 0) > 0)
    meta_ok = sum(1 for r in rows if 50 <= (r.get('meta_description_len') or 0) <= 170)
    return {
        'total_urls': total,
        'http_200': ok_200,
        'canonical_self_match': canon_ok,
        'jsonld_present': with_schema,
        'meta_desc_len_50_170': meta_ok,
    }


def main():
    p = argparse.ArgumentParser(description='WordPress management audit for URL quality gates.')
    p.add_argument('--url', action='append', help='URL to audit (repeatable)')
    p.add_argument('--urls-file', help='Text file with one URL per line')
    p.add_argument('--timeout', type=int, default=20)
    p.add_argument('--out', help='Output JSON path')
    args = p.parse_args()

    urls = load_urls(args)
    if not urls:
        raise SystemExit('Provide --url and/or --urls-file')

    rows = [audit_url(u, timeout=args.timeout) for u in urls]
    result = {'summary': summarize(rows), 'urls': rows}

    if args.out:
        with open(args.out, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(args.out)
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
