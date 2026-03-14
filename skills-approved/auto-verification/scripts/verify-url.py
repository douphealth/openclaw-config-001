#!/usr/bin/env python3
"""Verify a URL returns expected content"""
import sys, urllib.request, urllib.error

def verify(url, expected_text=None, expected_status=200):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=15)
        status = resp.getcode()
        body = resp.read().decode('utf-8', errors='ignore')
        result = {'url': url, 'status': status, 'ok': status == expected_status}
        if expected_text:
            result['text_found'] = expected_text in body
            result['ok'] = result['ok'] and result['text_found']
        return result
    except Exception as e:
        return {'url': url, 'status': 0, 'ok': False, 'error': str(e)}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 verify-url.py <url> [expected_text]")
        sys.exit(1)
    url = sys.argv[1]
    expected = sys.argv[2] if len(sys.argv) > 2 else None
    result = verify(url, expected)
    status = 'PASS' if result['ok'] else 'FAIL'
    print(f"{status} | {url} | HTTP {result['status']}")
    if expected:
        print(f"  Looking for: '{expected}' -> {'Found' if result.get('text_found') else 'NOT FOUND'}")
    sys.exit(0 if result['ok'] else 1)
