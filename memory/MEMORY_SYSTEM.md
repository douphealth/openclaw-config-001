# Memory System Contract

## Goal
Make recall faster, more reliable, and less noisy by separating durable memory from audit-trail noise.

## Canonical Layers
- `MEMORY.md` — curated durable memory only
- `memory/entities/*.md` — project/system/person memory
- `memory/RICH_INDEX.md` — pointers to dense daily files worth semantic lookup
- `memory/PLACEHOLDER_POLICY.md` — explicit ignore rule for synthetic daily stubs
- `memory/YYYY-MM-DD.md` — append-only audit trail
- `memory/heartbeat-state.json` — operational state, not narrative memory

## Retrieval Priority
1. `MEMORY.md`
2. `memory/entities/*.md`
3. `memory/RICH_INDEX.md`
4. recent real daily files
5. oversized historical logs only when needed

## Rules
- Placeholder daily files (`<=30 bytes`) are not working memory.
- Durable facts belong in `MEMORY.md` or `memory/entities/`, not only in daily logs.
- Large daily files must be distilled, then referenced from `RICH_INDEX.md`.
- New lessons that change future behavior should also be logged in `memory/improvements.md`.
- Secrets never go into memory files; only secret file locations may be referenced.

## Health Targets
- `MEMORY.md` stays concise and curated.
- Entity files cover active systems/projects.
- Search settings favor freshness + precision over raw breadth.
- Health checks must ignore placeholder stub files when judging memory quality.
