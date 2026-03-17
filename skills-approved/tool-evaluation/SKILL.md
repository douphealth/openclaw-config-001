---
name: tool-evaluation
description: Enterprise tool evaluation and vendor comparison. Use when comparing software, vendors, platforms, or internal tool choices for adoption, replacement, or standardization. Triggers on evaluating tools, comparing platforms, choosing between vendors, assessing ROI, assessing security/integration fit, or recommending the best tool for a business workflow.
---

# Tool Evaluation — Enterprise Vendor Assessment

## Purpose
Choose tools with less bias and better total-cost judgment. Deliver a defensible recommendation backed by weighted scoring, not a feature checklist.

## When to Use
- Comparing 2+ software vendors or platforms
- Assessing ROI, security fit, or integration compatibility
- Choosing tools for a specific business workflow
- Standardizing tooling across teams or organizations

**Do NOT use for:** Implementing an already-chosen tool (→ go straight to implementation), SEO-specific analysis (→ `seo-audit-playbook`).

## Evaluation Framework

### Phase 1: Define the Job
1. Write job-to-be-done in one sentence: "We need [tool] to [outcome] for [audience] given [constraints]."
2. List non-negotiable constraints (integrations, compliance, budget, deployment model)
3. Identify evaluation team and decision-maker

### Phase 2: Weighted Scoring

Score each option (1-5 scale):

| Dimension | Default Weight | What it measures |
|-----------|---------------|------------------|
| Functionality fit | 25% | Does it do the job well? |
| Integration fit | 20% | Connects to existing stack |
| Usability | 15% | Team can adopt without heavy training |
| Security & risk | 15% | Data handling, compliance, stability |
| Total cost | 15% | Price + training + migration + maintenance |
| Vendor quality | 10% | Support, roadmap, community |

**Scoring guide:**
- 5 = Exceeds requirement, category leader
- 4 = Meets requirement with room to spare
- 3 = Meets requirement adequately
- 2 = Partially meets, gaps exist
- 1 = Fails or not available

### Phase 3: Decision Matrix

Build weighted comparison:

| Option | Functionality (25%) | Integration (20%) | Usability (15%) | Security (15%) | Cost (15%) | Vendor (10%) | Total |
|--------|-------------------|------------------|----------------|---------------|-----------|-------------|-------|
| Tool A | 4 → 1.00 | 3 → 0.60 | 4 → 0.60 | 5 → 0.75 | 3 → 0.45 | 4 → 0.40 | **3.80** |
| Tool B | 5 → 1.25 | 2 → 0.40 | 3 → 0.45 | 4 → 0.60 | 5 → 0.75 | 3 → 0.30 | **3.75** |

4. Fail any must-have = eliminated regardless of score
5. Distinguish "best in class" from "best for this team right now"

### Phase 4: Recommend
6. State tradeoffs explicitly: what you gain and what you give up
7. Note adoption risks and mitigations
8. Provide 90-day adoption plan


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
**Artifact**: Tool evaluation report with weighted matrix and recommendation
**Evidence**: Scoring matrix, must-have verification, TCO analysis
**Decision**: Recommended tool with stated tradeoffs
**Next**: 90-day adoption plan or further testing

## Anti-Patterns
- ❌ Recommending based on popularity over fit
- ❌ Ignoring switching cost and training overhead
- ❌ Treating feature lists as evaluation
- ❌ Skipping hands-on testing (vendor demos are theater)
- ❌ Not documenting TCO beyond license price

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
