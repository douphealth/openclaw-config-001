#!/usr/bin/env python3
import argparse, json, re, sys
BANNED=[
 r'in today\'s fast-paced digital world',r'it\'s important to note that',r'without further ado',r'let\'s dive in',r'at the end of the day',r'needless to say',r'as we all know',r'game-changer',r'holy grail'
]
if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('path')
    a=ap.parse_args()
    txt=open(a.path,'r',encoding='utf-8',errors='ignore').read().lower()
    hits=[]
    for p in BANNED:
        for m in re.finditer(p,txt):
            hits.append({'pattern':p,'start':m.start()})
    print(json.dumps({'count':len(hits),'hits':hits[:200]},indent=2))
    sys.exit(1 if hits else 0)
