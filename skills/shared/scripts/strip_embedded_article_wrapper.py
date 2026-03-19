#!/usr/bin/env python3
"""
Remove embedded article/header/H1 wrappers from post body content while preserving main content.
"""
import re, sys

def transform(raw):
    if '<article' not in raw.lower() or 'entry-header' not in raw.lower():
        return raw, False
    body=raw
    body=re.sub(r'<article[^>]*>', '', body, count=1, flags=re.I|re.S)
    body=re.sub(r'</article>\s*$', '', body, count=1, flags=re.I|re.S)
    body=re.sub(r'<header[^>]*class="entry-header"[^>]*>.*?</header>', '', body, count=1, flags=re.I|re.S)
    body=re.sub(r'<div[^>]*class="ast-post-format[^"]*"[^>]*>', '', body, count=1, flags=re.I|re.S)
    body=re.sub(r'</div>\s*$', '', body, count=1, flags=re.I|re.S)
    body=body.strip()
    return body, True

if __name__ == '__main__':
    raw=sys.stdin.read()
    out, changed = transform(raw)
    sys.stdout.write(out)
