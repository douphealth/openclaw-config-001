#!/usr/bin/env python3
import json
import re
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path('/home/openclaw/.openclaw/workspace')
REPORTS = ROOT / 'reports'
STATE = ROOT / 'state/amfs_email_sequence_state.json'
EXPECTED_HOURS = [0, 24, 72, 168, 336]
TOLERANCE_HOURS = 18  # operational tolerance for periodic runner/cadence drift


def parse_stamp_to_dt(stamp: str):
    # 20260301T180004Z
    return datetime.strptime(stamp, '%Y%m%dT%H%M%SZ').replace(tzinfo=timezone.utc)


def load_send_events():
    events = {}
    for p in sorted(REPORTS.glob('amfs-email-engine-run-*.json')):
        m = re.search(r'amfs-email-engine-run-(\d{8}T\d{6}Z)\.json$', p.name)
        if not m:
            continue
        run_dt = parse_stamp_to_dt(m.group(1))
        try:
            obj = json.loads(p.read_text())
        except Exception:
            continue
        for s in obj.get('sends', []):
            if not s.get('ok'):
                continue
            email = (s.get('email') or '').lower()
            step = int(s.get('step') or 0)
            if not email or step <= 0:
                continue
            events.setdefault(email, {}).setdefault(step, run_dt)
    return events


def run():
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    events = load_send_events()

    checks = []
    for email, rec in state.items():
        sent_steps = sorted(rec.get('sent_steps', []))
        if not sent_steps:
            continue
        # sent_steps are zero-indexed in state; convert to 1-indexed
        sent_steps = [x + 1 for x in sent_steps]
        e = events.get(email, {})
        base = e.get(1)
        if not base:
            checks.append({'email': email, 'status': 'insufficient_data_no_step1_timestamp'})
            continue

        deltas = []
        ok = True
        for step in sent_steps:
            dt = e.get(step)
            if not dt:
                continue
            expected = EXPECTED_HOURS[step - 1]
            actual = (dt - base).total_seconds() / 3600.0
            drift = actual - expected
            pass_step = abs(drift) <= TOLERANCE_HOURS or step == 1
            if not pass_step:
                ok = False
            deltas.append({
                'step': step,
                'expected_h': expected,
                'actual_h_from_step1': round(actual, 2),
                'drift_h': round(drift, 2),
                'pass': pass_step,
            })

        checks.append({'email': email, 'status': 'pass' if ok else 'warn', 'deltas': deltas})

    overall = 'pass' if all(c.get('status') != 'warn' for c in checks) else 'warn'
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    out = {
        'stamp': stamp,
        'method': 'state+engine-report synthetic cadence proof (UI-independent)',
        'expected_hours': EXPECTED_HOURS,
        'tolerance_hours': TOLERANCE_HOURS,
        'overall': overall,
        'checks': checks,
    }
    out_path = REPORTS / f'amfs-timing-proof-{stamp}.json'
    out_path.write_text(json.dumps(out, indent=2))
    print(out_path)


if __name__ == '__main__':
    run()
