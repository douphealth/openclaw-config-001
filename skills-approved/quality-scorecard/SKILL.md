---
name: quality-scorecard
description: Use when scoring skill quality, auditing skill performance, measuring workflow efficiency, or tracking improvement over time. Triggers on requests like "how good is this skill", "score our skills", "measure efficiency", "audit skill quality", or "track token usage".
---

# Quality Scorecard

## Purpose
Measure and track skill quality, trigger accuracy, output value, and token efficiency over time.

## Use this when
- Auditing skill performance after execution
- Scoring skills for improvement priority
- Measuring token efficiency of workflows
- Tracking quality trends over time

## Do NOT use this for
- Creating or editing skills (→ skill-authoring-standard)
- Routing tasks to skills (→ skill-router)

## Do this

### 1. Skill Quality Score (0-100)
Score each skill on 5 dimensions (20 points each):

| Dimension | 20 pts | 15 pts | 10 pts | 5 pts | 0 pts |
|-----------|--------|--------|--------|-------|-------|
| **Trigger clarity** | Fires exactly when needed, never false-positive | Usually correct | Sometimes ambiguous | Often fires wrong | No clear trigger |
| **Output contract** | Artifact + evidence + decision + next all defined | 3 of 4 | 2 of 4 | 1 of 4 | None |
| **Verification** | Proof required before "done" | Partial proof | Checklist exists | Mentioned only | None |
| **Token efficiency** | Scripts handle repeat work, references on-demand | Good structure | Some waste | Bloated | No optimization |
| **Boundary clarity** | Clear "do not use" with skill routing | Has boundaries | Some overlap | Vague | No boundaries |

### 2. Workflow Efficiency Score
After a multi-skill workflow completes:
- **Steps completed vs planned**: X/Y
- **Gates passed first time**: X/Y
- **Rework required**: Y/N (which step needed redo?)
- **Token estimate vs actual**: ~X tokens (over/under?)
- **Time estimate vs actual**: ~X minutes

### 3. Improvement Priority
Skills scoring <70 get flagged for improvement:
- 80-100: ✅ Production-grade
- 60-79: ⚠️ Needs polish
- 40-59: 🔶 Needs work
- <40: 🔴 Needs rewrite

## Output Contract
**Artifact**: Quality score report saved to ops/reports/quality-scorecard-YYYY-MM-DD.md
**Evidence**: Score breakdown by dimension, comparison to previous scores
**Decision**: Priority list of skills to improve
**Next**: Schedule improvement for flagged skills

## Checks
- Score skills after they're used, not in isolation
- Track trends — is quality improving over time?
- Focus improvement on frequently-used skills first
- Compare actual vs estimated token usage
