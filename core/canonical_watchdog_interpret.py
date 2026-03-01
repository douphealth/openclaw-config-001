#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def interpret(check: dict, expected: str) -> dict:
    http_ok = int(check.get('http_status') or 0) == 200
    html_can = check.get('html_canonical') or check.get('canonical_html')
    link_can = check.get('link_header_canonical') or check.get('canonical_link_header')

    html_match = bool(html_can and html_can == expected)
    link_match = bool(link_can and link_can == expected)

    status = 'ok' if (http_ok and (html_match or link_match)) else 'warn'
    reason = 'http200 + (html OR link canonical match expected)'

    return {
        'label': check.get('label'),
        'http_status': check.get('http_status'),
        'html_canonical': html_can,
        'link_header_canonical': link_can,
        'html_match': html_match,
        'link_match': link_match,
        'status': status,
        'reason': reason,
    }


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Normalize canonical watchdog interpretation')
    ap.add_argument('--input', required=True, help='watchdog json path')
    ap.add_argument('--output', required=False)
    a = ap.parse_args()

    inp = Path(a.input)
    if not inp.exists():
        raise SystemExit(f"INPUT_MISSING: {inp}")

    obj = json.loads(inp.read_text())
    if 'checks' not in obj:
        raise SystemExit("INPUT_INVALID: required key {checks} missing")

    expected = obj.get('expected') or obj.get('site')
    if not expected:
        raise SystemExit("INPUT_INVALID: expected canonical not found (expected|site)")

    normalized = [interpret(c, expected) for c in obj.get('checks', [])]
    overall = 'pass' if all(x['status'] == 'ok' for x in normalized) else 'warn'

    out = {
        'source': str(inp),
        'expected': expected,
        'rule': 'pass when HTTP 200 and expected canonical appears in HTML or Link header',
        'normalized_checks': normalized,
        'overall': overall,
    }

    if a.output:
        Path(a.output).write_text(json.dumps(out, indent=2))
        print(a.output)
    else:
        print(json.dumps(out, indent=2))
