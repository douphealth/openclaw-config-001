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

for d in scripts docs skills-approved skills-archive; do
  test -d "$d" || { echo "[validate] missing dir $d"; exit 1; }
done

secret_hits="$(grep -RInE '(OPENAI_API_KEY|ANTHROPIC_API_KEY|WP_APP_PASSWORD|BEGIN PRIVATE KEY|AIza|xoxb-|ghp_[A-Za-z0-9]|sk-[A-Za-z0-9])' . \
  --exclude-dir=.git \
  --exclude-dir=releases \
  --exclude=.env.example || true)"

if [[ -n "${secret_hits}" ]]; then
  echo "[validate] forbidden secret-like content detected"
  echo "${secret_hits}"
  exit 1
fi

for skill in \
  skills/openai-codex-orchestrator \
  skills/blog-master \
  skills/wordpress \
  skills/seo-research-master \
  skills/technical-seo-checker \
  skills/keyword-intelligence-os \
  skills/wp-reliability-ops \
  skills/git-sync \
  skills/grounding-compliance-os \
  skills/automation-ops
do
  test -d "$skill" || { echo "[validate] missing approved skill path: $skill"; exit 1; }
done

echo "[validate] repo structure ok"
