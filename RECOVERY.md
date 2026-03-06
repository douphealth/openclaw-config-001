# RECOVERY

## Goal
Rebuild the OpenClaw VPS fast, safely, and repeatably.

## Recovery order
1. Provision a fresh VPS with your hardened base image.
2. Install Node 22+ and OpenClaw.
3. Run `openclaw onboard --install-daemon`.
4. Clone this repository.
5. Restore non-secret repo files.
6. Recreate secrets from your external vault.
7. Place runtime config into `~/.openclaw/openclaw.json`.
8. Run `openclaw gateway status`.
9. Run `openclaw doctor`.
10. Run `make validate` and `make health`.

## Secrets checklist
Restore these from your vault, never from Git:
- model provider API keys
- channel tokens
- WordPress credentials
- SSH keys
- any webhook signing secrets

## Post-restore verification
- `openclaw gateway status` succeeds
- `openclaw doctor` returns no critical errors
- approved skills listed in `MANIFEST.yaml` exist
- backup and release scripts run successfully

## Failure policy
If validation fails:
- do not continue rollout
- revert to previous backup bundle
- compare `MANIFEST.yaml` to current runtime
