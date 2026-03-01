#!/usr/bin/env python3
import argparse, json, re
from urllib.parse import urlparse


def infer_patterns(urls):
    cat_pref=0
    root=0
    for u in urls:
        p=[x for x in urlparse(u).path.split('/') if x]
        if len(p)>=2:
            cat_pref += 1
        elif len(p)==1:
            root += 1
    return {'category_prefixed':cat_pref,'root_level':root}

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--sitemap-urls-json',required=True,help='JSON array of existing post URLs')
    ap.add_argument('--proposed-slug',required=True)
    ap.add_argument('--category',default='')
    a=ap.parse_args()
    urls=json.loads(a.sitemap_urls_json)
    p=infer_patterns(urls)
    use_cat=p['category_prefixed']>p['root_level']
    if use_cat and a.category:
        final=f"{a.category.strip('/')}/{a.proposed_slug.strip('/')}"
    else:
        final=a.proposed_slug.strip('/')
    print(json.dumps({'patterns':p,'use_category_prefix':use_cat,'final_slug_path':final},indent=2))
