#!/usr/bin/env python3
import argparse,json
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('inventory_json');a=ap.parse_args();d=json.load(open(a.inventory_json))
 orphan=[p for p in d if int(p.get('inbound_links',0))<3]
 print(json.dumps({'orphans':orphan,'count':len(orphan)},indent=2))
