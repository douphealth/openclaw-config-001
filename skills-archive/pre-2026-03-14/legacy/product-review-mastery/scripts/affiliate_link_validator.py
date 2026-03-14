#!/usr/bin/env python3
import argparse,re,sys
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('html_path');a=ap.parse_args()
    txt=open(a.html_path,encoding='utf-8',errors='ignore').read().lower()
    bad=[]
    for m in re.finditer(r'<a[^>]+href=',txt):
      tag=txt[m.start():txt.find('>',m.start())+1]
      if 'target="_blank"' in tag and not all(x in tag for x in ['sponsored','nofollow','noopener']):
        bad.append(tag)
    print({'invalid_affiliate_link_tags':len(bad)})
    sys.exit(1 if bad else 0)
