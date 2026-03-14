#!/usr/bin/env python3
"""test-links.py — Crawl a site and check for broken links.
Usage: python3 test-links.py <BASE_URL> [--max-pages N] [--timeout SECS]
Examples:
  python3 test-links.py https://example.com
  python3 test-links.py https://example.com --max-pages 50 --timeout 10
"""

import sys
import argparse
import urllib.request
import urllib.parse
import re
from html.parser import HTMLParser
from collections import deque

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = set()
    def handle_starttag(self, tag, attrs):
        for name, val in attrs:
            if name in ('href', 'src') and val:
                self.links.add(val)

def check_links(base_url, max_pages=20, timeout=10):
    parsed_base = urllib.parse.urlparse(base_url)
    base_origin = f"{parsed_base.scheme}://{parsed_base.netloc}"
    visited = set()
    queue = deque([base_url])
    results = []
    pages_checked = 0

    print(f"Crawling {base_url} (max {max_pages} pages)...\n")

    while queue and pages_checked < max_pages:
        url = queue.popleft()
        if url in visited:
            continue
        visited.add(url)
        pages_checked += 1

        try:
            req = urllib.request.Request(url, headers={"User-Agent": "test-links-bot/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                status = resp.status
                content_type = resp.headers.get("Content-Type", "")
                body = resp.read().decode("utf-8", errors="replace") if "text/html" in content_type else ""
        except Exception as e:
            results.append((url, 0, str(e)))
            continue

        results.append((url, status, ""))

        if body:
            parser = LinkExtractor()
            try:
                parser.feed(body)
            except Exception:
                pass
            for link in parser.links:
                abs_url = urllib.parse.urljoin(url, link)
                if abs_url.startswith(base_origin) and abs_url not in visited:
                    queue.append(abs_url)

    # Report
    broken = [(u, s, e) for u, s, e in results if s >= 400 or s == 0]
    ok = [r for r in results if r[1] < 400 and r[1] != 0]

    print(f"Pages checked: {pages_checked}")
    print(f"Links found: {len(results)}")
    print(f"✅ OK: {len(ok)}")
    print(f"❌ Broken: {len(broken)}")
    print()

    if broken:
        print("--- BROKEN LINKS ---")
        for url, status, err in broken:
            label = f"HTTP {status}" if status else f"ERROR: {err}"
            print(f"  [{label}] {url}")
        sys.exit(1)
    else:
        print("All links OK ✅")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--max-pages", type=int, default=20)
    parser.add_argument("--timeout", type=int, default=10)
    args = parser.parse_args()
    check_links(args.url, args.max_pages, args.timeout)
