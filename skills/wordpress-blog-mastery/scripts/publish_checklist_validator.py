#!/usr/bin/env python3
import argparse, json, pathlib
REQUIRED=['title_ok','h1_ok','meta_ok','answer_block','faq_present','internal_links_ok','external_links_ok','canonical_ok','schema_ok','mobile_ok']
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('checklist_json'); a=ap.parse_args()
    p=pathlib.Path(a.checklist_json)
    data=json.loads(p.read_text())
    missing=[k for k in REQUIRED if k not in data]
    fails=[k for k in REQUIRED if k in data and not bool(data[k])]
    print(json.dumps({'missing_fields':missing,'failed_checks':fails,'pass':(not missing and not fails)},indent=2))
