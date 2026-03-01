#!/usr/bin/env python3
import argparse, json, datetime
if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--product',required=True)
    ap.add_argument('--keyword',required=True)
    ap.add_argument('--intent',default='commercial')
    a=ap.parse_args()
    out={
      'product':a.product,'keyword':a.keyword,'intent':a.intent,
      'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z'),
      'reader_profile':{'awareness':'comparison-ready','main_risk':'buying wrong fit'},
      'sections':['hook','answer_first','snapshot','fit','method','analysis','pros_cons','alternatives','verdict','faq','trust_footer']
    }
    print(json.dumps(out,indent=2))
