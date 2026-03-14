#!/usr/bin/env python3
import argparse, json, re, requests, time
from pathlib import Path

def load_env(path):
    vals={}
    for l in Path(path).read_text().splitlines():
        if '=' in l and not l.strip().startswith('#'):
            k,v=l.split('=',1); vals[k.strip()]=v.strip().strip('"').strip("'")
    return vals

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
    ap.add_argument('--limit', type=int, default=30)
    args=ap.parse_args()
    v=load_env(args.env)
    site=v['SITE_URL'].rstrip('/'); auth=(v['WP_USERNAME'],v['WP_APP_PASSWORD'])
    posts=req_json(site+'/wp-json/wp/v2/posts',params={'per_page':args.limit,'orderby':'modified','order':'desc'},auth=auth,timeout=20)
    href=re.compile(r'href=["\'](https?://[^"\']+)["\']',re.I)
    bad=[]
    seen={}
    for p in posts:
        e=req_json(f"{site}/wp-json/wp/v2/posts/{p['id']}?context=edit",auth=auth,timeout=20)
        raw=(e.get('content',{}) or {}).get('raw','')
        for u in href.findall(raw):
            if u in seen: st=seen[u]
            else:
                try: st=requests.head(u,allow_redirects=True,timeout=12).status_code
                except Exception: st=0
                seen[u]=st
            if st>=400 or st==0:
                bad.append({'post_id':p['id'],'post_url':p['link'],'link':u,'status':st})
    print(json.dumps({'site':site,'broken_link_count':len(bad),'broken_links':bad},indent=2))

if __name__=='__main__':
    main()
