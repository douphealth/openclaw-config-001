#!/usr/bin/env python3
"""
Extract body content from a full HTML document pasted into WP post content.
Demotes embedded H1 to a styled paragraph to avoid duplicate H1 on themed pages.
"""
import re, sys

def transform(raw):
    m=re.search(r'<body[^>]*>(.*)</body>', raw, re.I|re.S)
    if not m:
        return raw, False
    body=m.group(1)
    body=re.sub(r'^(</p>|<p>|<br\s*/?>|\s)+','',body,flags=re.I)
    am=re.match(r'\s*<article[^>]*class="p"[^>]*>(.*)</article>\s*$', body, re.I|re.S)
    if am:
        body=am.group(1)
    body=re.sub(r'<h1[^>]*>(.*?)</h1>', r'<p class="ph-hero-title"><strong>\1</strong></p>', body, count=1, flags=re.I|re.S)
    body=body.strip()
    return body, True

if __name__ == '__main__':
    raw=sys.stdin.read()
    out, changed = transform(raw)
    sys.stdout.write(out)
