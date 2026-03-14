#!/usr/bin/env python3
import argparse
import json


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--primary', required=True, help='Primary keyword/entity')
    ap.add_argument('--product', required=True)
    ap.add_argument('--alternatives', default='[]', help='JSON list of alternative products')
    a = ap.parse_args()

    alternatives = json.loads(a.alternatives)

    plan = {
        'primary': a.primary,
        'product': a.product,
        'coverage_buckets': {
            'core_entity': [a.product, a.primary],
            'buyer_intent': ['worth it', 'who should buy', 'who should skip', 'best for'],
            'performance': ['battery life', 'accuracy', 'usability', 'reliability', 'value'],
            'comparison': ['alternatives', 'vs', 'trade-offs'] + alternatives,
            'risk_limitations': ['limitations', 'where it underperforms', 'testing limits'],
            'decision_framework': ['buy now', 'test first', 'skip if'],
        },
        'placement_guidance': {
            'intro': 'core entity + buyer intent',
            'analysis_sections': 'performance + comparison + limitations',
            'faq': 'entity-rich long-tail question variants',
            'verdict': 'decision framework language'
        },
        'anti_stuffing_rules': [
            'Avoid repeating exact-match term in consecutive paragraphs',
            'Do not add sections solely for keyword insertion',
            'Prefer natural variants and buyer language'
        ]
    }

    print(json.dumps(plan, indent=2, ensure_ascii=False))
