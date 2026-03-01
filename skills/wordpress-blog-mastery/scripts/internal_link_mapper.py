#!/usr/bin/env python3
import argparse,json
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--post-url',required=True);ap.add_argument('--cluster',default='');ap.add_argument('--inventory-json',default='[]');a=ap.parse_args()
 inv=json.loads(a.inventory_json)
 out={'post_url':a.post_url,'cluster':a.cluster,'to_hub':next((x for x in inv if x.get('role')=='hub'),None),'to_siblings':[x for x in inv if x.get('role') in ('sibling','spoke')][:8],'to_money':[x for x in inv if x.get('role')=='money'][:4]}
 print(json.dumps(out,indent=2))
