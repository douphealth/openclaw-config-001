# HEARTBEAT.md

Read on every heartbeat poll. Keep this lean.

## Instructions

1. Check top 1-3 items from the priority list below
2. If something needs attention, report it without `HEARTBEAT_OK`
3. If nothing needs attention, reply `HEARTBEAT_OK`
4. Rotate checks; do not re-run everything every time

## Priority Checks

- **Memory maintenance** — review recent daily files, promote durable truths to `MEMORY.md`
- **Active OpenClaw health** — config validity, gateway health, model/auth regressions
- **Workspace hygiene** — stale files, broken skills, obvious drift in runtime docs/config
- **High-value projects** — blockers, unfinished verification, fragile automations

## Severity Rules

- **Urgent:** gateway down, auth broken, failed reminders/automation, public-facing failures, or anything blocking normal operation
- **Soon:** documentation drift, stale memory, recoverable warnings, low-risk cleanup
- **Quiet hours (23:00-08:00):** only surface urgent issues

## Rules

- **Just checked <30min ago**: reply `HEARTBEAT_OK` unless something changed
- **Human is clearly busy**: do not interrupt unless useful
- **Batch checks**: combine related checks in one pass
- Track check timestamps/state in `memory/heartbeat-state.json`
