#!/usr/bin/env python3
import argparse, json

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--candidates-json',required=True,help='JSON list with fields demand,competition,relevance,freshness,monetization')
    a=ap.parse_args()
    rows=json.loads(a.candidates_json)
    out=[]
    for r in rows:
        s=(r.get('demand',0)*0.30 + (100-r.get('competition',100))*0.25 + r.get('relevance',0)*0.25 + r.get('freshness',0)*0.10 + r.get('monetization',0)*0.10)
        rr=dict(r); rr['score']=round(s,2); out.append(rr)
    out=sorted(out,key=lambda x:x['score'],reverse=True)
    print(json.dumps({'ranked':out,'top20':out[:20]},indent=2))
