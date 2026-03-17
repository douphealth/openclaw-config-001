#!/usr/bin/env python3
"""
WordPress Content Verifier — Verify content operations are working correctly.
Usage: python3 wp-verify.py --site https://example.com --post-id 123 --auth "user:pass"
"""

import re
import json
import base64
import argparse
import urllib.request
from typing import Dict, List, Tuple


class WPVerifier:
    def __init__(self, site: str, auth: str):
        self.site = site.rstrip('/')
        self.auth = base64.b64encode(f"{auth}".encode()).decode()

    def _api_get(self, endpoint: str) -> dict:
        req = urllib.request.Request(
            f"{self.site}/wp-json/wp/v2/{endpoint}",
            headers={'Authorization': f'Basic {self.auth}'}
        )
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())

    def _fetch_page(self, url: str) -> str:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            return resp.read().decode('utf-8', errors='replace')

    def verify_content_integrity(self, post_id: int, content_type: str = 'posts') -> Dict:
        """Verify content is correctly stored and accessible."""
        endpoint = f"{content_type}/{post_id}"
        post = self._api_get(endpoint)

        raw_len = len(post['content']['raw'])
        rendered_len = len(post['content']['rendered'])
        status = post['status']
        title = post['title']['rendered']

        checks = {
            'id': post_id,
            'title': title[:60],
            'status': status,
            'content_raw_length': raw_len,
            'content_rendered_length': rendered_len,
            'checks': {}
        }

        # Check 1: Raw content exists
        checks['checks']['raw_content'] = {
            'pass': raw_len > 0,
            'value': raw_len,
            'message': 'OK' if raw_len > 0 else 'EMPTY — post_content in DB is 0 chars!'
        }

        # Check 2: Rendered content exists
        checks['checks']['rendered_content'] = {
            'pass': rendered_len > 0,
            'value': rendered_len,
            'message': 'OK' if rendered_len > 0 else 'EMPTY — no content to render'
        }

        # Check 3: Content is published
        checks['checks']['published'] = {
            'pass': status == 'publish',
            'value': status,
            'message': 'OK' if status == 'publish' else f'Status is {status}'
        }

        # Check 4: No wpautop artifacts in style blocks
        style_blocks = re.findall(r'<style[^>]*>(.*?)</style>',
                                   post['content']['rendered'], re.DOTALL)
        artifacts = sum(s.count('<p>') + s.count('</p>') + s.count('<br')
                       for s in style_blocks)
        checks['checks']['style_artifacts'] = {
            'pass': artifacts == 0,
            'value': artifacts,
            'message': f'{artifacts} artifacts found' if artifacts > 0 else 'Clean'
        }

        return checks

    def verify_live_page(self, url: str) -> Dict:
        """Verify the live page renders correctly."""
        try:
            html = self._fetch_page(url)
        except Exception as e:
            return {
                'url': url,
                'accessible': False,
                'error': str(e),
                'checks': {}
            }

        checks = {
            'url': url,
            'accessible': True,
            'page_size': len(html),
            'checks': {}
        }

        # Check 1: Page has reasonable size
        checks['checks']['page_size'] = {
            'pass': len(html) > 5000,
            'value': len(html),
            'message': f'{len(html)} bytes' if len(html) > 5000 else 'Suspiciously small'
        }

        # Check 2: Has header and footer
        has_header = '</header>' in html
        has_footer = '<footer' in html
        checks['checks']['header_footer'] = {
            'pass': has_header and has_footer,
            'value': f'header={has_header}, footer={has_footer}',
            'message': 'OK' if has_header and has_footer else 'Missing header or footer'
        }

        # Check 3: Content between header and footer
        header_end = html.find('</header>')
        footer_start = html.find('<footer')
        if header_end > -1 and footer_start > -1:
            between = html[header_end:footer_start]
            text = re.sub(r'<style[^>]*>.*?</style>', '', between, flags=re.DOTALL)
            text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
            text = re.sub(r'<[^>]+>', ' ', text)
            text = re.sub(r'\s+', ' ', text).strip()

            checks['checks']['content_between_header_footer'] = {
                'pass': len(text) > 100,
                'value': len(text),
                'message': f'{len(text)} chars of text' if len(text) > 100 else 'BLANK or near-blank'
            }
        else:
            checks['checks']['content_between_header_footer'] = {
                'pass': False,
                'value': 0,
                'message': 'Could not find header/footer markers'
            }

        # Check 4: Body class analysis
        body_match = re.search(r'<body[^>]*class="([^"]+)"', html)
        if body_match:
            classes = body_match.group(1)
            is_page = 'page-id-' in classes
            is_post = 'postid-' in classes
            template = 'unknown'

            if 'elementor_header_footer' in classes:
                template = 'elementor_header_footer'
            elif 'page-template' in classes:
                template_match = re.search(r'page-template-([^\s]+)', classes)
                template = template_match.group(1) if template_match else 'custom'

            checks['checks']['body_class'] = {
                'pass': True,
                'value': f'page={is_page}, post={is_post}, template={template}',
                'message': f'{"Page" if is_page else "Post" if is_post else "Unknown"} (template: {template})'
            }

            # Warning if page template with no content area
            if template == 'elementor_header_footer':
                checks['checks']['body_class']['pass'] = False
                checks['checks']['body_class']['message'] += ' — WARNING: no content area in this template!'
        else:
            checks['checks']['body_class'] = {
                'pass': False,
                'value': 'not found',
                'message': 'Could not find body class'
            }

        # Check 5: Check for specific content markers
        for marker in ['gutf-article', 'gutf-review', 'entry-content', 'wp-block-post-content']:
            if marker in html:
                checks['checks'][f'marker_{marker}'] = {
                    'pass': True,
                    'value': True,
                    'message': f'Found {marker}'
                }

        return checks

    def full_verification(self, post_id: int, content_type: str = 'posts',
                          live_url: str = None) -> Dict:
        """Run full verification: API + Live page."""
        api_check = self.verify_content_integrity(post_id, content_type)

        result = {
            'api': api_check,
            'live': None,
            'overall_pass': True
        }

        if live_url:
            result['live'] = self.verify_live_page(live_url)

        # Determine overall pass
        for check in api_check['checks'].values():
            if not check['pass']:
                result['overall_pass'] = False
                break

        if result['live'] and result['live'].get('accessible'):
            for check in result['live']['checks'].values():
                if not check.get('pass', True):
                    result['overall_pass'] = False
                    break

        return result


def main():
    parser = argparse.ArgumentParser(description='Verify WordPress content operations')
    parser.add_argument('--site', required=True, help='WordPress site URL')
    parser.add_argument('--auth', required=True, help='user:password')
    parser.add_argument('--post-id', type=int, help='Post ID to verify')
    parser.add_argument('--page-id', type=int, help='Page ID to verify')
    parser.add_argument('--live-url', help='Live URL to verify')
    parser.add_argument('--api-only', action='store_true', help='Only check API, not live page')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()
    verifier = WPVerifier(args.site, args.auth)

    post_id = args.post_id or args.page_id
    content_type = 'pages' if args.page_id else 'posts'

    if not post_id:
        print("Error: --post-id or --page-id required")
        return

    live_url = args.live_url
    if not live_url and not args.api_only:
        # Try to get permalink from API
        try:
            post = verifier._api_get(f"{content_type}/{post_id}")
            live_url = post.get('link')
        except:
            pass

    if args.api_only:
        result = verifier.verify_content_integrity(post_id, content_type)
    else:
        result = verifier.full_verification(post_id, content_type, live_url)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"=== Verification: {content_type}/{post_id} ===")
        if 'api' in result:
            api = result['api']
            print(f"Title: {api['title']}")
            for name, check in api['api' if 'api' in api else 'checks'].items() if isinstance(api.get('api'), dict) else api['checks'].items():
                status = '✅' if check['pass'] else '❌'
                print(f"  {status} {name}: {check['message']}")

        if result.get('live'):
            live = result['live']
            print(f"\nLive page: {live['url']}")
            if live['accessible']:
                for name, check in live['checks'].items():
                    status = '✅' if check['pass'] else '❌'
                    print(f"  {status} {name}: {check['message']}")
            else:
                print(f"  ❌ Not accessible: {live['error']}")

        print(f"\n{'✅ PASS' if result['overall_pass'] else '❌ FAIL'}")


if __name__ == '__main__':
    main()
