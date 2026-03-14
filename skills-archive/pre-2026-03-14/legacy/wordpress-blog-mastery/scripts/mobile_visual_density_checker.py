#!/usr/bin/env python3
import argparse
import json
import re


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('path')
    a = ap.parse_args()

    txt = open(a.path, encoding='utf-8', errors='ignore').read()
    blocks = [b for b in re.split(r'\n\s*\n', txt) if b.strip()]

    consec = 0
    max_consec = 0
    for b in blocks:
        is_visual = bool(re.search(r'<(table|img|figure|aside|details|nav|ul|ol|div\s+class="oc-)', b, re.I))
        if is_visual:
            consec = 0
        else:
            consec += 1
            max_consec = max(max_consec, consec)

    print(json.dumps({'max_consecutive_text_blocks': max_consec, 'pass': max_consec <= 3}, indent=2))
