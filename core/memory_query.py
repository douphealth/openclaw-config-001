#!/usr/bin/env python3
import argparse
import json
import sqlite3
from pathlib import Path

DB = Path('/home/openclaw/.openclaw/workspace/state/memory_store.db')


def query_facts(limit: int, category: str | None, key_like: str | None):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    sql = "SELECT id, category, key, value, source, updated_at FROM facts"
    clauses = []
    params = []
    if category:
        clauses.append("category = ?")
        params.append(category)
    if key_like:
        clauses.append("key LIKE ?")
        params.append(f"%{key_like}%")
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)
    sql += " ORDER BY updated_at DESC LIMIT ?"
    params.append(limit)

    rows = [dict(r) for r in cur.execute(sql, params).fetchall()]
    conn.close()
    return rows


def query_events(limit: int, kind: str | None):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    sql = "SELECT id, kind, payload_json, created_at FROM events"
    params = []
    if kind:
        sql += " WHERE kind = ?"
        params.append(kind)
    sql += " ORDER BY created_at DESC LIMIT ?"
    params.append(limit)

    rows = [dict(r) for r in cur.execute(sql, params).fetchall()]
    conn.close()
    return rows


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Query structured memory store')
    sub = ap.add_subparsers(dest='cmd', required=True)

    p1 = sub.add_parser('facts')
    p1.add_argument('--limit', type=int, default=20)
    p1.add_argument('--category')
    p1.add_argument('--key-like')

    p2 = sub.add_parser('events')
    p2.add_argument('--limit', type=int, default=20)
    p2.add_argument('--kind')

    args = ap.parse_args()

    if args.cmd == 'facts':
        out = query_facts(args.limit, args.category, args.key_like)
    else:
        out = query_events(args.limit, args.kind)

    print(json.dumps({'rows': out, 'count': len(out)}, ensure_ascii=False, indent=2))
