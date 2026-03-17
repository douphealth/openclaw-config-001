---
name: memory-operations
description: Enterprise memory management for OpenClaw agents. Use when organizing, reviewing, consolidating, promoting, or improving OpenClaw memory across daily notes, MEMORY.md, and entity memory files. Triggers on remembering something, improving memory, reviewing memory, consolidating notes, promoting durable facts, cleaning up stale memory, or making semantic memory retrieval more useful.
---

# Memory Operations — Enterprise Agent Memory Management

## Purpose
Keep agent memory organized, searchable, and useful across sessions. Ensure continuity, reduce retrieval noise, and promote durable knowledge.

## When to Use
- Remembering facts, decisions, or preferences for future sessions
- Reviewing and consolidating daily memory files
- Cleaning up stale or outdated memory entries
- Promoting daily notes to long-term memory
- Organizing entity memory (people, sites, projects, operations)

**Do NOT use for:** General note-taking (→ write directly to files), search operations (→ use `memory_search`).

## Memory Architecture

### File Structure
```
memory/
├── YYYY-MM-DD.md          # Daily raw logs (one file per session)
├── heartbeat-state.json   # Last check timestamps
├── people/                # Entity memory for individuals
│   └── {name}.md
├── sites/                 # Entity memory for managed sites
│   └── {domain}.md
├── projects/              # Entity memory for projects
│   └── {project}.md
└── ops/                   # Entity memory for operations
│   └── {operation}.md
MEMORY.md                  # Long-term curated memory (auto-read in main session)
```

### Memory Types
| Type | Location | Purpose | Retention |
|------|----------|---------|-----------|
| Daily logs | `memory/YYYY-MM-DD.md` | Raw events, decisions, context | Rolling 30 days |
| Entity memory | `memory/{type}/{name}.md` | Structured facts about entities | Updated as needed |
| Long-term | `MEMORY.md` | Curated, durable truths | Permanent |
| Heartbeat state | `heartbeat-state.json` | Last check timestamps | Auto-managed |

## Operations

### 1. Remember (Capture)
When the user says "remember this":
- Extract the key fact or decision
- Save to appropriate location:
  - Daily events → `memory/YYYY-MM-DD.md`
  - Entity facts → `memory/{type}/{name}.md`
  - Durable truths → `MEMORY.md`
- Include timestamp and context ("why" and "when")

### 2. Consolidate (Daily → Long-Term)
Periodically (during heartbeats or manual trigger):
- Review daily notes from past 7-14 days
- Identify durable facts worth keeping long-term
- Promote to entity memory or MEMORY.md
- Remove redundant entries from daily files once promoted

### 3. Clean Up
- Remove stale entries where reality has changed
- Archive outdated daily notes (>30 days)
- Deduplicate overlapping entries
- Update entity memory when facts change

### 4. Retrieve Efficiently
- Use `memory_search` for semantic queries
- Use `memory_get` for specific file reads
- Entity memory files are best for current state
- Daily files are best for chronological context

## Rules
- **Write, don't trust memory**: "Mental notes" don't survive restarts
- **Timestamps matter**: Always include "when" for context
- **Entity > Daily for state**: Current truth goes in entity files
- **MEMORY.md is curated**: Only durable, important facts
- **Privacy first**: Don't store secrets without encryption


## Self-Critique Scorecard (/25)
After every operation, score yourself:

| Dimension | Score | Notes |
|-----------|-------|-------|
| **Functionality** (1-5) | ? | Does it work perfectly and meet all requirements? |
| **Quality** (1-5) | ? | Is it enterprise-grade and production-ready? |
| **Verification** (1-5) | ? | Was it verified via multiple methods? |
| **Speed** (1-5) | ? | Was execution optimal with parallel operations? |
| **Learning** (1-5) | ? | Were new patterns documented and memory updated? |

**Target: 22+/25 before claiming completion**

### Pre-Flight Checklist
- [ ] Credentials verified and target exists
- [ ] Rollback plan identified
- [ ] Success criteria defined
- [ ] Anti-patterns reviewed

### Post-Flight Checklist
- [ ] Verified via API response + live check
- [ ] Quality score logged to memory/YYYY-MM-DD.md
- [ ] Skill references updated if new patterns discovered
- [ ] No common mistakes made

## Output Contract
**Artifact**: Updated memory files with organized, timestamped content
**Evidence**: Memory files exist and are properly structured
**Decision**: Fact remembered or consolidated
**Next**: Will be retrieved by `memory_search` in future sessions

## Anti-Patterns
- ❌ Storing secrets in memory without encryption
- ❌ Memory bloat: everything goes to MEMORY.md (keep it curated)
- ❌ No context: storing facts without "why" or "when"
- ❌ Daily notes promoted without deduplication
- ❌ Forgetting to update entity memory after state changes
- ❌ Never cleaning up stale entries

## Compatibility
- Targets current WordPress 6.9+ where applicable
- REST API + WP-CLI preferred over browser automation
- Batch operations via `_fields` + `per_page=100` + `concurrent.futures`
- Browser automation only when API/CLI insufficient

## Inputs Required (Pre-Flight)
Before executing any task in this skill:
1. **Target identification** — What site, page, post, or system is being operated on?
2. **Auth verification** — Confirm credentials work (test API call or CLI command)
3. **Current state** — Understand what exists before making changes (GET before POST)
4. **Environment** — Production vs staging (assume production unless stated)
5. **Constraints** — No downtime? Preserve SEO? Preserve data? Budget limits?

## Triage Protocol
Before ANY operation:
1. **Identify** — What type of content/system/problem is this?
2. **Check state** — Query current state via API/CLI before modifying
3. **Verify creds** — Confirm authentication works
4. **Plan rollback** — How to undo if something breaks?
5. **Scope check** — Is this a single item or batch? Scale determines approach.

## Speed Optimizations
- **API calls**: Always use `_fields` parameter (80%+ payload reduction)
- **Pagination**: Use `per_page=100` for list endpoints
- **Parallelism**: Use `concurrent.futures` for independent operations (max 10/site)
- **Caching**: Store results in session — never re-fetch same data
- **Batching**: Group similar operations into single API calls where possible
- **Direct CLI**: Use WP-CLI `wp db query` for complex operations

## Error Recovery (Auto-Learning)
- Track error patterns — after 2 failures, try alternative approach
- Log recurring fixes to `memory/YYYY-MM-DD.md`
- Update references when new patterns discovered
- Rollback plan: Know how to undo before making changes

## Self-Critique Scorecard (/25)
Before claiming complete, score yourself:
1. **Triage** (1-5): Was current state fully understood before changes?
2. **Execution** (1-5): Was the operation clean, efficient, correct?
3. **Verification** (1-5): Was the result verified via API/live check?
4. **Rollback** (1-5): Can changes be undone if issues found?
5. **Learning** (1-5): Were new patterns documented for future use?

**Target: 22+/25**

## Output Contract
- **Artifact**: What was created/changed/deleted
- **Evidence**: API response proof + live verification
- **Decision**: Success/failure with reasoning
- **Next**: What follow-up is needed (if any)
