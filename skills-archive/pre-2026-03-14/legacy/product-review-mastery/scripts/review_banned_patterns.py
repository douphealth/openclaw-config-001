#!/usr/bin/env python3
import argparse,re,json,sys
ban=[r'in today\'s fast-paced digital world',r'game-changer',r'without further ado',r'click here',r'best ever']
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('path');a=ap.parse_args();t=open(a.path,encoding='utf-8',errors='ignore').read().lower()
 hits=[]
 for p in ban:
  hits += [p for _ in re.finditer(p,t)]
 print(json.dumps({'count':len(hits),'patterns':hits},indent=2))
 sys.exit(1 if hits else 0)
