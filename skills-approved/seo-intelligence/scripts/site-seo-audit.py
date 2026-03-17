#!/usr/bin/env python3
"""
Site SEO Audit — Automated technical SEO + content quality check
Checks all managed WordPress sites for indexation, schema, internal links, and AI visibility.
"""

import json
import sys
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    print("ERROR: pip install requests")
    sys.exit(1)

# === Site Credentials ===
def load_env(path):
    env = {}
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    env[k.strip()] = v.strip().strip('"').strip("'")
    return env

SECRETS_DIR = os.path.expanduser('~/.openclaw/workspace/.secrets/')

SITES = {
    'mysticaldigits.com': {'env': 'mysticaldigits.access.env'},
    'affiliatemarketingforsuccess.com': {'env': 'affiliatemarketingforsuccess.access.env'},
    'frenchyfab.com': {'env': 'frenchyfab.access.env'},
    'efficientgptprompts.com': {'env': 'efficientgptprompts.access.env'},
    'micegoneguide.com': {'env': 'micegoneguide.access.env'},
    'gearuptogrow.com': {'env': 'gearuptogrow.access.env'},
    'gearuptofit.com': {'env': 'gearuptofit.access.env'},
    'plantastichaven.com': {'env': 'plantastichaven.access.env'},
}

def get_wp_auth(site_key):
    """Get WP credentials for a site."""
    site = SITES.get(site_key)
    if not site:
        return None
    env = load_env(os.path.join(SECRETS_DIR, site['env']))
    user = env.get('WP_USERNAME', env.get('WP_USER', ''))
    password = env.get('WP_APP_PASSWORD', env.get('WP_PASSWORD', ''))
    if user and password:
        return (user, password)
    return None

def wp_api_get(site_url, endpoint, auth, params=None):
    """GET from WP REST API."""
    params = params or {}
    url = f"{site_url}/wp-json/wp/v2/{endpoint}"
    try:
        resp = requests.get(url, auth=auth, params=params, timeout=15)
        if resp.status_code == 200:
            return resp.json(), dict(resp.headers)
        return None, dict(resp.headers)
    except Exception as e:
        return str(e), {}

def check_head(url):
    """Check HTTP headers of a URL."""
    try:
        resp = requests.head(url, timeout=10, allow_redirects=True, headers={
            'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1)'
        })
        return {
            'status': resp.status_code,
            'content_type': resp.headers.get('content-type', ''),
            'cache': resp.headers.get('cf-cache-status', resp.headers.get('x-litespeed-cache', 'none')),
            'redirects': len(resp.history),
            'final_url': resp.url
        }
    except Exception as e:
        return {'error': str(e)}

def check_schema(url):
    """Check if a page has schema markup."""
    try:
        resp = requests.get(url, timeout=10, headers={
            'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1)'
        })
        if resp.status_code != 200:
            return {'error': f'Status {resp.status_code}'}
        
        html = resp.text
        schemas = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.DOTALL)
        
        schema_types = []
        for s in schemas:
            try:
                data = json.loads(s)
                if '@graph' in data:
                    for item in data['@graph']:
                        if '@type' in item:
                            schema_types.append(item['@type'])
                elif '@type' in data:
                    schema_types.append(data['@type'])
            except:
                pass
        
        # Check for key elements
        has_faq = 'FAQPage' in schema_types
        has_article = 'Article' in schema_types or 'BlogPosting' in schema_types
        has_breadcrumb = 'BreadcrumbList' in schema_types
        has_organization = 'Organization' in schema_types
        has_speakable = 'SpeakableSpecification' in schema_types
        
        # Check meta tags
        meta_title = re.search(r'<title>(.*?)</title>', html)
        meta_desc = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', html)
        og_title = re.search(r'<meta[^>]*property=["\']og:title["\'][^>]*content=["\'](.*?)["\']', html)
        
        return {
            'schemas': schema_types,
            'has_faq': has_faq,
            'has_article': has_article,
            'has_breadcrumb': has_breadcrumb,
            'has_organization': has_organization,
            'has_speakable': has_speakable,
            'meta_title': meta_title.group(1) if meta_title else None,
            'meta_description': meta_desc.group(1) if meta_desc else None,
            'og_title': og_title.group(1) if og_title else None,
        }
    except Exception as e:
        return {'error': str(e)}

def audit_post(post, site_url, auth):
    """Audit a single post for SEO issues."""
    post_id = post['id']
    post_url = post['link']
    post_title = post['title']['rendered']
    
    issues = []
    score = 100
    
    # 1. Check content length
    content = post['content']['rendered']
    word_count = len(re.findall(r'\w+', content))
    if word_count < 800:
        issues.append(f"Thin content ({word_count} words)")
        score -= 15
    elif word_count < 1500:
        issues.append(f"Medium content ({word_count} words) — could be deeper")
        score -= 5
    
    # 2. Check for H2/H3 structure
    h2_count = len(re.findall(r'<h2[^>]*>', content))
    h3_count = len(re.findall(r'<h3[^>]*>', content))
    if h2_count == 0:
        issues.append("No H2 headings — bad for AI parsing")
        score -= 15
    elif h2_count < 3 and word_count > 1000:
        issues.append(f"Only {h2_count} H2 headings — need more structure")
        score -= 5
    
    # 3. Check Yoast meta
    yoast_title = post.get('yoast_head_json', {}).get('title')
    yoast_desc = post.get('yoast_head_json', {}).get('description')
    if not yoast_title:
        issues.append("No Yoast meta title")
        score -= 10
    if not yoast_desc:
        issues.append("No Yoast meta description")
        score -= 10
    
    # 4. Check for images
    img_count = len(re.findall(r'<img[^>]*>', content))
    if img_count == 0:
        issues.append("No images — missing engagement signal")
        score -= 5
    
    # 5. Check for internal links
    internal_links = re.findall(r'href=["\']([^"\']*' + re.escape(site_url.replace('https://', '').replace('http://', '')) + r'[^"\']*)["\']', content)
    if len(internal_links) < 3:
        issues.append(f"Only {len(internal_links)} internal links — need 6-10")
        score -= 10
    
    # 6. Check schema on live page
    schema = check_schema(post_url)
    if 'error' not in schema:
        if not schema['has_article']:
            issues.append("No Article schema")
            score -= 10
        if not schema['has_faq']:
            issues.append("No FAQPage schema — missing AI visibility")
            score -= 5
        if not schema['has_breadcrumb']:
            issues.append("No BreadcrumbList schema")
            score -= 3
    
    return {
        'id': post_id,
        'title': post_title,
        'url': post_url,
        'word_count': word_count,
        'h2_count': h2_count,
        'h3_count': h3_count,
        'images': img_count,
        'internal_links': len(internal_links),
        'schema': schema.get('schemas', []),
        'issues': issues,
        'score': max(score, 0)
    }

def audit_site(site_url, max_posts=50):
    """Full site SEO audit."""
    domain = urlparse(site_url).netloc.replace('www.', '')
    auth = get_wp_auth(domain)
    
    if not auth:
        return {'error': f'No credentials for {domain}'}
    
    print(f"\n{'='*60}")
    print(f"SEO AUDIT: {site_url}")
    print(f"{'='*60}\n")
    
    # Get posts
    posts_data, headers = wp_api_get(site_url, 'posts', auth, {
        'per_page': min(max_posts, 100),
        '_fields': 'id,title,content,link,yoast_head_json,date,modified',
        'orderby': 'modified',
        'order': 'desc'
    })
    
    if not posts_data or isinstance(posts_data, str):
        return {'error': f'Failed to fetch posts: {posts_data}'}
    
    print(f"📝 Auditing {len(posts_data)} posts...\n")
    
    # Audit posts
    results = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(audit_post, post, site_url, auth): post for post in posts_data}
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
    
    # Sort by score (worst first)
    results.sort(key=lambda x: x['score'])
    
    # Summary
    avg_score = sum(r['score'] for r in results) / len(results) if results else 0
    critical = [r for r in results if r['score'] < 60]
    warning = [r for r in results if 60 <= r['score'] < 80]
    good = [r for r in results if r['score'] >= 80]
    
    print(f"📊 SUMMARY")
    print(f"  Average Score: {avg_score:.0f}/100")
    print(f"  Critical (<60): {len(critical)} posts")
    print(f"  Warning (60-80): {len(warning)} posts")
    print(f"  Good (80+): {len(good)} posts")
    
    # Worst posts
    if critical:
        print(f"\n🔴 CRITICAL POSTS (need immediate attention)")
        for r in critical[:10]:
            print(f"\n  [{r['score']}/100] {r['title'][:50]}")
            print(f"  URL: {r['url']}")
            print(f"  Words: {r['word_count']} | H2s: {r['h2_count']} | Images: {r['images']} | Links: {r['internal_links']}")
            for issue in r['issues']:
                print(f"  ❌ {issue}")
    
    if warning:
        print(f"\n🟡 WARNING POSTS")
        for r in warning[:5]:
            print(f"  [{r['score']}/100] {r['title'][:50]} — {', '.join(r['issues'][:2])}")
    
    # Common issues
    all_issues = []
    for r in results:
        all_issues.extend(r['issues'])
    
    from collections import Counter
    common = Counter(all_issues).most_common(10)
    
    print(f"\n📋 MOST COMMON ISSUES")
    for issue, count in common:
        pct = count / len(results) * 100
        print(f"  {count:3d} posts ({pct:4.1f}%) — {issue}")
    
    print(f"\n{'='*60}\n")
    
    return {
        'site': site_url,
        'avg_score': avg_score,
        'critical': len(critical),
        'warning': len(warning),
        'good': len(good),
        'common_issues': common,
        'posts': results
    }

def main():
    import argparse
    parser = argparse.ArgumentParser(description='WordPress Site SEO Audit')
    parser.add_argument('--site', help='Specific site URL')
    parser.add_argument('--all', action='store_true', help='Audit all managed sites')
    parser.add_argument('--max-posts', type=int, default=50, help='Max posts to audit per site')
    parser.add_argument('--output', help='Save results to JSON')
    
    args = parser.parse_args()
    
    results = {}
    
    if args.all:
        for domain in SITES:
            site_url = f'https://{domain}'
            result = audit_site(site_url, args.max_posts)
            results[domain] = result
    elif args.site:
        result = audit_site(args.site, args.max_posts)
        results[args.site] = result
    else:
        parser.print_help()
        return
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"Results saved to {args.output}")

if __name__ == '__main__':
    main()
