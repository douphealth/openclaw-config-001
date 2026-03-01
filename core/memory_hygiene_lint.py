#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path('/home/openclaw/.openclaw/workspace')
mem_dir = ROOT / 'memory'

def scan_file(path: Path):
    text = path.read_text(encoding='utf-8', errors='ignore')
    issues = []
    if 'done|partial|blocked|investigating' not in text and path.name == 'procedures.md':
        issues.append('procedures_missing_status_schema_hint')
    if re.search(r'\bclick here\b', text, re.I):
        issues.append('generic_anchor_phrase_in_memory')
    if len(text.splitlines()) > 400 and path.name.endswith('.md') and path.name[:4].isdigit():
        issues.append('daily_log_too_long_consider_rollup')
    return issues

if __name__ == '__main__':
    files = [ROOT / 'MEMORY.md', mem_dir / 'index.md', mem_dir / 'procedures.md']
    files += sorted(mem_dir.glob('20*.md'))[-7:]
    total = 0
    for f in files:
        if not f.exists():
            continue
        issues = scan_file(f)
        if issues:
            print(f'{f}: {", ".join(issues)}')
            total += len(issues)
    if total == 0:
        print('MEMORY_LINT_OK')
