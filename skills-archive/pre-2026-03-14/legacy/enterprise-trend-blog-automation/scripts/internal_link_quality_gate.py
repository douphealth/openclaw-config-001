#!/usr/bin/env python3
import argparse, json, re
BAD={'click here','read more','learn more','here','this post'}
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('html_path'); ap.add_argument('--word-count',type=int,default=0)
    a=ap.parse_args(); t=open(a.html_path,encoding='utf-8',errors='ignore').read()
    links=re.findall(r'<a[^>]*>(.*?)</a>',t,flags=re.I|re.S)
    anchors=[re.sub('<[^>]+>','',x).strip().lower() for x in links]
    generic=[x for x in anchors if x in BAD]
    wc=a.word_count or max(1,len(re.findall(r"\b\w+\b",re.sub('<[^>]+>',' ',t))))
    density_ok=len(anchors)<=max(3,wc//150)
    min_links_ok=len(anchors)>=3
    len_ok=sum(1 for x in anchors if 3<=len(x.split())<=8)
    print(json.dumps({'anchors_total':len(anchors),'generic_anchor_violations':generic,'anchor_length_3_8_words_count':len_ok,'density_rule_pass':density_ok,'minimum_links_pass':min_links_ok,'pass':len(generic)==0 and density_ok and min_links_ok},indent=2))
