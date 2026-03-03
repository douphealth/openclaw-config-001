#!/usr/bin/env python3
import argparse, datetime, json
from pathlib import Path

STATE = Path('/home/openclaw/.openclaw/workspace/state/trend_blog_automation_mode.json')

def nowz():
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z')

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='pause/resume/status for trend blog automation')
    ap.add_argument('mode', choices=['pause','resume','status'])
    a = ap.parse_args()

    state = {'enabled': True, 'updated_at': nowz(), 'note': 'initialized'}
    if STATE.exists():
        try:
            state = json.loads(STATE.read_text(encoding='utf-8'))
        except Exception:
            pass

    if a.mode == 'pause':
        state.update({'enabled': False, 'updated_at': nowz(), 'note': 'Paused by operator'})
        STATE.write_text(json.dumps(state, indent=2), encoding='utf-8')
    elif a.mode == 'resume':
        state.update({'enabled': True, 'updated_at': nowz(), 'note': 'Resumed by operator'})
        STATE.write_text(json.dumps(state, indent=2), encoding='utf-8')

    print(json.dumps(state, indent=2))
