#!/usr/bin/env python3
import argparse, hashlib, json, sqlite3, datetime
from pathlib import Path
DB=Path('/home/openclaw/.openclaw/workspace/state/codex_orchestrator.db')
DB.parent.mkdir(parents=True,exist_ok=True)

def conn():
    c=sqlite3.connect(DB)
    c.execute("CREATE TABLE IF NOT EXISTS cache (key TEXT PRIMARY KEY, value_json TEXT NOT NULL, created_at TEXT NOT NULL)")
    c.commit(); return c

def h(x:str): return hashlib.sha256(x.strip().encode()).hexdigest()

if __name__=='__main__':
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True)
    g=sub.add_parser('get'); g.add_argument('--intent',required=True); g.add_argument('--ttl-hours',type=int,default=24)
    s=sub.add_parser('set'); s.add_argument('--intent',required=True); s.add_argument('--value-json',required=True)
    a=ap.parse_args(); c=conn(); k=h(a.intent)
    if a.cmd=='get':
        r=c.execute('SELECT value_json,created_at FROM cache WHERE key=?',(k,)).fetchone()
        if not r: print(json.dumps({'hit':False})); raise SystemExit(0)
        v,ts=r; dt=datetime.datetime.fromisoformat(ts)
        age=(datetime.datetime.utcnow()-dt).total_seconds()/3600
        if age>a.ttl_hours: print(json.dumps({'hit':False,'expired':True})); raise SystemExit(0)
        print(json.dumps({'hit':True,'value':json.loads(v)}))
    else:
        c.execute('INSERT OR REPLACE INTO cache(key,value_json,created_at) VALUES(?,?,?)',(k,a.value_json,datetime.datetime.utcnow().isoformat()))
        c.commit(); print(json.dumps({'ok':True,'key':k}))
