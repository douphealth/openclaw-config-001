#!/usr/bin/env bash
set -euo pipefail

DRY_RUN="${1:-}"

if [[ "${DRY_RUN}" == "--dry-run" ]]; then
  echo "[restore] dry run ok"
  echo "[restore] expected inputs:"
  echo "  - release tarball"
  echo "  - checksum file"
  echo "  - external secrets vault"
  echo "  - target path ~/.openclaw/openclaw.json"
  exit 0
fi

echo "[restore] restore is intentionally manual for safety"
echo "[restore] see RECOVERY.md"
exit 0
