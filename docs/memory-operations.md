# Memory Operations

Enterprise memory layer for OpenClaw workspaces.

## Included components
- `memory/MEMORY_SYSTEM.md` — canonical memory-layer contract
- `memory/MEMORY_REGRESSION_PROTOCOL.md` — thresholds and automatic responses
- `memory/RICH_INDEX.md` — startup-friendly dense memory pointers
- `memory/PLACEHOLDER_POLICY.md` — ignore/archival rules for synthetic date stubs
- `scripts/archive-placeholder-memory.ps1` — archive active placeholder noise
- `scripts/memory-distill.ps1` — oversized-log distillation entry point
- `scripts/memory-health-check.ps1` — scored memory health check
- `scripts/memory-maintenance.ps1` — self-healing maintenance runner + dashboard generator

## Operating targets
- Score target: 90+
- Stretch target: 95+
- Placeholder files in active memory: 0
- Entity files: 5+
- `MEMORY.md`: keep concise and curated

## Maintenance pattern
1. Run `scripts/memory-maintenance.ps1`
2. Review generated dashboard artifact
3. If score regresses, follow `memory/MEMORY_REGRESSION_PROTOCOL.md`
4. Promote durable facts out of daily logs and into entity memory

## Why this exists
Memory quality degrades when placeholder files, oversized logs, and rediscovery-heavy workflows accumulate. This layer keeps memory clean, fast, measurable, and regression-aware.
