#!/usr/bin/env python3
import argparse, json, time
from pathlib import Path

STATE = Path('/home/openclaw/.openclaw/workspace/state/codex_rate_state.json')


def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {
        'requests_remaining': None,
        'tokens_remaining': None,
        'backoff_until': 0,
        'consecutive_429s': 0,
        'updated_at': 0,
    }


def save(s):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(s, indent=2))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)

    p1 = sub.add_parser('precheck')
    p1.add_argument('--estimated-tokens', type=int, default=0)

    p2 = sub.add_parser('update')
    p2.add_argument('--requests-remaining', type=int)
    p2.add_argument('--tokens-remaining', type=int)
    p2.add_argument('--status-code', type=int, default=200)
    p2.add_argument('--retry-after', type=float, default=0)

    a = ap.parse_args()
    s = load_state()
    now = time.time()

    if a.cmd == 'precheck':
        if now < s.get('backoff_until', 0):
            wait = round(s['backoff_until'] - now, 2)
            print(json.dumps({'allow': False, 'wait_seconds': wait, 'reason': 'backoff_from_429'}))
        elif s.get('requests_remaining') is not None and s['requests_remaining'] <= 2:
            print(json.dumps({'allow': False, 'wait_seconds': 2.0, 'reason': 'requests_limit_near'}))
        elif s.get('tokens_remaining') is not None and s['tokens_remaining'] < a.estimated_tokens:
            print(json.dumps({'allow': False, 'wait_seconds': 2.0, 'reason': 'token_limit_near'}))
        else:
            print(json.dumps({'allow': True, 'wait_seconds': 0, 'reason': 'clear'}))
    else:
        if a.requests_remaining is not None:
            s['requests_remaining'] = a.requests_remaining
        if a.tokens_remaining is not None:
            s['tokens_remaining'] = a.tokens_remaining

        if a.status_code == 429:
            s['consecutive_429s'] = int(s.get('consecutive_429s', 0)) + 1
            base = a.retry_after if a.retry_after > 0 else 5.0
            wait = min(base * (2 ** (s['consecutive_429s'] - 1)), 120)
            s['backoff_until'] = now + wait
        elif a.status_code < 400:
            s['consecutive_429s'] = 0

        s['updated_at'] = int(now)
        save(s)
        print(json.dumps({'ok': True, 'state': s}, indent=2))
