#!/usr/bin/env python3
import argparse, json, re, collections

STOP = set('a an the and or but if with to for from in on of by as is are was were be been being this that these those your our their into over under after before than then very most more less best top review guide vs what how why when where who should can could would may might'.split())

def terms(txt: str):
    words = [w.lower() for w in re.findall(r"[a-zA-Z][a-zA-Z0-9\-]{2,}", txt)]
    return [w for w in words if w not in STOP]

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--top3-json', required=True, help='JSON array of 3 competitor texts')
    ap.add_argument('--draft-path', required=True)
    ap.add_argument('--limit', type=int, default=20)
    a = ap.parse_args()

    top3 = json.loads(a.top3_json)
    comp = collections.Counter()
    for t in top3:
        comp.update(terms(t))

    draft = open(a.draft_path, encoding='utf-8', errors='ignore').read()
    dset = set(terms(draft))

    missing = [{'term': k, 'score': v} for k, v in comp.most_common(500) if k not in dset]
    print(json.dumps({'missing_top_terms': missing[:a.limit], 'count': min(a.limit, len(missing))}, indent=2))
