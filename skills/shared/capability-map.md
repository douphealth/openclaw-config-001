# Capability Map

Machine-oriented summary of how the OpenClaw skill stack should compose.

## Layer 1 — Intake / Control
- `skill-router` → choose the right path
- `using-superpowers` → force serious execution discipline
- `task-intake-spec-writer` → convert vague requests into execution briefs

## Layer 2 — Orchestration
- `parallel-execution-director` → split and synthesize independent work
- `execution-state-ledger` → persist long-running state and checkpoints
- `batch-mutation-controller` → control sitewide writes safely

## Layer 3 — Recovery / Repair
- `failure-recovery-director` → contain, classify, recover
- `content-integrity-cleanup` → repair duplicated/broken content structures
- `wp-error-recovery` → WordPress-specific rescue work

## Layer 4 — Domain Execution
- `seo-command-center`
- `wordpress-growth-ops`
- `revenue-site-execution`
- `editorial-post-enhancement`
- `tracking-measurement`
- `email-automation-debugging`
- `service-funnel-architecture`

## Default Route Heuristics
- ambiguous + high-risk → `using-superpowers` + `task-intake-spec-writer`
- full audit → `site-audit-director`
- many independent checks → `parallel-execution-director`
- many similar writes → `batch-mutation-controller`
- unstable infra / partial corruption → `failure-recovery-director`
- duplicate or malformed content → `content-integrity-cleanup`

## Artifact Flow
1. **Execution brief**
2. **Worker plan / batch plan**
3. **Worker results / checkpoints**
4. **Verification evidence**
5. **Completion or recovery decision**
