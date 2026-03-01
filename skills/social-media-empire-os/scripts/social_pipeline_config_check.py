#!/usr/bin/env python3
import argparse, json
from pathlib import Path

ENV = Path('/home/openclaw/.openclaw/workspace/.secrets/social-media-empire.env')
REQ = [
  'PUBLER_API_KEY','CANVA_CLIENT_ID','CANVA_CLIENT_SECRET','BLOG_RSS_URLS','BRAND_NAME','BRAND_WEBSITE'
]

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--path', default=str(ENV)); a = p.parse_args()
    path = Path(a.path)
    out={'path':str(path),'exists':path.exists(),'missing':[],'pass':False}
    vals={}
    if path.exists():
        for l in path.read_text().splitlines():
            if '=' in l and not l.strip().startswith('#'):
                k,v=l.split('=',1); vals[k.strip()]=v.strip()
        out['missing']=[k for k in REQ if not vals.get(k)]
        out['pass']=len(out['missing'])==0
    print(json.dumps(out,indent=2))
