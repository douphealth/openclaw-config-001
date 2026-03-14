#!/usr/bin/env python3
import argparse, json, sqlite3
from pathlib import Path
DB=Path('/home/openclaw/.openclaw/workspace/state/codex_orchestrator.db')
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--day',default=None); a=ap.parse_args()
    c=sqlite3.connect(DB)
    if a.day:
        r=c.execute("SELECT model, count(*), coalesce(sum(est_tokens),0), coalesce(sum(est_cost_usd),0) FROM ledger WHERE substr(ts,1,10)=? GROUP BY model ORDER BY 2 DESC",(a.day,)).fetchall()
    else:
        r=c.execute("SELECT substr(ts,1,10) d, count(*), coalesce(sum(est_tokens),0), coalesce(sum(est_cost_usd),0) FROM ledger GROUP BY d ORDER BY d DESC LIMIT 14").fetchall()
    print(json.dumps({'rows':r},indent=2))
