#!/usr/bin/env python3
import argparse
import datetime
import json
from pathlib import Path

STATE = Path('/home/openclaw/.openclaw/workspace/state/social_media_mode.json')


def nowz():
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Control social media pipeline mode')
    ap.add_argument('mode', choices=['dry_run', 'live', 'pause', 'resume', 'status'])
    a = ap.parse_args()

    state = {'mode': 'dry_run', 'enabled': True, 'updated_at': nowz(), 'note': 'initialized'}
    if STATE.exists():
        try:
            state = json.loads(STATE.read_text(encoding='utf-8'))
        except Exception:
            pass

    if a.mode == 'dry_run':
        state.update({'mode': 'dry_run', 'enabled': True, 'updated_at': nowz(), 'note': 'Generate-only mode'})
    elif a.mode == 'live':
        state.update({'mode': 'live', 'enabled': True, 'updated_at': nowz(), 'note': 'Live publish mode'})
    elif a.mode == 'pause':
        state.update({'enabled': False, 'updated_at': nowz(), 'note': 'Paused by operator'})
    elif a.mode == 'resume':
        state.update({'enabled': True, 'updated_at': nowz(), 'note': 'Resumed by operator'})

    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2), encoding='utf-8')
    print(json.dumps(state, indent=2))
