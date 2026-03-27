#!/usr/bin/env bash
set -euo pipefail
BASE="/home/openclaw/.openclaw"
WS="$BASE/workspace"
STAMP="$(date -u +%Y-%m-%dT%H%M%SZ)"
OUT_DIR="$WS/ops/backups/system"
OUT_FILE="$OUT_DIR/workspace-critical-core-${STAMP}.tar.gz"
mkdir -p "$OUT_DIR"
tar -czf "$OUT_FILE" \
  -C "$BASE" \
  workspace/AGENTS.md \
  workspace/SOUL.md \
  workspace/USER.md \
  workspace/TOOLS.md \
  workspace/IDENTITY.md \
  workspace/MEMORY.md \
  workspace/skills \
  workspace/memory \
  workspace/clawflows \
  openclaw.json
printf 'BACKUP_CREATED %s\n' "$OUT_FILE"
stat --printf='SIZE_BYTES %s\n' "$OUT_FILE" 2>/dev/null || wc -c "$OUT_FILE"
