#!/usr/bin/env python3
import argparse
import datetime
import json
import re
import sqlite3
from pathlib import Path

ROOT = Path('/home/openclaw/.openclaw/workspace')
MEM_DIR = ROOT / 'memory'
DB = ROOT / 'state' / 'memory_store.db'

STATUS_RE = re.compile(r'\b(done|partial|blocked|investigating)\b', re.I)
OUTCOME_RE = re.compile(r'\b(pass|warn|fail)\b', re.I)


def to_utc_z(dt: datetime.datetime) -> str:
    return dt.astimezone(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')


def parse_file(path: Path):
    text = path.read_text(encoding='utf-8', errors='ignore')
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]

    statuses = []
    outcomes = []
    evidence_paths = []

    for ln in lines:
        statuses += [m.group(1).lower() for m in STATUS_RE.finditer(ln)]
        outcomes += [m.group(1).lower() for m in OUTCOME_RE.finditer(ln)]
        if 'reports/' in ln:
            # coarse extraction
            for token in re.findall(r'reports/[\w\-\./]+', ln):
                evidence_paths.append(token)

    return {
        'path': str(path),
        'line_count': len(lines),
        'status_counts': {k: statuses.count(k) for k in sorted(set(statuses))},
        'outcome_counts': {k: outcomes.count(k) for k in sorted(set(outcomes))},
        'evidence_paths': sorted(set(evidence_paths))[:30],
    }


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


def compact(days: int, dry_run: bool):
    today = datetime.datetime.now(datetime.timezone.utc).date()
    files = []
    for p in sorted(MEM_DIR.glob('20*.md')):
        m = re.match(r'(\d{4}-\d{2}-\d{2})\.md$', p.name)
        if not m:
            continue
        d = datetime.date.fromisoformat(m.group(1))
        age = (today - d).days
        if age >= days:
            files.append((p, age))

    summaries = [parse_file(p) | {'age_days': age} for p, age in files]

    rollup_path = MEM_DIR / f"rollup-{today.isoformat()}.md"
    lines = [
        f"# Memory Rollup ({today.isoformat()})",
        '',
        f"updated_at: {to_utc_z(datetime.datetime.now(datetime.timezone.utc))}",
        '',
        f"source_window_days: >= {days}",
        f"files_compacted: {len(summaries)}",
        '',
        '## Summaries',
    ]
    for s in summaries:
        lines += [
            f"### {Path(s['path']).name}",
            f"- age_days: {s['age_days']}",
            f"- line_count: {s['line_count']}",
            f"- status_counts: {s['status_counts']}",
            f"- outcome_counts: {s['outcome_counts']}",
            f"- evidence_paths: {', '.join(s['evidence_paths']) if s['evidence_paths'] else 'none'}",
            '',
        ]

    if not dry_run:
        rollup_path.write_text('\n'.join(lines), encoding='utf-8')
        upsert_fact('memory', 'last_rollup_path', str(rollup_path), 'memory_compact.py')
        upsert_fact('memory', 'last_rollup_files_count', str(len(summaries)), 'memory_compact.py')
        append_event('memory_rollup', {'rollup_path': str(rollup_path), 'files': len(summaries), 'days': days})

    return {'rollup_path': str(rollup_path), 'files_compacted': len(summaries), 'dry_run': dry_run}


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Compact old daily memory logs into rollup summaries + sqlite facts/events')
    ap.add_argument('--days', type=int, default=5, help='compact files older than or equal to this age in days')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    out = compact(args.days, args.dry_run)
    print(json.dumps(out, indent=2))
