#!/usr/bin/env bash
set -euo pipefail
if [ $# -lt 1 ]; then
  echo "Usage: $0 <url>"
  exit 1
fi
URL="$1"
DIR="/home/openclaw/.openclaw/workspace/ops/browser-visual"
cd "$DIR"
node browser_ops.js screenshot --url "$URL" --device desktop
node browser_ops.js screenshot --url "$URL" --device mobile
