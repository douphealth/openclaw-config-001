#!/usr/bin/env python3
import argparse, json, re, requests, time
from pathlib import Path

def load_env(path):
    vals={}
    for l in Path(path).read_text().splitlines():
        if '=' in l and not l.strip().startswith('#'):
            k,v=l.split('=',1); vals[k.strip()]=v.strip().strip('"').strip("'")
    return vals

def score(raw,title):
    txt=re.sub('<[^>]+>',' ',raw)
    words=len([w for w in txt.split() if w.strip()])
    aff=1 if re.search(r'amazon|amzn\.to|shareasale|impact\.com|clickbank|cj\.com|partnerstack',raw,re.I) else 0
    cta=1 if re.search(r'get started|buy now|learn more|pricing|try now|sign up',raw,re.I) else 0
    faq=1 if re.search(r'faq',raw,re.I) else 0
    return max(0, (1-aff)*30 + (1-cta)*25 + (1-faq)*15 + (1 if words<1000 else 0)*20 + (1 if len(title)<35 else 0)*10)

def req_json(url, *, auth=None, params=None, timeout=20, tries=6):
    last=None
    for i in range(tries):
        try:
            r=requests.get(url,auth=auth,params=params,timeout=timeout)
            return json.loads(r.content.decode('utf-8-sig','replace'))
        except Exception as e:
            last=e; time.sleep(1.5*(i+1))
    raise last

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--env', required=True)
    ap.add_argument('--limit', type=int, default=50)
    args=ap.parse_args()
    v=load_env(args.env)
    site=v['SITE_URL'].rstrip('/'); auth=(v['WP_USERNAME'],v['WP_APP_PASSWORD'])
    posts=req_json(site+'/wp-json/wp/v2/posts',params={'per_page':args.limit,'orderby':'modified','order':'desc'},auth=auth,timeout=20)
    rows=[]
    for p in posts:
        e=req_json(f"{site}/wp-json/wp/v2/posts/{p['id']}?context=edit",auth=auth,timeout=20)
        raw=(e.get('content',{}) or {}).get('raw','')
        title=(e.get('title',{}) or {}).get('raw','') or (p.get('title',{}) or {}).get('rendered','')
        rows.append({'id':p['id'],'url':p['link'],'gap_score':score(raw,title)})
    rows=sorted(rows,key=lambda x:x['gap_score'],reverse=True)
    print(json.dumps({'site':site,'top_gaps':rows[:20]},indent=2))

if __name__=='__main__':
    main()
