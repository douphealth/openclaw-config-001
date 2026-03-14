# Memory Architecture

## File Hierarchy
- `MEMORY.md` — Long-term curated memory (loaded at session start)
- `memory/YYYY-MM-DD.md` — Daily notes (chronological raw log)
- `memory/people/` — Person profiles and preferences
- `memory/sites/` — Site configs, access, quirks
- `memory/projects/` — Project status and decisions
- `memory/ops/` — Operational procedures and scripts

## Promotion Rules
- Daily → Entity: when info is current and actionable
- Entity → MEMORY.md: when it's a durable truth or lesson
- MEMORY.md → Archive: when superseded by newer info

## Pattern Lifecycle (foundry pattern)
1. Failure occurs → note in daily
2. Resolution found → note with solution
3. Pattern emerges (3+ times) → create rule
4. Rule validated → promote to MEMORY.md
