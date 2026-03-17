---
name: quality-scorecard
description: Use when scoring skill quality, auditing workflow efficiency, measuring trigger accuracy, or tracking improvement over time. Prioritizes architecture-critical skills, remediation queues, and trend tracking instead of one-off scoring only.
---

# Quality Scorecard

## Purpose
Measure and track skill quality, trigger accuracy, verification strength, and workflow efficiency over time so weak skills can be identified, prioritized, and improved.

## Use this when
- auditing skill performance after execution
- scoring skills for improvement priority
- measuring workflow efficiency of multi-skill work
- tracking quality trends over time
- deciding which skills should be hardened first

## Do NOT use this for
- creating or editing skills directly (→ `skill-authoring-standard`)
- routing tasks to skills (→ `skill-router`)
- claiming a skill is good without execution evidence where evidence exists

## Scoring model
### 1. Skill quality score (0-100)
Score each skill on 5 dimensions (20 points each):

| Dimension | 20 pts | 15 pts | 10 pts | 5 pts | 0 pts |
|---|---|---|---|---|---|
| Trigger clarity | Fires exactly when needed, never false-positive | Usually correct | Sometimes ambiguous | Often fires wrong | No clear trigger |
| Output contract | Artifact + evidence + decision + next all defined | 3 of 4 | 2 of 4 | 1 of 4 | None |
| Verification | Proof required before done | Partial proof | Checklist exists | Mentioned only | None |
| Token efficiency | Scripts + references + lean structure | Good structure | Some waste | Bloated | No optimization |
| Boundary clarity | Clear do-not-use + routing discipline | Has boundaries | Some overlap | Vague | No boundaries |

### 2. Workflow efficiency score
After a multi-skill workflow completes, measure:
- steps completed vs planned
- gates passed first time
- rework required
- token estimate vs actual
- time estimate vs actual
- where thrashing or duplication occurred

## Priority model
### Score bands
- 80-100: ✅ Production-grade
- 60-79: ⚠️ Needs polish
- 40-59: 🔶 Needs work
- <40: 🔴 Needs rewrite

### Architecture-critical skills
Prioritize these first when present:
- skill-router
- swarm-orchestrator
- auto-verification
- quality-scorecard
- workflow-macros
- skill-authoring-standard

### Remediation queue rules
Flag a skill for remediation if any are true:
- total score < 80 for an architecture-critical skill
- total score < 70 for any frequently used skill
- repeated false completion or verification failure occurs
- trigger ambiguity causes repeated routing waste
- token inefficiency is materially harming execution quality

## Reporting standard
Save reports to:
- `ops/reports/quality-scorecard-YYYY-MM-DD.md`

Each report should include:
- scope
- method
- score table
- findings by skill or workflow
- bottlenecks
- prioritized remediation list
- decision
- next actions

## Cadence
Use one of these cadences depending on need:
- after a major workflow
- after a major skill refactor
- during periodic system hardening
- when repeated quality problems appear

## Checks and common mistakes
- Score skills after real use whenever possible, not only in isolation.
- Track trends, not just one-off scores.
- Focus improvement on architecture-critical and frequently used skills first.
- Separate “good writing” from “good operating behavior”.
- Do not score a skill highly if it still permits fake completion.

## Output contract
**Artifact:** quality score report saved to `ops/reports/quality-scorecard-YYYY-MM-DD.md`
**Evidence:** score breakdown, observed behavior, and comparison to previous reports where available
**Decision:** prioritized list of skills or workflows to improve
**Next:** remediation queue and next hardening actions
