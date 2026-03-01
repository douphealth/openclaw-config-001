#!/usr/bin/env python3
import argparse
import datetime
import json
from pathlib import Path

STATE = Path('/home/openclaw/.openclaw/workspace/state/email_autonomy_mode.json')


def nowz():
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Pause/resume/status for email autonomy mode')
    ap.add_argument('mode', choices=['pause', 'resume', 'status'])
    args = ap.parse_args()

    state = {'enabled': True, 'updated_at': nowz(), 'note': 'initialized'}
    if STATE.exists():
        try:
            state = json.loads(STATE.read_text(encoding='utf-8'))
        except Exception:
            pass

    if args.mode == 'pause':
        state['enabled'] = False
        state['note'] = 'Paused by operator'
        state['updated_at'] = nowz()
        STATE.write_text(json.dumps(state, indent=2), encoding='utf-8')
    elif args.mode == 'resume':
        state['enabled'] = True
        state['note'] = 'Resumed by operator'
        state['updated_at'] = nowz()
        STATE.write_text(json.dumps(state, indent=2), encoding='utf-8')

    print(json.dumps(state, indent=2))
