#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--current', required=True, help='JSON file with current revenue by url')
    ap.add_argument('--previous', required=True, help='JSON file with previous revenue by url')
    ap.add_argument('--threshold', type=float, default=15.0)
    args=ap.parse_args()
    cur=json.loads(Path(args.current).read_text())
    prev=json.loads(Path(args.previous).read_text())
    alerts=[]
    for url,val in cur.items():
        p=prev.get(url)
        if p is None or p==0: continue
        drop=((p-val)/p)*100.0
        if drop>=args.threshold:
            alerts.append({'url':url,'previous':p,'current':val,'drop_pct':round(drop,2)})
    print(json.dumps({'threshold_pct':args.threshold,'alert_count':len(alerts),'alerts':alerts},indent=2))

if __name__=='__main__':
    main()
