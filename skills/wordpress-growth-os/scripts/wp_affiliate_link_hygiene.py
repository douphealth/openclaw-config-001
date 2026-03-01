#!/usr/bin/env python3
"""Detect affiliate links missing standard attributes in HTML snippets."""

import re

A_RE = re.compile(r'<a\b([^>]*?)>', re.I | re.S)
HREF_RE = re.compile(r'href\s*=\s*(["\'])(.*?)\1', re.I | re.S)


def check_anchor(tag_attrs: str):
    href_m = HREF_RE.search(tag_attrs)
    if not href_m:
        return None
    href = href_m.group(2)
    # lightweight affiliate heuristic
    is_aff = any(k in href.lower() for k in ['ref=', 'aff', 'bta=', '/track/', '/visit/'])
    if not is_aff:
        return None

    target_ok = bool(re.search(r'target\s*=\s*["\']_blank["\']', tag_attrs, re.I))
    rel_m = re.search(r'rel\s*=\s*(["\'])(.*?)\1', tag_attrs, re.I | re.S)
    rel = (rel_m.group(2).lower() if rel_m else '')
    rel_ok = all(x in rel for x in ['sponsored', 'nofollow', 'noopener'])

    return {
        'href': href,
        'target_ok': target_ok,
        'rel_ok': rel_ok,
        'needs_fix': not (target_ok and rel_ok)
    }


def scan(html: str):
    out = []
    for m in A_RE.finditer(html):
        r = check_anchor(m.group(1))
        if r:
            out.append(r)
    return out


if __name__ == '__main__':
    sample = '<a href="https://x.com/?ref=abc">link</a>'
    print(scan(sample))
