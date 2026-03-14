#!/usr/bin/env python3
import argparse
import json
import re

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('path')
    a = ap.parse_args()

    t = open(a.path, encoding='utf-8', errors='ignore').read()
    blocks = [b for b in re.split(r'\n\s*\n', t) if b.strip()]

    c = 0
    m = 0
    for b in blocks:
        visual = bool(re.search(r'<(img|table|figure|aside|details|ul|ol|div\s+class="prm-)', b, re.I))
        c = 0 if visual else c + 1
        m = max(m, c)

    print(json.dumps({'max_consecutive_text_blocks': m, 'pass': m <= 3}, indent=2))
