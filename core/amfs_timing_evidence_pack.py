#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path('/home/openclaw/.openclaw/workspace')
REPORTS = ROOT / 'reports'

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Build AMFS timing evidence packet (UI-independent)')
    ap.add_argument('--out', default='')
    a = ap.parse_args()

    timing = sorted(REPORTS.glob('amfs-timing-proof-*.json'))
    engine = sorted(REPORTS.glob('amfs-email-engine-run-*.json'))
    suppress = sorted(REPORTS.glob('amfs-test-contact-suppression-*.json'))

    latest_timing = str(timing[-1]) if timing else None
    recent_engine = [str(p) for p in engine[-10:]]
    latest_suppress = str(suppress[-1]) if suppress else None

    packet = {
        'generated_at': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        'purpose': 'AMFS lifecycle cadence proof (UI-independent) + KPI hygiene evidence',
        'latest_timing_proof': latest_timing,
        'recent_engine_runs': recent_engine,
        'latest_test_contact_suppression': latest_suppress,
        'manual_ui_gap': 'If strict UI screenshot compliance is required, capture Brevo node screenshots (0h/+24h/+3d/+7d/+14d) and attach under reports/evidence/',
    }

    out = Path(a.out) if a.out else REPORTS / f"amfs-timing-evidence-pack-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    out.write_text(json.dumps(packet, indent=2))
    print(out)
