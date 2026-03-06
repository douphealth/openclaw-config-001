#!/usr/bin/env bash
set -euo pipefail

STAMP="$(date -u +%Y-%m-%dT%H%M%SZ)"
OUT="releases/openclaw-config-bundle-${STAMP}"

mkdir -p releases
bash scripts/validate.sh

tar \
  --exclude='.git' \
  --exclude='releases' \
  --exclude='.secrets' \
  -czf "${OUT}.tar.gz" \
  README.md RECOVERY.md OPERATIONS.md SECURITY.md MANIFEST.yaml \
  runtime skills-approved infrastructure scripts docs .gitignore Makefile publish.sh .editorconfig

sha256sum "${OUT}.tar.gz" > "${OUT}.sha256"

echo "[release] created ${OUT}.tar.gz"
echo "[release] created ${OUT}.sha256"
