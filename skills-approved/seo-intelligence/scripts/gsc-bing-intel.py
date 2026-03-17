#!/usr/bin/env python3
"""
SEO Intelligence — Google Search Console + Bing Webmaster Tools
Pull search performance data, diagnose indexation, find opportunities.
"""

import json
import sys
import os
import argparse
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed

# === Google Search Console ===
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GSC_AVAILABLE = True
except ImportError:
    GSC_AVAILABLE = False

import requests

# === Config ===
GSC_SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
BING_API_BASE = 'https://www.bing.com/webmaster/api.svc/json'
CACHE_DIR = os.path.expanduser('~/.openclaw/workspace/cache/seo-intel/')
os.makedirs(CACHE_DIR, exist_ok=True)


def load_env_file(path):
    """Load .env file into dict."""
    env = {}
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def get_gsc_service(credentials_path):
    """Build GSC API service."""
    if not GSC_AVAILABLE:
        print("ERROR: pip install google-api-python-client google-auth")
        sys.exit(1)
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path, scopes=GSC_SCOPES)
    return build('searchconsole', 'v1', credentials=credentials)


# === GSC Functions ===

def gsc_search_analytics(service, site_url, start_date, end_date, dimensions=None, row_limit=1000):
    """Pull search performance data."""
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': dimensions or ['query'],
        'rowLimit': row_limit,
        'dataState': 'final'
    }
    response = service.searchanalytics().query(siteUrl=site_url, body=request).execute()
    return response.get('rows', [])


def gsc_url_inspect(service, site_url, inspection_url):
    """Check indexation status of a URL."""
    request = {'inspectionUrl': inspection_url, 'siteUrl': site_url}
    response = service.urlInspection().index().inspect(body=request).execute()
    result = response.get('inspectionResult', {})
    index = result.get('indexStatusResult', {})
    return {
        'verdict': index.get('verdict'),
        'coverage': index.get('coverageState'),
        'indexing': index.get('indexingState'),
        'last_crawl': index.get('lastCrawlTime'),
        'canonical': index.get('googleCanonical'),
        'page_fetch': index.get('pageFetchState'),
    }


def gsc_sitemaps(service, site_url):
    """List submitted sitemaps."""
    response = service.sitemaps().list(siteUrl=site_url).execute()
    return response.get('sitemap', [])


# === Bing WMT Functions ===

def bing_api(api_key, endpoint, params=None):
    """Call Bing Webmaster Tools API."""
    params = params or {}
    params['apikey'] = api_key
    response = requests.get(f'{BING_API_BASE}/{endpoint}', params=params)
    return response.json()


def bing_query_stats(api_key, site_url, start_date, end_date, row_limit=1000):
    """Get query performance from Bing."""
    return bing_api(api_key, 'GetQueryStats', {
        'siteUrl': site_url,
        'startDate': start_date,
        'endDate': end_date,
        'rowLimit': row_limit
    })


def bing_page_stats(api_key, site_url, start_date, end_date):
    """Get page performance from Bing."""
    return bing_api(api_key, 'GetPageStats', {
        'siteUrl': site_url,
        'startDate': start_date,
        'endDate': end_date,
        'rowLimit': 1000
    })


def bing_crawl_stats(api_key, site_url, start_date, end_date):
    """Get crawl stats from Bing."""
    return bing_api(api_key, 'GetCrawlStats', {
        'siteUrl': site_url,
        'startDate': start_date,
        'endDate': end_date
    })


def bing_submit_url(api_key, site_url, url):
    """Submit URL for Bing indexing."""
    return bing_api(api_key, 'SubmitUrl', {
        'siteUrl': site_url,
        'url': url
    })


# === Analysis Functions ===

def find_ctr_opportunities(rows, min_impressions=100, max_ctr=0.02):
    """High impressions, low CTR = quick wins."""
    opps = []
    for row in rows:
        if row['impressions'] >= min_impressions and row['ctr'] <= max_ctr:
            potential = int(row['impressions'] * 0.05) - row['clicks']
            opps.append({
                'query': row['keys'][0],
                'impressions': row['impressions'],
                'clicks': row['clicks'],
                'ctr': row['ctr'],
                'position': row['position'],
                'potential_clicks': max(potential, 0)
            })
    return sorted(opps, key=lambda x: x['potential_clicks'], reverse=True)


def find_ranking_opportunities(rows, min_pos=5, max_pos=15, min_impressions=50):
    """Position 5-15 = close to page 1."""
    return [r for r in rows if min_pos <= r['position'] <= max_pos and r['impressions'] >= min_impressions]


def find_declining_pages(current_rows, previous_rows):
    """Compare periods to find declining pages."""
    prev_map = {r['keys'][0]: r for r in previous_rows}
    declining = []
    for row in current_rows:
        page = row['keys'][0]
        if page in prev_map:
            prev = prev_map[page]
            change = row['clicks'] - prev['clicks']
            if change < -5:
                declining.append({
                    'page': page,
                    'current_clicks': row['clicks'],
                    'previous_clicks': prev['clicks'],
                    'change': change
                })
    return sorted(declining, key=lambda x: x['change'])


# === Main Reports ===

def report_gsc_full(service, site_url, days=28):
    """Full GSC intelligence report."""
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    prev_start = (datetime.now() - timedelta(days=days*2)).strftime('%Y-%m-%d')
    prev_end = (datetime.now() - timedelta(days=days+1)).strftime('%Y-%m-%d')

    print(f"\n{'='*60}")
    print(f"SEO INTELLIGENCE REPORT — {site_url}")
    print(f"Period: {start_date} to {end_date}")
    print(f"{'='*60}\n")

    # Pull data in parallel
    with ThreadPoolExecutor(max_workers=3) as executor:
        f_queries = executor.submit(gsc_search_analytics, service, site_url, start_date, end_date, ['query'], 5000)
        f_pages = executor.submit(gsc_search_analytics, service, site_url, start_date, end_date, ['page'], 5000)
        f_prev_pages = executor.submit(gsc_search_analytics, service, site_url, prev_start, prev_end, ['page'], 5000)
        
        queries = f_queries.result()
        pages = f_pages.result()
        prev_pages = f_prev_pages.result()

    # Summary
    total_clicks = sum(r['clicks'] for r in pages)
    total_impressions = sum(r['impressions'] for r in pages)
    avg_ctr = total_clicks / total_impressions if total_impressions else 0
    avg_pos = sum(r['position'] * r['impressions'] for r in pages) / total_impressions if total_impressions else 0

    print(f"📊 SUMMARY ({days} days)")
    print(f"  Total Clicks: {total_clicks:,}")
    print(f"  Total Impressions: {total_impressions:,}")
    print(f"  Average CTR: {avg_ctr:.2%}")
    print(f"  Average Position: {avg_pos:.1f}")
    print(f"  Indexed Pages: {len(pages)}")
    print(f"  Unique Queries: {len(queries)}")

    # Top queries
    print(f"\n🔍 TOP 10 QUERIES (by clicks)")
    for i, q in enumerate(queries[:10], 1):
        print(f"  {i:2d}. {q['keys'][0]:40s} | clicks:{q['clicks']:5d} | imp:{q['impressions']:6d} | ctr:{q['ctr']:.1%} | pos:{q['position']:.1f}")

    # CTR opportunities
    ctr_opps = find_ctr_opportunities(queries)
    if ctr_opps:
        print(f"\n🎯 CTR OPPORTUNITIES (top 10)")
        for i, opp in enumerate(ctr_opps[:10], 1):
            print(f"  {i:2d}. {opp['query'][:40]:40s} | imp:{opp['impressions']:6d} | ctr:{opp['ctr']:.1%} | pos:{opp['position']:.1f} | potential:+{opp['potential_clicks']} clicks")

    # Ranking opportunities
    rank_opps = find_ranking_opportunities(queries)
    if rank_opps:
        print(f"\n📈 RANKING OPPORTUNITIES (pos 5-15, top 10)")
        for i, opp in enumerate(sorted(rank_opps, key=lambda x: x['impressions'], reverse=True)[:10], 1):
            print(f"  {i:2d}. {opp['keys'][0][:40]:40s} | pos:{opp['position']:5.1f} | imp:{opp['impressions']:6d}")

    # Declining pages
    declining = find_declining_pages(pages, prev_pages)
    if declining:
        print(f"\n📉 DECLINING PAGES (top 10)")
        for i, d in enumerate(declining[:10], 1):
            print(f"  {i:2d}. {d['page'][:50]:50s} | prev:{d['previous_clicks']:5d} | now:{d['current_clicks']:5d} | change:{d['change']:+d}")

    print(f"\n{'='*60}")
    print(f"Report complete. {len(ctr_opps)} CTR opps, {len(rank_opps)} ranking opps, {len(declining)} declining pages")
    print(f"{'='*60}\n")

    return {
        'summary': {'clicks': total_clicks, 'impressions': total_impressions, 'ctr': avg_ctr, 'position': avg_pos},
        'ctr_opportunities': ctr_opps[:20],
        'ranking_opportunities': rank_opps[:20],
        'declining_pages': declining[:20]
    }


def report_bing_full(api_key, site_url, days=28):
    """Full Bing WMT intelligence report."""
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

    print(f"\n{'='*60}")
    print(f"BING WEBMASTER TOOLS REPORT — {site_url}")
    print(f"Period: {start_date} to {end_date}")
    print(f"{'='*60}\n")

    queries = bing_query_stats(api_key, site_url, start_date, end_date)
    pages = bing_page_stats(api_key, site_url, start_date, end_date)
    crawl = bing_crawl_stats(api_key, site_url, start_date, end_date)

    print(f"📊 BING PERFORMANCE")
    if isinstance(queries, list) and queries:
        print(f"  Queries: {len(queries)}")
        for q in queries[:10]:
            print(f"    {q}")
    if isinstance(pages, list) and pages:
        print(f"  Pages: {len(pages)}")
    if isinstance(crawl, dict):
        print(f"  Crawl Stats: {json.dumps(crawl, indent=2)[:500]}")

    return {'queries': queries, 'pages': pages, 'crawl': crawl}


# === CLI ===

def main():
    parser = argparse.ArgumentParser(description='SEO Intelligence — GSC + Bing WMT')
    parser.add_argument('--gsc', action='store_true', help='Run GSC report')
    parser.add_argument('--bing', action='store_true', help='Run Bing report')
    parser.add_argument('--site', required=True, help='Site URL (https://example.com)')
    parser.add_argument('--days', type=int, default=28, help='Days to analyze (default: 28)')
    parser.add_argument('--gsc-creds', default='~/.openclaw/workspace/.secrets/gsc-service-account.json', help='GSC service account JSON')
    parser.add_argument('--bing-key', default=None, help='Bing API key (or set in .secrets/bing-api-key.txt)')
    parser.add_argument('--inspect-url', help='Inspect a specific URL in GSC')
    parser.add_argument('--output', help='Save report to JSON file')
    
    args = parser.parse_args()
    
    results = {}

    if args.gsc:
        creds_path = os.path.expanduser(args.gsc_creds)
        service = get_gsc_service(creds_path)
        
        if args.inspect_url:
            status = gsc_url_inspect(service, args.site, args.inspect_url)
            print(json.dumps(status, indent=2))
        else:
            results['gsc'] = report_gsc_full(service, args.site, args.days)

    if args.bing:
        bing_key = args.bing_key
        if not bing_key:
            key_path = os.path.expanduser('~/.openclaw/workspace/.secrets/bing-api-key.txt')
            if os.path.exists(key_path):
                with open(key_path) as f:
                    bing_key = f.read().strip()
        if not bing_key:
            print("ERROR: Provide --bing-key or create .secrets/bing-api-key.txt")
            sys.exit(1)
        results['bing'] = report_bing_full(bing_key, args.site, args.days)

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"\nReport saved to {args.output}")


if __name__ == '__main__':
    main()
