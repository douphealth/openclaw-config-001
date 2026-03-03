#!/usr/bin/env python3
"""Unified mode control for all OpenClaw subsystems.
Usage: python3 mode_control.py <subsystem> <pause|resume|status>
Subsystems: ceo, email, master, trend_blog, social, all
"""
import argparse, datetime, json, sys
from pathlib import Path

ROOT = Path('/home/openclaw/.openclaw/workspace/state')
SUBSYSTEMS = {
    'ceo': 'ceo_mode.json',
    'email': 'email_autonomy_mode.json',
    'master': 'master_orchestrator_mode.json',
    'trend_blog': 'trend_blog_automation_mode.json',
    'social': 'social_media_mode.json',
}

def nowz():
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')

def load(path):
    if path.exists():
        try: return json.loads(path.read_text())
        except Exception: pass
    return {'enabled': True, 'updated_at': nowz(), 'note': 'initialized'}

def save(path, state):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2))

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('subsystem', choices=list(SUBSYSTEMS) + ['all'])
    ap.add_argument('mode', choices=['pause', 'resume', 'status'])
    a = ap.parse_args()

    targets = SUBSYSTEMS if a.subsystem == 'all' else {a.subsystem: SUBSYSTEMS[a.subsystem]}
    results = {}

    for name, filename in targets.items():
        path = ROOT / filename
        state = load(path)
        if a.mode == 'pause':
            state.update(enabled=False, note='Paused by operator', updated_at=nowz())
            save(path, state)
        elif a.mode == 'resume':
            state.update(enabled=True, note='Resumed by operator', updated_at=nowz())
            save(path, state)
        results[name] = state

    print(json.dumps(results, indent=2))
