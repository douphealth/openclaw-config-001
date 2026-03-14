#!/usr/bin/env python3
"""test-api.py — Validate API endpoints return expected status codes.
Usage: python3 test-api.py <URL> [URL2 ...] [--expect CODE] [--timeout SECS]
Examples:
  python3 test-api.py https://api.example.com/health
  python3 test-api.py https://site.com https://site.com/api --expect 200
"""

import sys
import argparse
import urllib.request
import urllib.error

def test_endpoint(url, expected=200, timeout=15):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "test-api-bot/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = resp.status
            body_preview = resp.read(200).decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        status = e.code
        body_preview = ""
    except Exception as e:
        return False, 0, str(e)

    ok = (status == expected)
    return ok, status, body_preview

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs="+")
    parser.add_argument("--expect", type=int, default=200)
    parser.add_argument("--timeout", type=int, default=15)
    args = parser.parse_args()

    print(f"Testing {len(args.urls)} endpoint(s), expecting HTTP {args.expect}\n")

    passed = 0
    failed = 0

    for url in args.urls:
        ok, status, detail = test_endpoint(url, args.expect, args.timeout)
        icon = "✅" if ok else "❌"
        print(f"  {icon} {url}")
        print(f"     Status: {status} (expected {args.expect})")
        if not ok:
            print(f"     Detail: {detail[:200]}")
            failed += 1
        else:
            passed += 1
        print()

    print(f"Summary: {passed} passed, {failed} failed")
    sys.exit(0 if failed == 0 else 1)

if __name__ == "__main__":
    main()
