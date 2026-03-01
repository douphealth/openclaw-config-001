---
name: portfolio-command-center
description: Cross-site execution orchestration for WordPress portfolios. Use when managing multiple websites, deciding what to fix first, allocating daily execution capacity, consolidating blockers, and producing one clear high-velocity plan + status.
---

# Portfolio Command Center

## Scope Ownership
### Own
- Execute Cross-site execution orchestration for WordPress portfolios. Use when managing multiple websites, deciding what to fix first, allocating daily execution capacity, consolidating blockers, and producing one clear high-velocity plan + status.
- Apply workflows, gates, and outputs defined in this file and its references/scripts.

### Do Not Own
- Do not override responsibilities of more specific domain skills when one clearly matches.
- Do not claim completion for adjacent systems without their direct verification gates.

## Daily operating loop
1. build priority queue by impact/urgency/reversibility/confidence
2. select top 1–2 sites for active sprint
3. execute micro-batches with evidence
4. publish concise update: changes, verification, next queue

## Priority model
- P0: outage/trust/security/indexation blocker
- P1: canonical/schema/internal-link blocker on money pages
- P2: title/CTR/AEO upgrades
- P3: expansion/scale tasks

## Required artifacts per cycle
- `today-plan` (targets/risks/expected lift)
- `execution-log` (what changed)
- `verification-log` (proof/residuals)

## Anti-drift
- no random context switching mid-batch
- no done-claims without evidence
- if blocked >15 min, escalate with shortest unblock path