---
name: quality-scorecard
description: Enterprise quality scoring and performance measurement for skills, workflows, and portfolio sites. Use when auditing skill performance, measuring workflow efficiency, tracking quality trends, scoring site health, or generating quality reports with prioritized improvement recommendations.
---

# Quality Scorecard — Enterprise Quality Measurement

## Purpose
Measure, track, and improve quality across skills, workflows, and managed sites with quantified scoring and prioritized improvement plans.

## When to Use
- Post-execution skill quality audits
- Workflow efficiency measurement
- Portfolio site health scoring
- Token efficiency analysis
- Quality trend tracking over time
- Improvement priority ranking

**Do NOT use for:** Creating skills (→ `skill-authoring-standard`), routing tasks (→ `skill-router`), SEO auditing (→ `seo-audit-playbook`).

## Skill Quality Score (0-100)

Score each skill on 5 dimensions (20 points each):

| Dimension | 20 pts (Excellent) | 15 pts (Good) | 10 pts (Fair) | 5 pts (Poor) | 0 pts (Missing) |
|-----------|-------------------|---------------|---------------|--------------|-----------------|
| **Trigger clarity** | Fires exactly when needed, zero false positives | Usually correct | Sometimes ambiguous | Often fires wrong | No clear trigger |
| **Output contract** | Artifact + Evidence + Decision + Next all defined | 3 of 4 defined | 2 of 4 defined | 1 of 4 defined | None |
| **Verification** | Proof required before "done" | Partial proof | Checklist exists | Mentioned only | None |
| **Token efficiency** | Scripts handle repeat work, references on-demand | Good structure | Some waste | Bloated | No optimization |
| **Boundary clarity** | Clear "do not use" with routing to alternatives | Has boundaries | Some overlap | Vague | No boundaries |

### Quality Grades
| Score | Grade | Action |
|-------|-------|--------|
| 90-100 | A+ | Production-grade, reference for others |
| 80-89 | A | Production-grade, minor polish possible |
| 70-79 | B | Needs polish before next use |
| 60-69 | C | Needs significant improvement |
| 40-59 | D | Needs rewrite |
| <40 | F | Replace or remove |

## Workflow Efficiency Score

After any multi-skill workflow:
```
Steps completed: X/Y
Gates passed first time: X/Y
Rework required: Y/N (step: ___)
Token estimate vs actual: ~X (over/under by Y%)
Time estimate vs actual: ~X min (over/under by Y min)
```

## Site Health Score (Portfolio Mode)

For managed WordPress sites:

| Dimension | Weight | Measurement |
|-----------|--------|-------------|
| Uptime | 20% | HTTP status, response time |
| Content quality | 25% | Word count, internal links, freshness |
| SEO health | 20% | Meta tags, schema, Core Web Vitals |
| Conversion path | 20% | Lead capture, email automation, CTAs |
| Technical | 15% | Plugin health, PHP errors, cache status |

## Output Contract
**Artifact**: Quality score report saved to `ops/reports/quality-{type}-{YYYY-MM-DD}.md`
**Evidence**: Score breakdown by dimension, comparison to previous scores
**Decision**: Priority-ranked improvement list
**Next**: Schedule improvements for flagged items

## Self-Critique Scorecard (/25)
After every operation, score yourself:
1. **Functionality** (1-5): Does it work perfectly and meet all requirements?
2. **Quality** (1-5): Is it enterprise-grade and production-ready?
3. **Verification** (1-5): Was it verified via multiple methods (API + live + visual)?
4. **Speed** (1-5): Was execution optimal with parallel operations where possible?
5. **Learning** (1-5): Were new patterns documented and memory updated?

**Target: 22+/25 before claiming completion**

### Quality Checklist
- [ ] Pre-flight checks completed (credentials, target exists, rollback plan)
- [ ] Operation verified via API response + live page check
- [ ] Anti-patterns checked (no common mistakes)
- [ ] Scorecard completed and logged to memory/YYYY-MM-DD.md
- [ ] Skill references updated if new patterns discovered

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
