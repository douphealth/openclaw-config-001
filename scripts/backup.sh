#!/usr/bin/env bash
set -euo pipefail

STAMP="$(date -u +%Y-%m-%dT%H%M%SZ)"
OUTDIR="releases"
BASENAME="openclaw-backup-${STAMP}"

mkdir -p "${OUTDIR}" backups/manifests

tar -czf "${OUTDIR}/${BASENAME}.tar.gz" \
  README.md RECOVERY.md OPERATIONS.md SECURITY.md MANIFEST.yaml \
  scripts docs infrastructure runtime skills-approved .gitignore Makefile 2>/dev/null || true

sha256sum "${OUTDIR}/${BASENAME}.tar.gz" > "${OUTDIR}/${BASENAME}.sha256"

cat > "backups/manifests/${BASENAME}.manifest.txt" <<MANIFEST
created_at=${STAMP}
artifact=${OUTDIR}/${BASENAME}.tar.gz
checksum=${OUTDIR}/${BASENAME}.sha256
MANIFEST

echo "[backup] created ${OUTDIR}/${BASENAME}.tar.gz"
echo "[backup] next step: encrypt and upload outside the VPS"
