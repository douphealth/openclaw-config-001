# HEARTBEAT.md — Periodic Check Instructions

_Read on every heartbeat poll. Keep this lean (under 20 lines)._

## Instructions

1. Check top 1-3 items from priority list below
2. If something needs attention, report it (no HEARTBEAT_OK)
3. If nothing needs attention, reply `HEARTBEAT_OK`
4. Rotate through items — don't check everything every time

## Priority Checks (rotate)

- **Memory maintenance** — Review recent daily files, promote durable truths to MEMORY.md
- **Active projects** — Any high-priority blockers or unfinished verification?
- **Revenue sites** — Money paths verified? Tracking working?

## Rules

- **Late night (23:00-08:00)**: Only surface urgent issues
- **Just checked <30min ago**: Reply HEARTBEAT_OK without re-checking
- **Human is clearly busy**: Don't interrupt unless critical
- **Batch checks**: Combine related checks in one pass

## Check State

Track last check times in `memory/heartbeat-state.json`:
```json
{
  "lastChecks": {
    "memory": null,
    "projects": null,
    "sites": null
  }
}
```

---

_Keep this file under 20 lines. Edit as priorities change._
