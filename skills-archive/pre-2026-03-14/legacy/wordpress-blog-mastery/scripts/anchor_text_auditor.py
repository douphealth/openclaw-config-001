#!/usr/bin/env python3
import argparse,json,re
GEN={'click here','read more','learn more','here','this post'}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('json_path');a=ap.parse_args();d=json.load(open(a.json_path))
 anchors=[x.get('anchor','').strip().lower() for x in d.get('links',[])]
 bad=[a for a in anchors if a in GEN or len(a.split())<3 or len(a.split())>8]
 print(json.dumps({'anchors_total':len(anchors),'invalid':bad,'pass':len(bad)==0},indent=2))
