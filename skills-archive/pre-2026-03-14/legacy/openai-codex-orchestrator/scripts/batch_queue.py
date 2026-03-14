#!/usr/bin/env python3
import argparse, json, time
from collections import defaultdict

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Simple in-memory batch queue simulator')
    ap.add_argument('--task-type', required=True)
    ap.add_argument('--items-json', required=True)
    ap.add_argument('--max-batch-size', type=int, default=10)
    a = ap.parse_args()

    items = json.loads(a.items_json)
    dedup = []
    seen = set()
    for it in items:
        k = json.dumps(it, sort_keys=True)
        if k in seen:
            continue
        seen.add(k)
        dedup.append(it)

    batches = [dedup[i:i+a.max_batch_size] for i in range(0, len(dedup), a.max_batch_size)]
    print(json.dumps({'task_type': a.task_type, 'deduped_count': len(dedup), 'batch_count': len(batches), 'batches': batches}, indent=2))
