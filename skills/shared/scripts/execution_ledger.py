#!/usr/bin/env python3
"""
Structured execution ledger helper.
"""
import json, os, sys
from datetime import datetime

LEDGER_DIR = os.path.expanduser('~/'.replace('~/', '') )

class ExecutionLedger:
    def __init__(self, job_id, base_dir='/home/openclaw/.openclaw/workspace/ops/execution-ledger'):
        self.job_id = job_id
        self.base_dir = base_dir
        os.makedirs(base_dir, exist_ok=True)
        self.path = os.path.join(base_dir, f'{job_id}.json')
        if os.path.exists(self.path):
            with open(self.path) as f:
                self.data = json.load(f)
        else:
            self.data = {
                'job_id': job_id,
                'created_at': datetime.utcnow().isoformat() + 'Z',
                'status': 'initialized',
                'brief': {},
                'targets': [],
                'checkpoints': [],
                'workers': [],
                'failures': [],
                'verification': [],
                'next_step': '',
            }
            self.save()

    def save(self):
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=2)

    def set_brief(self, brief):
        self.data['brief'] = brief
        self.save()

    def set_targets(self, targets):
        self.data['targets'] = targets
        self.save()

    def checkpoint(self, label, note=''):
        self.data['checkpoints'].append({
            'time': datetime.utcnow().isoformat() + 'Z',
            'label': label,
            'note': note,
        })
        self.save()

    def add_worker_result(self, result):
        self.data['workers'].append(result)
        self.save()

    def add_failure(self, failure):
        self.data['failures'].append({
            'time': datetime.utcnow().isoformat() + 'Z',
            **failure,
        })
        self.save()

    def add_verification(self, evidence):
        self.data['verification'].append({
            'time': datetime.utcnow().isoformat() + 'Z',
            **evidence,
        })
        self.save()

    def set_status(self, status, next_step=''):
        self.data['status'] = status
        self.data['next_step'] = next_step
        self.save()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: execution_ledger.py JOB_ID')
        sys.exit(1)
    ledger = ExecutionLedger(sys.argv[1])
    print(ledger.path)
