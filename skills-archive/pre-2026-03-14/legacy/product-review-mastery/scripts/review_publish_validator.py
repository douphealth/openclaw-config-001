#!/usr/bin/env python3
import argparse,json
REQ=['title_ok','h1_ok','meta_ok','answer_block','faq','disclosure','affiliate_attrs','images_alt','canonical','schema']
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('json_path');a=ap.parse_args();d=json.load(open(a.json_path))
 miss=[k for k in REQ if k not in d];fail=[k for k in REQ if k in d and not d[k]]
 print(json.dumps({'missing':miss,'failed':fail,'pass':not miss and not fail},indent=2))
