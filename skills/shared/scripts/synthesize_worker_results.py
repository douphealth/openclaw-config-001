#!/usr/bin/env python3
"""
Synthesize structured worker results into one actionable summary.
Input: JSON array from stdin or file path.
"""
import json, sys
from collections import Counter


def load_input():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            return json.load(f)
    return json.load(sys.stdin)


def synthesize(results):
    statuses = Counter(r.get('status', 'UNKNOWN') for r in results)
    blockers = []
    evidence = []
    recommendations = []
    totals = {'items_checked': 0, 'items_changed': 0, 'errors': 0}

    for r in results:
        blockers.extend(r.get('blockers', []))
        evidence.extend(r.get('evidence', []))
        if r.get('next_recommendation'):
            recommendations.append(r['next_recommendation'])
        metrics = r.get('metrics', {})
        for k in totals:
            totals[k] += int(metrics.get(k, 0) or 0)

    summary = {
        'worker_count': len(results),
        'status_breakdown': dict(statuses),
        'totals': totals,
        'top_blockers': blockers[:10],
        'key_evidence': evidence[:20],
        'recommended_next_steps': recommendations[:10],
        'go_no_go': 'GO' if statuses.get('FAILED', 0) == 0 else 'HOLD'
    }
    return summary


if __name__ == '__main__':
    data = load_input()
    print(json.dumps(synthesize(data), indent=2))
