#!/usr/bin/env python3
import argparse
import json


def audit(data):
    checks = []
    def add(name, ok):
        checks.append({'check': name, 'ok': bool(ok)})

    wc = int(data.get('word_count', 0))
    links = data.get('links', [])
    anchors = [l.get('anchor', '').strip().lower() for l in links]
    targets = [l.get('target', '') for l in links]

    add('hub_link_present', any(l.get('type') == 'hub' for l in links))
    add('min_3_links', len(links) >= 3)
    add('max_density_1_per_150_words', len(links) <= max(1, wc // 150))

    generic = {'click here', 'read more', 'learn more', 'here', 'this post'}
    add('no_generic_anchors', all(a not in generic for a in anchors if a))

    from collections import Counter
    ac = Counter(anchors)
    tc = Counter(targets)
    add('no_exact_anchor_repeat_gt1', all(v <= 1 for k, v in ac.items() if k))
    add('same_target_not_linked_gt2', all(v <= 2 for v in tc.values()))
    add('money_links_contextual', all((l.get('type') != 'money') or l.get('contextual', False) for l in links))

    passed = sum(1 for c in checks if c['ok'])
    return {
        'checks': checks,
        'passed': passed,
        'total': len(checks),
        'pass': passed == len(checks)
    }


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('input_json', help='JSON with word_count and links[]')
    args = ap.parse_args()
    with open(args.input_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(json.dumps(audit(data), indent=2))
