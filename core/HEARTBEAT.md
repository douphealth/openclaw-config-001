# HEARTBEAT.md — Runtime Health & Session Log

_version: 2.1 | updated: 2026-03-03

## Purpose
Track session state, active errors, and subsystem health. Updated every significant execution.

## Current Session
- **Started:** (set at session start)
- **Mode:** (safe|aggressive|degraded)
- **Active Errors:** (none | list)

## Subsystem Health
| Subsystem | Status | Last Check |
|-----------|--------|------------|
| Gateway | (check systemctl) | |
| Codex Auth | (check preflight) | |
| Mission Control | (check /api/health) | |
| GitHub Sync | (check git push --dry-run) | |
| Social Pipeline | (check mode_control.py social status) | |

## Session Log
<!-- Append entries: [timestamp] action → outcome -->

## Sync Protocol
- Update on every significant tool output or file change
- Commit: `git commit -m "[HEARTBEAT] <summary>"`
- Verify against STATUS.md indicators
