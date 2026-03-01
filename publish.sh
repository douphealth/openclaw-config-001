#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_DIR"

echo "[publish] repo: $REPO_DIR"

git fetch origin

# Ensure working tree is clean
if [[ -n "$(git status --porcelain)" ]]; then
  echo "[publish] ERROR: working tree is not clean. Commit/stash first."
  exit 1
fi

# Push main
if git show-ref --verify --quiet refs/heads/main; then
  echo "[publish] pushing main"
  git checkout main
  git pull --rebase origin main || true
  git push origin main
else
  echo "[publish] WARNING: main branch not found locally"
fi

# Push enterprise-curated
if git show-ref --verify --quiet refs/heads/enterprise-curated; then
  echo "[publish] pushing enterprise-curated"
  git checkout enterprise-curated
  git pull --rebase origin enterprise-curated || true
  git push origin enterprise-curated
else
  echo "[publish] WARNING: enterprise-curated branch not found locally"
fi

# Optional tag support: ./publish.sh v2026.03.01-enterprise-curated
if [[ "${1:-}" != "" ]]; then
  TAG="$1"
  echo "[publish] creating/pushing tag: $TAG"
  if git rev-parse "$TAG" >/dev/null 2>&1; then
    echo "[publish] tag already exists locally: $TAG"
  else
    git tag -a "$TAG" -m "release $TAG"
  fi
  git push origin "$TAG"
fi

echo "[publish] done"
