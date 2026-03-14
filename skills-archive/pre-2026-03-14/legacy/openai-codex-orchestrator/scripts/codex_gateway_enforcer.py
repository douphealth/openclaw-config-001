#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path

ROOT = Path('/home/openclaw/.openclaw/workspace/skills')

DIRECT_PATTERNS = [
    re.compile(r'api\.openai\.com', re.I),
    re.compile(r'openai\.(chat|responses|completions|embeddings)', re.I),
    re.compile(r'OPENAI_API_KEY', re.I),
]

ALLOWLIST = {
    'openai-codex-orchestrator',
}

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Detect direct OpenAI call patterns outside orchestrator skill')
    ap.add_argument('--path', default=str(ROOT))
    a = ap.parse_args()

    base = Path(a.path)
    violations = []
    for p in base.rglob('*'):
        if not p.is_file():
            continue
        if p.suffix.lower() not in {'.py', '.md', '.yaml', '.yml', '.json', '.txt', '.js', '.ts', '.php', '.sh'}:
            continue
        rel = p.relative_to(base)
        top = rel.parts[0] if rel.parts else ''
        if top in ALLOWLIST:
            continue
        txt = p.read_text(encoding='utf-8', errors='ignore')
        for pat in DIRECT_PATTERNS:
            if pat.search(txt):
                violations.append({'file': str(rel), 'pattern': pat.pattern})
                break

    out = {'pass': len(violations) == 0, 'violations': violations, 'count': len(violations)}
    print(json.dumps(out, indent=2))
    raise SystemExit(0 if out['pass'] else 1)
