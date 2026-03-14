#!/usr/bin/env python3
import argparse
import datetime
import json


def utc_now_iso_z() -> str:
    # Compatible across Python versions (timezone.utc available broadly).
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--topic', required=True)
    ap.add_argument('--keyword', required=True)
    ap.add_argument('--content-type', required=True)
    a = ap.parse_args()

    out = {
        'topic': a.topic,
        'keyword': a.keyword,
        'content_type': a.content_type,
        'generated_at': utc_now_iso_z(),
        'serp_analysis': {'dominant_intent': '', 'top3': [], 'paa': [], 'content_gap': ''},
        'entity_map': {'core_entity': '', 'supporting_entities': []},
        'section_plan': [],
        'evidence_slots': [],
        'quality_targets': {'min_score': 85},
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
