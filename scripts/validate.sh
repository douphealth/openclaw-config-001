#!/usr/bin/env bash
set -euo pipefail

required_files=(
  README.md
  RECOVERY.md
  OPERATIONS.md
  SECURITY.md
  MANIFEST.yaml
  Makefile
)

for f in "${required_files[@]}"; do
  test -f "$f" || { echo "[validate] missing $f"; exit 1; }
done

for d in scripts docs skills-approved skills-archive config .github; do
  test -d "$d" || { echo "[validate] missing dir $d"; exit 1; }
done

secret_hits="$(grep -RInE 'ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|xoxb-[A-Za-z0-9-]{20,}|AIza[0-9A-Za-z_-]{20,}|-----BEGIN (RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----|sk-(live|test|proj)-[A-Za-z0-9]+' . \
  --exclude-dir=.git \
  --exclude-dir=releases \
  --exclude=.env.example || true)"

if [[ -n "${secret_hits}" ]]; then
  echo "[validate] forbidden secret-like content detected"
  echo "${secret_hits}"
  exit 1
fi

approved_count=$(find skills-approved -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')
if [[ "${approved_count}" -lt 1 ]]; then
  echo "[validate] no approved skills found"
  exit 1
fi

missing_skill_md=0
while IFS= read -r dir; do
  if [[ ! -f "$dir/SKILL.md" ]]; then
    echo "[validate] missing SKILL.md in $dir"
    missing_skill_md=1
  fi
done < <(find skills-approved -mindepth 1 -maxdepth 1 -type d | sort)

if [[ "$missing_skill_md" -ne 0 ]]; then
  exit 1
fi

python3 - <<'PY'
import sys
from pathlib import Path
import yaml

manifest = Path('MANIFEST.yaml')
try:
    data = yaml.safe_load(manifest.read_text())
except Exception as e:
    print(f"[validate] invalid MANIFEST.yaml: {e}")
    sys.exit(1)

skills = data.get('production_skills', [])
if not isinstance(skills, list) or not skills:
    print('[validate] MANIFEST.yaml has no production_skills entries')
    sys.exit(1)

missing = []
for item in skills:
    path = item.get('path')
    name = item.get('name')
    if not path:
        missing.append(f"manifest entry missing path for {name}")
        continue
    p = Path(path)
    if not p.exists():
        missing.append(f"missing path: {path}")
        continue
    if p.is_dir() and not (p / 'SKILL.md').exists():
        missing.append(f"missing SKILL.md in {path}")

if missing:
    print('[validate] manifest/path mismatches detected')
    for m in missing:
        print(m)
    sys.exit(1)

print(f"[validate] manifest ok ({len(skills)} production skills)")
PY

echo "[validate] repo structure ok"
