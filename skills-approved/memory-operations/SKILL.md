---
name: memory-operations
description: Use when organizing, reviewing, consolidating, promoting, or improving OpenClaw memory across `memory/YYYY-MM-DD.md`, `MEMORY.md`, and entity memory files under `memory/people/`, `memory/sites/`, `memory/projects/`, or `memory/ops/`. Triggers on requests to remember something, improve memory, review memory, consolidate notes, promote durable facts, clean up stale memory, or make semantic memory retrieval more useful.
---

# Memory Operations

## Purpose
Keep OpenClaw memory high-signal, current, and easy to retrieve. Operate across three layers: daily notes (ephemeral), entity files (current truth), and `MEMORY.md` (curated wisdom).

## Use this when
- Remembering something, consolidating notes, or reviewing memory health
- Promoting facts from daily → entity → long-term memory
- Cleaning up stale, contradictory, or duplicated memory entries
- Improving semantic search quality or entity memory structure
- Running periodic memory maintenance (heartbeat or cron)

Do **not** use for: general project documentation (use project files directly), one-off notes (write to daily), or file operations unrelated to memory.

## Do this

### Writing & promotion
1. Decide layer: daily note (raw), entity file (current state), or `MEMORY.md` (durable insight).
2. Prefer updating current truth in an existing entity file over appending history.
3. Promote durable operational state into entity files before promoting into `MEMORY.md`.
4. Use semantic memory search when the exact file is unclear.
5. Consolidate repeated truths instead of copying across files.

### Pattern lifecycle (from failure to crystallized knowledge)
6. When a failure occurs: capture the failure and resolution in the daily note.
7. After 2–3 instances, identify the pattern and document it in the relevant entity or ops file.
8. Promote crystallized patterns (proven, reusable) into `MEMORY.md` or a skill hook.
9. Delete the intermediate drafts — keep only the distilled version.
10. Pattern maturity: raw observation → validated pattern → actionable rule → skill-embedded hook.

### Memory health check (run monthly or on retrieval degradation)
11. Scan daily notes from the last 7 days for promotion candidates.
12. Check entity files for stale state (values that no longer match reality).
13. Verify `MEMORY.md` entries are still true and actionable.
14. Run a semantic search test: query 3 known facts, confirm they surface correctly.
15. Prune contradictions, merge duplicates, update timestamps.
16. Score health: 5/5 = all pass, 3–4/5 = maintenance needed, <3 = rebuild.

### Semantic search & entity memory best practices
- Entity files should have a clear `## Current State` section at the top.
- Use concrete nouns and specific values in memory entries (avoid "seems like" or "maybe").
- Keep entity files under 50 lines — split when they grow beyond that.
- Tag entity files with frontmatter: `type`, `last-updated`, `source`.
- When semantic search returns wrong files, the problem is usually vague writing, not the search engine.
- Write entries in declarative sentences with facts, not narrative summaries.
- Front-load the most actionable information in each file.

## Common memory patterns

### Capturing a decision
```
## Current State
- Decision: [what was decided]
- Date: [when]
- Context: [why]
- Reversible: [yes/no, and how]
```

### Capturing a lesson
```
## Lessons Learned
- [Situation] → [What happened] → [What to do instead]
- Tag with the domain (ops, dev, content) for future retrieval
```

### Capturing entity state
```
## Current State
- Status: [active/paused/archived]
- Key metrics: [numbers]
- Last reviewed: [date]
- Open items: [bullets]
```

## Resources
Read when needed:
- `references/memory-architecture.md` — memory system design and layer model
- `references/retrieval-order.md` — how memory search ranks results
- `references/promotion-rules.md` — when to promote between layers
- `references/review-workflow.md` — periodic review procedure
- `references/health-check-workflow.md` — memory health diagnostics

## Checks and common mistakes
- Do not use daily notes as the only memory layer — they rot fast.
- Do not turn `MEMORY.md` into a dumping ground — it's curated, not comprehensive.
- Do not leave entity files stale when current state changes.
- Do not trust semantic search to rescue low-quality memory writing.
- Do not preserve five versions of the same blocker when one current bullet will do.
- Do not promote transient operational state into `MEMORY.md` — entity files are the right home.
- Do not skip the health check when retrieval quality degrades — it compounds.

## Output contract
When performing memory operations, deliver:
- **Promotion log**: list of items promoted between layers (source → destination, reason)
- **Pruned entries**: items removed or merged (with reason)
- **Updated files**: list of files modified
- **Health status**: pass/fail on the 5-point health check with notes on any failures
- **Pattern findings**: any new patterns identified from repeated observations

## Output Contract
**Artifact**: Skill-specific deliverable (report, fix, config, or document)
**Evidence**: Proof that the work was completed correctly
**Decision**: What was decided or recommended
**Next**: Follow-up action or monitoring period
