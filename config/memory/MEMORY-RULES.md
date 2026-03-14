# MEMORY-RULES.md — Memory System Operating Manual

## Purpose
Keep OpenClaw memory high-signal, retrievable, and operationally useful.

This file defines how memory should be written, promoted, reviewed, and pruned.

## Core Principle
Do not optimize for storing more.
Optimize for storing what will matter later.

Good memory is:
- Durable
- Structured
- Low-noise
- Easy to retrieve by subject
- Updated when reality changes

## Memory Layers

### 1. Daily Memory (`memory/YYYY-MM-DD.md`)
**Use for:**
- Chronological notes of meaningful events
- Decisions, blockers, constraints, state changes
- Session-local context worth preserving

**Do NOT use for:**
- Transcript-style dumping
- Repetitive chatter
- Obvious filler

### 2. Long-Term Curated Memory (`MEMORY.md`)
**Use for:**
- Stable truths and durable lessons
- Recurring user preferences
- Long-term priorities
- Important cross-session context

**Do NOT use for:**
- Raw meeting/session notes
- Temporary issues
- Daily noise

### 3. Entity Memory (`memory/entities/`)
Locations:
- `memory/people/` — Person-specific context
- `memory/sites/` — Site-specific state and knowledge
- `memory/projects/` — Project tracking
- `memory/ops/` — Operational patterns and systems

**Use for:**
- Subject-specific state
- Operational continuity
- Work retrieved by entity rather than date

## Promotion Rules

### Daily → Entity Memory when:
- Information belongs clearly to a person, site, project, or system
- Likely to matter again
- Affects future execution
- Describes a current blocker, decision, or known state

### Daily/Entity → MEMORY.md when:
- Durable truth that won't change soon
- Stable preference
- Recurring pattern
- Worth remembering across many future sessions

### Keep in Daily Memory only when:
- Session-local only
- Unlikely to matter later
- Not important enough for entity or long-term memory

## Noise Control Rules

### Do NOT store:
- Repetitive restatements of the same issue
- Emotional filler without operational value
- Obvious transcript residue
- Large blocks of chat rewritten as notes
- Stale facts already replaced by newer ones

### Prefer:
- One updated bullet over many duplicate bullets
- One clear current blocker over five versions of the same blocker
- One current truth over contradictory old fragments

## Update Rules

When reality changes:
1. Update the relevant entity file
2. Don't leave outdated info uncorrected
3. If a blocker is resolved, mark it resolved or replace it
4. If a priority changes, update the file directly

**Memory should reflect the current best-known reality.**

## Retrieval Order

When working on something specific:
1. Check the relevant entity memory file first
2. Use semantic memory search when exact location is unclear
3. Check recent `memory/YYYY-MM-DD.md` files
4. Check `MEMORY.md` for durable context if relevant

Use subject memory before date memory.
Use semantic search to find likely notes, not to replace structured files.

## Review Cadence

### Daily
- Write meaningful events to daily memory
- Update entity files when state changes materially

### Weekly
- Review recent daily files
- Promote durable facts into entity files
- Consolidate duplicates
- Prune noise
- Update `MEMORY.md` only with stable cross-session truths

### Periodically
- Archive stale summaries
- Remove outdated assumptions
- Verify active project/site files reflect reality
- Run memory health check when retrieval quality degrades

## Memory Content Standards

- Prefer bullets
- Be terse
- Prefer facts over interpretation

**Store:**
- Decisions
- Blockers
- Constraints
- Owners
- Access changes
- Status shifts
- Next actions

**Avoid vague notes like:**
- "talked about website stuff"
- "worked on some fixes"
- "things improved a bit"

**Use concrete notes like:**
- "Installed WooCommerce + WooPayments on [Site]"
- "Manual email sending works; automatic welcome flow still unresolved"
- "Prototype exists but still staging-only"

## Security Rule

- Never store credentials in memory files
- Use `.secrets/` directory for all secrets
- Memory should retain access-state facts when useful, not become a credential dump
- Never expose memory in shared/group contexts without sanitizing

## Good Memory Test

A memory note is good if future-you can use it to answer one of these quickly:
- What matters now?
- What changed?
- What is blocked?
- What was decided?
- What should happen next?
- Where does this belong?

If the note doesn't help with that, it's noise.
