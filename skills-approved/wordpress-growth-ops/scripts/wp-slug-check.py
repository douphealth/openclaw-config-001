#!/usr/bin/env python3
"""
WordPress Slug Conflict Checker — Detect slug conflicts between posts and pages.
Usage: python3 wp-slug-check.py --site https://example.com --auth "user:pass"
"""

import json
import base64
import argparse
import urllib.request
from collections import defaultdict


class WPSlugChecker:
    def __init__(self, site: str, auth: str):
        self.site = site.rstrip('/')
        self.auth = base64.b64encode(f"{auth}".encode()).decode()

    def _api_get(self, endpoint: str) -> list:
        req = urllib.request.Request(
            f"{self.site}/wp-json/wp/v2/{endpoint}",
            headers={'Authorization': f'Basic {self.auth}'}
        )
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())

    def _get_all(self, content_type: str) -> list:
        """Get all items of a content type."""
        items = []
        page = 1
        while True:
            try:
                batch = self._api_get(f"{content_type}?page={page}&per_page=100&_fields=id,slug,title,status")
                if not batch:
                    break
                items.extend(batch)
                page += 1
            except urllib.error.HTTPError:
                break
        return items

    def check_conflicts(self) -> list:
        """Find slug conflicts between all content types."""
        posts = self._get_all('posts')
        pages = self._get_all('pages')

        print(f"Found: {len(posts)} posts, {len(pages)} pages")

        # Build slug map
        slug_map = defaultdict(list)

        for post in posts:
            slug_map[post['slug']].append({
                'type': 'post',
                'id': post['id'],
                'title': post['title']['rendered'][:50],
                'status': post['status']
            })

        for page in pages:
            slug_map[page['slug']].append({
                'type': 'page',
                'id': page['id'],
                'title': page['title']['rendered'][:50],
                'status': page['status']
            })

        # Find conflicts
        conflicts = []
        for slug, items in slug_map.items():
            if len(items) > 1:
                # Check if there's a post and a page with same slug
                types = set(i['type'] for i in items)
                if len(types) > 1:  # Cross-type conflict (post vs page)
                    conflicts.append({
                        'slug': slug,
                        'items': items,
                        'severity': 'HIGH',
                        'message': 'Page and Post share slug — Page will be served, Post hidden'
                    })
                elif len(items) > 1:  # Same-type conflict
                    conflicts.append({
                        'slug': slug,
                        'items': items,
                        'severity': 'MEDIUM',
                        'message': f'Multiple {items[0]["type"]}s share slug'
                    })

        return conflicts

    def check_orphaned_pages(self) -> list:
        """Find pages with elementor_header_footer template and 0 content."""
        pages = self._get_all('pages')
        orphaned = []

        for page in pages:
            # Get full page data
            try:
                full = self._api_get(f"pages/{page['id']}")
                template = full.get('template', '')
                content_len = len(full.get('content', {}).get('raw', ''))

                if template == 'elementor_header_footer' and content_len == 0:
                    orphaned.append({
                        'id': page['id'],
                        'slug': page['slug'],
                        'title': page['title']['rendered'][:50],
                        'status': page['status'],
                        'template': template,
                        'content_length': content_len,
                        'risk': 'HIGH — Blocks posts with same slug, renders blank'
                    })
            except:
                pass

        return orphaned


def main():
    parser = argparse.ArgumentParser(description='Check WordPress slug conflicts')
    parser.add_argument('--site', required=True, help='WordPress site URL')
    parser.add_argument('--auth', required=True, help='user:password')
    parser.add_argument('--check-orphaned', action='store_true', help='Also check for orphaned pages')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()
    checker = WPSlugChecker(args.site, args.auth)

    print("=== Checking for slug conflicts ===")
    conflicts = checker.check_conflicts()

    if args.json:
        output = {'conflicts': conflicts}
        if args.check_orphaned:
            output['orphaned'] = checker.check_orphaned_pages()
        print(json.dumps(output, indent=2))
    else:
        if conflicts:
            print(f"\n⚠️ Found {len(conflicts)} conflicts:\n")
            for c in conflicts:
                print(f"Slug: {c['slug']} ({c['severity']})")
                print(f"  {c['message']}")
                for item in c['items']:
                    status_icon = '✅' if item['status'] == 'publish' else '🗑️' if item['status'] == 'trash' else '⚠️'
                    print(f"  {status_icon} {item['type'].upper()} {item['id']}: {item['title']} ({item['status']})")
                print()
        else:
            print("✅ No slug conflicts found")

        if args.check_orphaned:
            print("=== Checking for orphaned pages ===")
            orphaned = checker.check_orphaned_pages()
            if orphaned:
                print(f"\n⚠️ Found {len(orphaned)} orphaned pages:\n")
                for p in orphaned:
                    print(f"  Page {p['id']}: {p['title']}")
                    print(f"    Slug: {p['slug']}")
                    print(f"    Template: {p['template']}")
                    print(f"    Risk: {p['risk']}")
                    print()
            else:
                print("✅ No orphaned pages found")


if __name__ == '__main__':
    main()
