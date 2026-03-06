#!/usr/bin/env bash
set -euo pipefail

echo "[health] repo validation"
bash scripts/validate.sh

if command -v openclaw >/dev/null 2>&1; then
  echo "[health] openclaw detected"
  openclaw gateway status || true
  openclaw doctor || true
else
  echo "[health] openclaw binary not found in PATH"
fi
