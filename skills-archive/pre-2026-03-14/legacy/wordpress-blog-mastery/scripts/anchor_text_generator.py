#!/usr/bin/env python3
import argparse,json
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--topic',required=True);ap.add_argument('--context',required=True);a=ap.parse_args()
 t=a.topic.strip();ctx=a.context.strip()
 out={'variant_a_keyword_adjacent':f'{t} guide','variant_b_semantic':f'how {t} works','variant_c_intent_descriptive':f'detailed {t} walkthrough','context':ctx}
 print(json.dumps(out,indent=2))
