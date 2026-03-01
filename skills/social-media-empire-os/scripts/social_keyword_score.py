#!/usr/bin/env python3
import argparse, json, re

def score(c):
    d=c.get('search_demand',5); comp=c.get('competition',5); vir=c.get('viral_potential',5); rel=c.get('semantic_relevance',5); ev=c.get('evergreen_score',5)
    return (d*2)+((10-comp)*2)+(vir*3)+(rel*2)+(ev*1)

if __name__ == '__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--candidates-json',required=True)
    a=ap.parse_args()
    cands=json.loads(a.candidates_json)
    for c in cands: c['composite']=score(c)
    ranked=sorted(cands,key=lambda x:x['composite'],reverse=True)
    out={'winner':ranked[0] if ranked else None,'runners_up':ranked[1:6],'ranked':ranked}
    print(json.dumps(out,indent=2))
