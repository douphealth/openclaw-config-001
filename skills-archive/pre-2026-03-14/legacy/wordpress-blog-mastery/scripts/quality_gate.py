#!/usr/bin/env python3
import argparse, json
DIMS=['intent','evidence','craft','expertise','readability','completeness','seo','differentiation','trust','actionability']
if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--scores',required=True,help='JSON object with 0-10 per dimension')
    a=ap.parse_args(); s=json.loads(a.scores)
    weights={'intent':2,'evidence':2,'craft':1.5,'expertise':1.5,'readability':1,'completeness':1,'seo':1,'differentiation':1,'trust':1,'actionability':1}
    miss=[d for d in DIMS if d not in s]
    if miss: raise SystemExit(f'Missing dimensions: {miss}')
    total=sum(weights.values())
    score=sum(float(s[d])*weights[d] for d in DIMS)/total*10
    status='publish_ready' if score>=90 else 'revise_minor' if score>=85 else 'revise_major' if score>=80 else 'rework'
    print(json.dumps({'score_100':round(score,2),'status':status,'weak_dimensions':[d for d in DIMS if float(s[d])<8]},indent=2))
