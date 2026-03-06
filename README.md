# openclaw-config-001

Production control plane for the OpenClaw VPS.

## Purpose
This repository is the non-secret source of truth for:
- approved OpenClaw skills
- runtime configuration templates
- operations and recovery runbooks
- release bundles and validation scripts

## Fast paths
- Validate: `make validate`
- Backup: `make backup`
- Release: `make release`
- Health: `make health`
- Restore dry run: `make restore-dry-run`

## Repo contract
- Secrets are never committed.
- `MANIFEST.yaml` defines the production-approved skill set.
- `skills/` remains the legacy inventory until migration is complete.
- `skills-approved/` is the curated approval layer.
- Every release generates a checksum.

## Core files
- `RECOVERY.md`
- `OPERATIONS.md`
- `SECURITY.md`
- `MANIFEST.yaml`

## OpenClaw runtime assumptions
- Config path: `~/.openclaw/openclaw.json`
- Install / daemon bootstrap: `openclaw onboard --install-daemon`
- Health checks: `openclaw gateway status`, `openclaw doctor`

## Migration note
This repo previously mixed many top-level docs and a broad skill inventory. The new structure keeps compatibility while introducing a stricter production path.
