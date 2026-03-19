#!/usr/bin/env python3
import json, sys, uuid, os
from datetime import datetime
sys.path.append('/home/openclaw/.openclaw/workspace/skills/shared/scripts')
from execution_ledger import ExecutionLedger
from execution_brief import make_brief

if len(sys.argv) < 2:
    print('Usage: job_bootstrapper.py "objective" [strategy] [skill1,skill2]')
    sys.exit(1)
objective = sys.argv[1]
strategy = sys.argv[2] if len(sys.argv) > 2 else 'plan-first execution'
skills = sys.argv[3].split(',') if len(sys.argv) > 3 and sys.argv[3] else []
job_id = 'job-' + datetime.utcnow().strftime('%Y%m%d-%H%M%S') + '-' + str(uuid.uuid4())[:8]
brief = make_brief(objective, strategy, skills)
ledger = ExecutionLedger(job_id)
ledger.set_brief(brief)
ledger.checkpoint('bootstrapped', objective)
print(json.dumps({'job_id': job_id, 'brief': brief, 'ledger': ledger.path}, indent=2))
