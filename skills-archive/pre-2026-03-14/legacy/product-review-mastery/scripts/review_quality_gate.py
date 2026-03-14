#!/usr/bin/env python3
import argparse,json
w={'intent':2,'evidence':2,'craft':1.5,'depth':1.5,'actionability':1,'seo_aeo':1,'trust':1,'visual':1}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--scores',required=True);a=ap.parse_args();s=json.loads(a.scores)
 total=sum(w.values())
 score=sum(float(s[k])*w[k] for k in w)/total*10
 status='publish_ready' if score>=90 else 'revise_minor' if score>=85 else 'rework'
 print(json.dumps({'score_100':round(score,2),'status':status},indent=2))
