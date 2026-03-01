#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path('/home/openclaw/.openclaw/workspace')
REPORTS = ROOT / 'reports'

CLAIM_PATTERNS = [
    re.compile(r'\bpass on first attempt\b', re.I),
    re.compile(r'\boverall\s*:\s*pass\b', re.I),
    re.compile(r'\b0\s+flags\b', re.I),
]


def find_report_refs(line: str):
    return re.findall(r'reports/[\w\-\./]+', line)


def scan(path: Path):
    lines = path.read_text(encoding='utf-8', errors='ignore').splitlines()
    issues = []
    for i, line in enumerate(lines, start=1):
        if not any(p.search(line) for p in CLAIM_PATTERNS):
            continue
        # explicitly downgraded uncertain statements are allowed
        if re.search(r'\bunverified\b|\bpending artifact\b|\buncertain\b', line, re.I):
            continue

        refs = find_report_refs(line)
        if refs:
            existing = [r for r in refs if (ROOT / r).exists()]
            if existing:
                continue
        # allow evidence on adjacent lines
        nearby = '\n'.join(lines[max(0, i-3):min(len(lines), i+2)])
        nearby_refs = find_report_refs(nearby)
        existing_nearby = [r for r in nearby_refs if (ROOT / r).exists()]
        if existing_nearby:
            continue
        issues.append({'line': i, 'text': line.strip()[:220], 'reason': 'claim_missing_valid_evidence_reference'})
    return issues


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Block ungrounded pass-claims without valid evidence references')
    ap.add_argument('--path', required=True)
    args = ap.parse_args()

    p = Path(args.path)
    issues = scan(p)
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    out = {
        'stamp': stamp,
        'path': str(p),
        'issues': issues,
        'issue_count': len(issues),
        'pass': len(issues) == 0,
    }
    out_path = REPORTS / f'grounding-blocker-{stamp}.json'
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(out_path)
    raise SystemExit(0 if out['pass'] else 1)
