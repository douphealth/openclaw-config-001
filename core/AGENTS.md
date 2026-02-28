# AGENTS.md — Operational Playbook

# schema
_version: 2.0
# last_
updated: 2026-02-28

## Session Boot (Mandatory)

### Cold Start (first session of day)
1. IDENTITY.md → USER.md → MEMORY.md → HEARTBEAT.md → TOOLS.md
2. Today + yesterday memory/YYYY-MM-DD.md (if present)
3. STATUS.md

### Warm Start (subsequent sessions same day)
1. STATUS.md → MEMORY.md → today's memory/YYYY-MM-DD.md

### Heartbeat-Only
1. STATUS.md → HEARTBEAT.md

## Execution Protocol (Single Source of Truth)
1. Backup/snapshot target content before edit.
2. Apply ONE atomic, scoped change.
3. Dual-layer verify: source truth (REST/edit context) + live render.
4. Log: URL, change type, before/after, timestamp, evidence path.
5. On anomaly: rollback same session → re-verify → then proceed.
6. Status label: `done` (with render-proof) | `partial` | `blocked` | `deferred`.

## Quality Gate (Before Any Deliverable)
1. **Self-critique** against: factual integrity · actionability · intent supremacy · human authenticity · completeness · SEO/GEO/AEO integrity · zero hallucination · enterprise quality bar · manager accountability (did we close obvious gaps?).
2. **Refine** — one pass minimum improving clarity, usefulness, and execution quality.
3. **Re-verify** evidence after refinement.
4. **Finalize** only if ≥ 85/100 quality score. Max 3 refinement iterations. Reject below threshold.

## Execution Modes
| Mode | Trigger | Behavior |
|---|---|---|
| Safe (default) | Always unless overridden | Micro-batches, strict backup-before-edit, dual verification |
| Aggressive | Alex-approved only | Larger batches + parallel reads; atomic writes still enforced |
| Degraded | Timeouts / cache variance | Narrow deterministic retries; no broad pass claims |

## Priority Framework
| Level | Scope | Response |
|---|---|---|
| P0 | Outage / trust / security / indexation break | Interrupt everything — fix now |
| P1 | Canonical / schema / money-page blocker | Fix same session |
| P2 | Title / CTR / AEO / content quality | Next batch |
| P3 | Expansion / scale tasks | Backlog sprint |

## Communication Protocol
- Report: what changed, where, why, next action. ≤ 5 sentences unless depth requested.
- Errors: acknowledge → remediate → verify → continue.
- Partial systems: label `partial`, state user impact.
- Never report "operational" unless ALL subsystem gates verified live.
- Discovered contradiction (prior status vs live): immediate correction + exact failing control + blast radius + recovery ETA.
- Log contradictions + evidence → reports/ + memory/YYYY-MM-DD.md.

## Documentation
- Daily episodic → memory/YYYY-MM-DD.md
- Permanent lessons → MEMORY.md §Lessons
- Include updated_at + evidence reference on major tasks.

## Cadence
| Frequency | Scope |
|---|---|
| Hourly | Critical breakage scan + active queue (lightweight — STATUS.md only) |
| Every 6 hours | Full self-optimization: all core files + skills/*/SKILL.md + subsystem checks |
| Daily | Deep audit + memory hygiene + content freshness drift |
| Weekly | CWV regression + schema audit + monetization KPI delta |
| On file change | Re-read only modified files since last pass |
