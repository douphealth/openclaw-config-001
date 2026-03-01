#!/usr/bin/env python3
import json
import shutil
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path('/home/openclaw/.openclaw/workspace')
STATE = ROOT / 'state/amfs_email_sequence_state.json'
REPORTS = ROOT / 'reports'
BACKUPS = ROOT / 'backups'

TEST_PATTERNS = ('@example.com', 'openclaw.autotest.', 'openclaw.crmtest')


def is_test(email: str) -> bool:
    e = email.lower()
    return any(p in e for p in TEST_PATTERNS)


def run():
    if not STATE.exists():
        print('NO_STATE')
        return
    obj = json.loads(STATE.read_text())
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    backup = BACKUPS / f'amfs-sequence-state-pre-suppression-{stamp}.json'
    BACKUPS.mkdir(parents=True, exist_ok=True)
    shutil.copy2(STATE, backup)

    removed = [k for k in obj.keys() if is_test(k)]
    for k in removed:
        obj.pop(k, None)

    STATE.write_text(json.dumps(obj, indent=2))
    rep = {
        'stamp': stamp,
        'removed_count': len(removed),
        'removed': removed,
        'backup': str(backup),
        'policy': 'remove test-domain/test-alias contacts from active KPI sequence state',
    }
    out = REPORTS / f'amfs-test-contact-suppression-{stamp}.json'
    out.write_text(json.dumps(rep, indent=2))
    print(out)


if __name__ == '__main__':
    run()
