#!/usr/bin/env python3
"""
Generate/refresh site registry dossiers from ops/sites + recovery packs + backups.
"""
import os, re, json
from pathlib import Path

ROOT = Path('/home/openclaw/.openclaw/workspace')
SITES = ROOT / 'ops' / 'sites'
RECOVERY = ROOT / 'ops' / 'site-recovery-packs'
BACKUPS = ROOT / 'ops' / 'backups'
OUT = ROOT / 'ops' / 'generated-site-dossiers.json'

entries = {}
for fp in sorted(SITES.glob('*.md')):
    if fp.name == 'README.md':
        continue
    name = fp.stem
    txt = fp.read_text()
    entries[name] = {
        'site': name,
        'role': None,
        'monetization_path': [],
        'default_swarm_pattern': [],
        'highest_value_tasks': [],
        'avoid': [],
        'verify_first': [],
        'recovery_pack': None,
        'backups': []
    }
    sec=None
    for line in txt.splitlines():
        if line.startswith('## '):
            sec = line[3:].strip().lower()
            continue
        if sec == 'role' and line.strip() and not line.startswith('-'):
            entries[name]['role'] = line.strip()
        elif sec == 'best monetization path' and line.startswith('- '):
            entries[name]['monetization_path'].append(line[2:].strip())
        elif sec == 'default swarm pattern' and line.startswith('- '):
            entries[name]['default_swarm_pattern'].append(line[2:].strip())
        elif sec == 'highest-value tasks' and re.match(r'^\d+\.', line.strip()):
            entries[name]['highest_value_tasks'].append(line.split('.',1)[1].strip())
        elif sec == 'avoid' and line.startswith('- '):
            entries[name]['avoid'].append(line[2:].strip())
        elif sec == 'verify first' and line.startswith('- '):
            entries[name]['verify_first'].append(line[2:].strip())
    rp = RECOVERY / f'{name}.md'
    if rp.exists():
        entries[name]['recovery_pack'] = str(rp.relative_to(ROOT))
    # backup dirs matching site hints
    for b in BACKUPS.iterdir():
        if name.split('.')[0] in b.name or name in b.name:
            entries[name]['backups'].append(str(b.relative_to(ROOT)))

OUT.write_text(json.dumps(entries, indent=2))
print(str(OUT))
