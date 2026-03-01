#!/usr/bin/env python3
import argparse
import datetime
import json
import sqlite3
from pathlib import Path

ROOT = Path('/home/openclaw/.openclaw/workspace')
DB = ROOT / 'state' / 'memory_store.db'


def utc_now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')


def upsert_fact(category: str, key: str, value: str, source: str):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO facts(category, key, value, source, updated_at)
        VALUES (?, ?, ?, ?, datetime('now'))
        ON CONFLICT(category, key)
        DO UPDATE SET value=excluded.value, source=excluded.source, updated_at=datetime('now')
        """,
        (category, key, value, source),
    )
    conn.commit()
    conn.close()


def append_event(kind: str, payload: dict):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO events(kind, payload_json, created_at) VALUES (?, ?, datetime('now'))",
        (kind, json.dumps(payload, ensure_ascii=False)),
    )
    conn.commit()
    conn.close()


def update_markdown(path: Path, header: str, bullet: str):
    now = utc_now()
    if path.exists():
        text = path.read_text(encoding='utf-8', errors='ignore')
        lines = text.splitlines()
        if lines and lines[0].startswith('# '):
            # refresh updated_at if present
            replaced = False
            for i, ln in enumerate(lines[:8]):
                if ln.startswith('updated_at:'):
                    lines[i] = f'updated_at: {now}'
                    replaced = True
                    break
            if not replaced:
                lines.insert(1, f'updated_at: {now}')
            text = '\n'.join(lines)
        if bullet not in text:
            text = text.rstrip() + f"\n\n- {bullet}\n"
    else:
        text = f"# {header}\n\nupdated_at: {now}\n\n- {bullet}\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Route memory items to markdown or sqlite stores')
    ap.add_argument('--kind', required=True, choices=['preference', 'project', 'knowledge', 'fact', 'event'])
    ap.add_argument('--key', required=True)
    ap.add_argument('--value', required=True)
    ap.add_argument('--source', default='manual')
    args = ap.parse_args()

    if args.kind == 'preference':
        update_markdown(ROOT / 'preferences' / 'communication.md', 'Communication Preferences', f"{args.key}: {args.value}")
    elif args.kind == 'project':
        update_markdown(ROOT / 'projects' / 'current-status.md', 'Current Status', f"{args.key}: {args.value}")
    elif args.kind == 'knowledge':
        update_markdown(ROOT / 'knowledge-base' / 'research-notes.md', 'Research Notes', f"{args.key}: {args.value}")
    elif args.kind == 'fact':
        upsert_fact('general', args.key, args.value, args.source)
    elif args.kind == 'event':
        append_event(args.key, {'value': args.value, 'source': args.source, 'ts': utc_now()})

    print(json.dumps({'ok': True, 'kind': args.kind, 'key': args.key}, ensure_ascii=False))
