#!/usr/bin/env python3
"""
WordPress Content Fixer — Fix wpautop artifacts in style blocks and content.
Usage: python3 wp-content-fix.py --site https://example.com --post-id 123 --auth "user:pass"
"""

import re
import json
import base64
import argparse
import urllib.request
import urllib.error
from typing import Tuple


class WPContentFixer:
    def __init__(self, site: str, auth: str):
        self.site = site.rstrip('/')
        self.auth = base64.b64encode(f"{auth}".encode()).decode()
        self.headers = {
            'Authorization': f'Basic {self.auth}',
            'Content-Type': 'application/json'
        }

    def _api_get(self, endpoint: str) -> dict:
        req = urllib.request.Request(
            f"{self.site}/wp-json/wp/v2/{endpoint}",
            headers=self.headers
        )
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())

    def _api_post(self, endpoint: str, data: dict) -> dict:
        req = urllib.request.Request(
            f"{self.site}/wp-json/wp/v2/{endpoint}",
            data=json.dumps(data).encode(),
            headers=self.headers,
            method='POST'
        )
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())

    def count_style_artifacts(self, content: str) -> int:
        """Count wpautop artifacts inside <style> blocks."""
        styles = re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
        artifacts = 0
        for s in styles:
            artifacts += s.count('<p>')
            artifacts += s.count('</p>')
            artifacts += s.count('<br />')
            artifacts += s.count('<br/>')
            artifacts += s.count('<br>')
        return artifacts

    def fix_style_blocks(self, content: str) -> Tuple[str, int, int]:
        """Remove wpautop artifacts from <style> blocks.
        Returns (fixed_content, artifacts_removed, style_blocks_fixed).
        """
        before = self.count_style_artifacts(content)

        def clean_style(match):
            style_content = match.group(1)
            # Remove wpautop artifacts
            style_content = re.sub(r'</?p>', '', style_content)
            style_content = re.sub(r'<br\s*/?>', '', style_content)
            return f'<style{match.group(2)}>{style_content}</style>'

        fixed = re.sub(
            r'<style([^>]*)>(.*?)</style>',
            clean_style,
            content,
            flags=re.DOTALL
        )

        after = self.count_style_artifacts(fixed)
        blocks = len(re.findall(r'<style[^>]*>.*?</style>', content, re.DOTALL))
        return fixed, before - after, blocks

    def fix_content(self, content: str) -> Tuple[str, dict]:
        """Apply all content fixes.
        Returns (fixed_content, report_dict).
        """
        report = {
            'style_artifacts_before': self.count_style_artifacts(content),
            'orphan_p_tags': 0,
            'p_around_scripts': 0,
            'double_spaces': 0
        }

        # Fix style blocks
        content, style_fixed, style_blocks = self.fix_style_blocks(content)
        report['style_artifacts_removed'] = style_fixed
        report['style_blocks'] = style_blocks

        # Fix orphan </p> before closing divs
        orphan_before = content.count('</p>')
        content = re.sub(r'</p>\s*(</div>|</section>|</article>)', r'\1', content)
        report['orphan_p_tags'] = orphan_before - content.count('</p>')

        # Fix <p> around <script> (shouldn't happen but just in case)
        script_p_before = len(re.findall(r'<p><script', content))
        content = re.sub(r'<p>(<script[^>]*>)', r'\1', content)
        content = re.sub(r'(</script>)</p>', r'\1', content)
        report['p_around_scripts'] = script_p_before

        # Clean double spaces
        double_before = content.count('  ')
        content = re.sub(r'  +', ' ', content)
        report['double_spaces'] = double_before - content.count('  ')

        return content, report

    def fix_post(self, post_id: int, content_type: str = 'posts', dry_run: bool = False) -> dict:
        """Fix a single post/page."""
        endpoint = f"{content_type}/{post_id}"
        post = self._api_get(endpoint)
        raw_content = post['content']['raw']

        if not raw_content:
            return {
                'id': post_id,
                'status': 'SKIPPED',
                'reason': 'raw content is empty (0 chars)',
                'rendered_length': len(post['content']['rendered'])
            }

        fixed_content, report = self.fix_content(raw_content)
        total_fixes = sum(v for k, v in report.items()
                         if k.endswith('_removed') or k.endswith('_tags')
                         or k.endswith('_scripts') or k.endswith('_spaces'))

        if total_fixes == 0:
            return {
                'id': post_id,
                'status': 'CLEAN',
                'title': post['title']['rendered'][:50],
                'content_length': len(raw_content)
            }

        if dry_run:
            return {
                'id': post_id,
                'status': 'WOULD_FIX',
                'title': post['title']['rendered'][:50],
                'fixes': total_fixes,
                'report': report
            }

        # Deploy fix
        result = self._api_post(endpoint, {'content': fixed_content})
        return {
            'id': post_id,
            'status': 'FIXED',
            'title': post['title']['rendered'][:50],
            'fixes': total_fixes,
            'report': report,
            'content_length': len(raw_content),
            'modified': result.get('modified', '?')
        }

    def scan_site(self, content_type: str = 'posts', limit: int = 100) -> list:
        """Scan all posts for issues."""
        issues = []
        page = 1
        scanned = 0

        while scanned < limit:
            posts = self._api_get(f"{content_type}?page={page}&per_page=10")
            if not posts:
                break

            for post in posts:
                scanned += 1
                content = post['content']['rendered']
                artifacts = self.count_style_artifacts(content)

                if artifacts > 0:
                    issues.append({
                        'id': post['id'],
                        'title': post['title']['rendered'][:50],
                        'artifacts': artifacts,
                        'content_length': len(content)
                    })

                if scanned >= limit:
                    break

            page += 1

        return issues


def main():
    parser = argparse.ArgumentParser(description='Fix WordPress content issues')
    parser.add_argument('--site', required=True, help='WordPress site URL')
    parser.add_argument('--auth', required=True, help='user:password')
    parser.add_argument('--post-id', type=int, help='Single post ID to fix')
    parser.add_argument('--page-id', type=int, help='Single page ID to fix')
    parser.add_argument('--scan', action='store_true', help='Scan for issues')
    parser.add_argument('--fix-all', action='store_true', help='Fix all issues found')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes only')
    parser.add_argument('--limit', type=int, default=100, help='Max posts to scan')

    args = parser.parse_args()
    fixer = WPContentFixer(args.site, args.auth)

    if args.post_id:
        result = fixer.fix_post(args.post_id, 'posts', args.dry_run)
        print(json.dumps(result, indent=2))

    elif args.page_id:
        result = fixer.fix_post(args.page_id, 'pages', args.dry_run)
        print(json.dumps(result, indent=2))

    elif args.scan:
        print("=== Scanning posts ===")
        issues = fixer.scan_site('posts', args.limit)
        for i in issues:
            print(f"  Post {i['id']}: {i['artifacts']} artifacts - {i['title']}")

        print(f"\nTotal issues: {len(issues)}")

        if args.fix_all and issues and not args.dry_run:
            print("\n=== Fixing ===")
            for i in issues:
                result = fixer.fix_post(i['id'], 'posts')
                print(f"  Post {i['id']}: {result['status']} ({result.get('fixes', 0)} fixes)")


if __name__ == '__main__':
    main()
