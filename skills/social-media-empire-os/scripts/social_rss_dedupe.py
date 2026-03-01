#!/usr/bin/env python3
import argparse, json
from pathlib import Path

if __name__ == '__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--fetched-json',required=True,help='JSON list of posts with url/title/content')
    ap.add_argument('--state-path',default='/home/openclaw/.openclaw/workspace/state/social_rss_state.json')
    a=ap.parse_args()
    fetched=json.loads(Path(a.fetched_json).read_text())
    sp=Path(a.state_path)
    seen=set(json.loads(sp.read_text()) if sp.exists() else [])
    new=[p for p in fetched if p.get('url') not in seen]
    print(json.dumps({'new_posts':new,'count':len(new)},indent=2))
