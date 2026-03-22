# Memory Regression Protocol

## Purpose
Prevent memory quality drift and define automatic responses before recall quality degrades noticeably.

## Targets
- Score target: **90+**
- Stretch target: **95+**
- Placeholder files in active `memory/`: **0**
- Entity files: **5+**
- `MEMORY.md` size target: **<=180 lines preferred**, hard attention at **>220**

## Automatic Responses
### If placeholder files reappear
- Run `scripts/archive-placeholder-memory.ps1`
- Re-run `scripts/memory-health-check.ps1`
- Log the regression in `memory/improvements.md`

### If a daily log exceeds 12KB
- Run `scripts/memory-distill.ps1 -Date <date>`
- Preserve raw copy under `artifacts/memory/raw/`
- Create or refresh `<date>-distilled-summary.md`
- Replace active daily log with compact summary when safe

### If score drops below 90
- Generate dashboard artifact with `scripts/memory-maintenance.ps1`
- Review `MEMORY.md`, `memory/entities/*.md`, and last 3 real daily files
- Promote any missing durable facts into entities or `MEMORY.md`

### If score drops below 75
- Treat as urgent hygiene failure
- Run full maintenance pass immediately
- Report the regression clearly with causes and proof

## Canonical Tools
- `scripts/memory-health-check.ps1`
- `scripts/memory-distill.ps1`
- `scripts/archive-placeholder-memory.ps1`
- `scripts/memory-maintenance.ps1`
