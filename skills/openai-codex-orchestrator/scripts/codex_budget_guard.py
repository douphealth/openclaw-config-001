#!/usr/bin/env python3
import argparse, json, sqlite3, datetime
from pathlib import Path
DB=Path('/home/openclaw/.openclaw/workspace/state/codex_orchestrator.db')
ENV=Path('/home/openclaw/.openclaw/workspace/.secrets/openai-codex.env')

def env():
    d={}
    if ENV.exists():
        for l in ENV.read_text().splitlines():
            if '=' in l and not l.strip().startswith('#'):
                k,v=l.split('=',1); d[k.strip()]=v.strip().strip('"').strip("'")
    return d

def conn():
    c=sqlite3.connect(DB)
    c.execute("CREATE TABLE IF NOT EXISTS ledger (id INTEGER PRIMARY KEY, ts TEXT NOT NULL, kind TEXT NOT NULL, request_id TEXT, model TEXT, est_cost_usd REAL DEFAULT 0, est_tokens INTEGER DEFAULT 0, status TEXT)")
    c.commit(); return c

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--est-cost',type=float,default=0); ap.add_argument('--est-tokens',type=int,default=0)
    a=ap.parse_args(); e=env(); c=conn(); now=datetime.datetime.now(datetime.timezone.utc)
    day=now.strftime('%Y-%m-%d'); hour=now.strftime('%Y-%m-%d %H')
    daily_reqs,daily_cost=c.execute("SELECT COUNT(*), COALESCE(SUM(est_cost_usd),0) FROM ledger WHERE substr(ts,1,10)=?",(day,)).fetchone()
    hourly_reqs=c.execute("SELECT COUNT(*) FROM ledger WHERE substr(ts,1,13)=?",(hour,)).fetchone()[0]
    max_hr=int(float(e.get('CODEX_MAX_HOURLY_REQUESTS',200))); max_day=int(float(e.get('CODEX_MAX_DAILY_REQUESTS',3000)))
    max_cost=float(e.get('CODEX_MAX_DAILY_SPEND_USD',10)); max_tok=int(float(e.get('CODEX_MAX_TOKENS_PER_REQUEST',16000)))
    ok=True; reasons=[]
    if hourly_reqs+1>max_hr: ok=False; reasons.append('hourly_request_cap')
    if daily_reqs+1>max_day: ok=False; reasons.append('daily_request_cap')
    if float(daily_cost)+a.est_cost>max_cost: ok=False; reasons.append('daily_spend_cap')
    if a.est_tokens>max_tok: ok=False; reasons.append('token_per_request_cap')
    print(json.dumps({'allow':ok,'reasons':reasons,'snapshot':{'hourly_reqs':hourly_reqs,'daily_reqs':daily_reqs,'daily_cost':float(daily_cost)}}))
