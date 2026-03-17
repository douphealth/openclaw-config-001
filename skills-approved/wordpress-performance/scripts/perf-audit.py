#!/usr/bin/env python3
"""
WordPress Performance Auditor — Quick performance audit for WordPress sites.
Usage: python3 perf-audit.py --site https://example.com
       python3 perf-audit.py --site https://example.com --page /review/product/
"""

import re
import json
import time
import argparse
import urllib.request
import urllib.error
from datetime import datetime


class WPPerfAuditor:
    def __init__(self, site: str):
        self.site = site.rstrip('/')

    def _fetch(self, url: str) -> tuple:
        """Fetch URL and return (html, metrics)."""
        start = time.time()
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                html = resp.read().decode('utf-8', errors='replace')
                ttfb = resp.headers.get('X-TTFB', time.time() - start)
                return html, {
                    'ttfb': round(ttfb, 3) if isinstance(ttfb, float) else 'N/A',
                    'total_time': round(time.time() - start, 3),
                    'size_bytes': len(html),
                    'status': resp.status,
                    'headers': dict(resp.headers)
                }
        except Exception as e:
            return '', {'error': str(e), 'total_time': round(time.time() - start, 3)}

    def audit_page(self, url: str) -> dict:
        """Audit a single page."""
        html, metrics = self._fetch(url)

        if 'error' in metrics:
            return {'url': url, 'error': metrics['error']}

        audit = {
            'url': url,
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'metrics': metrics,
            'checks': {}
        }

        # Check 1: TTFB
        ttfb = metrics.get('ttfb', 'N/A')
        if isinstance(ttfb, (int, float)):
            audit['checks']['ttfb'] = {
                'value': ttfb,
                'pass': ttfb < 0.8,
                'status': 'Good' if ttfb < 0.8 else 'Needs Improvement' if ttfb < 1.8 else 'Poor',
                'target': '< 0.8s'
            }

        # Check 2: Page size
        size = metrics['size_bytes']
        audit['checks']['page_size'] = {
            'value': f'{size:,} bytes ({size/1024:.0f} KB)',
            'pass': size < 500000,
            'status': 'Good' if size < 300000 else 'Needs Improvement' if size < 500000 else 'Large',
            'target': '< 500 KB'
        }

        # Check 3: Resource count
        css_count = len(re.findall(r'<link[^>]*rel=["\']stylesheet["\']', html))
        js_count = len(re.findall(r'<script[^>]*src=', html))
        total_resources = css_count + js_count
        audit['checks']['resources'] = {
            'css': css_count,
            'js': js_count,
            'total': total_resources,
            'pass': total_resources < 30,
            'status': 'Good' if total_resources < 20 else 'Needs Improvement' if total_resources < 40 else 'Heavy'
        }

        # Check 4: Images without lazy loading
        images = re.findall(r'<img[^>]+>', html)
        lazy_count = sum(1 for img in images if 'loading="lazy"' in img)
        total_images = len(images)
        audit['checks']['images'] = {
            'total': total_images,
            'lazy_loaded': lazy_count,
            'not_lazy': total_images - lazy_count,
            'pass': (total_images - lazy_count) <= 3,
            'status': 'Good' if lazy_count >= total_images * 0.8 else 'Needs Improvement'
        }

        # Check 5: Render-blocking resources
        render_blocking_css = len(re.findall(
            r'<link[^>]*rel=["\']stylesheet["\'][^>]*(?!media=["\']print["\'])', html))
        async_js = len(re.findall(r'<script[^>]*(async|defer)[^>]*src=', html))
        blocking_js = js_count - async_js
        audit['checks']['render_blocking'] = {
            'css': render_blocking_css,
            'js_blocking': blocking_js,
            'js_async': async_js,
            'pass': blocking_js <= 2,
            'status': 'Good' if blocking_js <= 2 else 'Needs Improvement'
        }

        # Check 6: Font loading
        font_preload = len(re.findall(r'<link[^>]*rel=["\']preload["\'][^>]*as=["\']font["\']', html))
        google_fonts = 'fonts.googleapis.com' in html or 'fonts.gstatic.com' in html
        audit['checks']['fonts'] = {
            'preloaded': font_preload,
            'google_fonts': google_fonts,
            'pass': font_preload > 0 or not google_fonts,
            'status': 'Good' if font_preload > 0 else 'Consider preloading critical fonts'
        }

        # Check 7: Caching headers
        cache_control = metrics.get('headers', {}).get('Cache-Control', '')
        cf_cache = metrics.get('headers', {}).get('CF-Cache-Status', 'N/A')
        audit['checks']['caching'] = {
            'cache_control': cache_control or 'Not set',
            'cloudflare': cf_cache,
            'pass': bool(cache_control),
            'status': 'Good' if cache_control else 'No cache headers'
        }

        # Check 8: Compression
        content_encoding = metrics.get('headers', {}).get('Content-Encoding', 'none')
        audit['checks']['compression'] = {
            'encoding': content_encoding,
            'pass': content_encoding in ('gzip', 'br', 'deflate'),
            'status': 'Good' if content_encoding in ('gzip', 'br', 'deflate') else 'Not compressed'
        }

        # Check 9: Core Web Vitals hints
        cls_issues = 0
        # Images without dimensions
        imgs_no_dims = len(re.findall(r'<img(?![^>]*(?:width|height))[^>]*>', html))
        cls_issues += imgs_no_dims

        audit['checks']['cls_risks'] = {
            'images_no_dimensions': imgs_no_dims,
            'pass': imgs_no_dims <= 2,
            'status': 'Good' if imgs_no_dims == 0 else f'{imgs_no_dims} images without dimensions'
        }

        # Calculate overall score
        passed = sum(1 for c in audit['checks'].values() if c.get('pass'))
        total = len(audit['checks'])
        audit['score'] = {
            'passed': passed,
            'total': total,
            'percentage': round(passed / total * 100) if total > 0 else 0,
            'grade': 'A' if passed/total > 0.8 else 'B' if passed/total > 0.6 else 'C' if passed/total > 0.4 else 'D'
        }

        return audit

    def audit_multiple(self, paths: list) -> list:
        """Audit multiple pages."""
        results = []
        for path in paths:
            url = f"{self.site}{path}" if path.startswith('/') else path
            print(f"Auditing: {url}")
            results.append(self.audit_page(url))
        return results


def main():
    parser = argparse.ArgumentParser(description='WordPress performance auditor')
    parser.add_argument('--site', required=True, help='WordPress site URL')
    parser.add_argument('--page', help='Specific page path to audit')
    parser.add_argument('--pages', nargs='+', help='Multiple pages to audit')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()
    auditor = WPPerfAuditor(args.site)

    if args.pages:
        results = auditor.audit_multiple(args.pages)
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            for r in results:
                print_audit(r)
    elif args.page:
        url = f"{args.site}{args.page}" if args.page.startswith('/') else args.page
        result = auditor.audit_page(url)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_audit(result)
    else:
        # Audit homepage by default
        result = auditor.audit_page(args.site)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_audit(result)


def print_audit(audit: dict):
    """Pretty print audit results."""
    print(f"\n=== Performance Audit: {audit['url']} ===")
    print(f"Score: {audit['score']['grade']} ({audit['score']['passed']}/{audit['score']['total']} passed)\n")

    for name, check in audit['checks'].items():
        status = '✅' if check.get('pass') else '⚠️'
        status_text = check.get('status', '')
        print(f"  {status} {name}: {status_text}")

    print(f"\nMetrics:")
    m = audit['metrics']
    print(f"  Total time: {m.get('total_time', 'N/A')}s")
    print(f"  Page size: {m.get('size_bytes', 0):,} bytes")
    print(f"  Status: {m.get('status', 'N/A')}")


if __name__ == '__main__':
    main()
