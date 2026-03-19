#!/usr/bin/env python3
"""
Generic wave runner for repair jobs.
Input JSON shape:
{
  "job_id": "ph-cleanup-1",
  "targets": [1,2,3],
  "canary": [1],
  "waves": [[2,3],[4,5]],
  "health_url": "https://site.com/",
  "failure_threshold": 3
}
This script manages wave state only; actual mutation function should be wrapped externally.
"""
import json, sys, requests, time
from pathlib import Path
sys.path.append('/home/openclaw/.openclaw/workspace/skills/shared/scripts')
from execution_ledger import ExecutionLedger

if len(sys.argv) < 2:
    print('Usage: repair_wave_runner.py plan.json')
    sys.exit(1)

plan = json.load(open(sys.argv[1]))
ledger = ExecutionLedger(plan['job_id'])
ledger.set_targets(plan.get('targets', []))
ledger.checkpoint('initialized', f"targets={len(plan.get('targets', []))}")

health_url = plan.get('health_url')
failures = 0

def health_ok():
    try:
        r = requests.get(health_url, timeout=15)
        return r.status_code == 200
    except:
        return False

if not health_ok():
    ledger.add_failure({'class':'health','detail':'initial health check failed'})
    ledger.set_status('blocked', 'site unhealthy before canary')
    print('BLOCKED')
    sys.exit(2)

ledger.checkpoint('canary-ready')
print('CANARY', plan.get('canary', []))

for i, wave in enumerate(plan.get('waves', []), start=1):
    if not health_ok():
        failures += 1
        ledger.add_failure({'class':'health','detail':f'health failed before wave {i}'})
        if failures >= plan.get('failure_threshold', 3):
            ledger.set_status('blocked', f'failed before wave {i}')
            print('STOP before wave', i)
            sys.exit(3)
        time.sleep(10)
        continue
    ledger.checkpoint(f'wave-{i}-start', f'items={len(wave)}')
    print('WAVE', i, wave)
    ledger.checkpoint(f'wave-{i}-complete')

ledger.set_status('complete', 'all waves processed by controller')
print('DONE')
