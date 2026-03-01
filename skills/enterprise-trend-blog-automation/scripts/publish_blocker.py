#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path('/home/openclaw/.openclaw/workspace/skills/enterprise-trend-blog-automation/scripts')


def run_json(cmd):
    cp = subprocess.run(cmd, capture_output=True, text=True)
    out = cp.stdout.strip() or cp.stderr.strip()
    try:
        data = json.loads(out)
    except Exception:
        data = {'raw': out}
    return cp.returncode, data


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Hard publish blocker for enterprise trend blog automation')
    ap.add_argument('--draft-path', required=True)
    ap.add_argument('--top3-json', required=True, help='JSON array(3) competitor texts')
    ap.add_argument('--min-words', type=int, default=3000)
    ap.add_argument('--visual-every-words', type=int, default=200)
    ap.add_argument('--require-top-missing', type=int, default=20)
    args = ap.parse_args()

    draft = Path(args.draft_path)
    if not draft.exists():
        print(json.dumps({'pass': False, 'error': f'draft_not_found: {draft}'}))
        sys.exit(2)

    text = draft.read_text(encoding='utf-8', errors='ignore')
    word_count = len(re.findall(r"\b\w+\b", re.sub('<[^>]+>', ' ', text)))

    checks = {}

    # 1) completeness gate
    c1, d1 = run_json([
        'python3', str(ROOT / 'post_completeness_gate.py'),
        str(draft), '--min-words', str(args.min_words), '--visual-every-words', str(args.visual_every_words)
    ])
    checks['post_completeness_gate'] = d1

    # 2) internal link gate
    c2, d2 = run_json([
        'python3', str(ROOT / 'internal_link_quality_gate.py'),
        str(draft), '--word-count', str(word_count)
    ])
    checks['internal_link_quality_gate'] = d2

    # 3) serp gap gate
    c3, d3 = run_json([
        'python3', str(ROOT / 'serp_gap_top3.py'),
        '--top3-json', args.top3_json,
        '--draft-path', str(draft),
        '--limit', str(args.require_top_missing)
    ])
    checks['serp_gap_top3'] = d3

    serp_count = int(d3.get('count', 0)) if isinstance(d3, dict) else 0
    serp_pass = serp_count >= args.require_top_missing

    # combined pass
    pass_flags = {
        'post_completeness_pass': bool(d1.get('pass', False)) if isinstance(d1, dict) else False,
        'internal_link_quality_pass': bool(d2.get('pass', False)) if isinstance(d2, dict) else False,
        'serp_gap_top_missing_count_pass': serp_pass,
    }

    overall = all(pass_flags.values())

    result = {
        'pass': overall,
        'word_count': word_count,
        'flags': pass_flags,
        'checks': checks,
        'block_reason': None if overall else 'one_or_more_quality_gates_failed'
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if overall else 1)
