---
name: launch-readiness-audit
description: Enterprise launch readiness assessment for sites, funnels, products, landing pages, checkouts, lead flows, and delivery systems. Use when deciding whether something is truly ready to launch, performing go-live reviews, preflight audits, readiness assessments, or making go/no-go decisions with evidence.
---

# Launch Readiness Audit — Enterprise Go/No-Go System

## Purpose
Assess whether a launch is truly ready with evidence, not assumptions. Return a clear go/no-go decision with quantified risk.

## When to Use
- "Is this site/page/funnel ready to launch?"
- Go-live reviews and preflight audits
- Readiness assessments for new features
- Launch proof requirements
- Multi-path readiness evaluation

**Do NOT use for:** Single checkout path proof (→ `money-path-verification`), SEO auditing (→ `seo-audit-playbook`), general site improvement (→ `wordpress-growth-ops`).

## Critical Path Framework

Every launch has a **critical path** — the minimum chain that must work for the launch to succeed:

```
Visitor → Value Prop → Action → Capture → Delivery → Follow-up → Monetization
```

If ANY link in this chain is broken, the launch is **BLOCKED**.

## Audit Checklist

### 1. Offer & Value Proposition (20%)
- [ ] Primary value proposition is clear in <5 seconds
- [ ] Target audience is explicitly defined
- [ ] Price/offer is final and tested
- [ ] Competitive differentiation is clear
- [ ] Social proof exists (testimonials, reviews, credentials)

### 2. Technical Functionality (25%)
- [ ] All pages load <3 seconds (Core Web Vitals pass)
- [ ] Mobile responsive on all breakpoints
- [ ] Forms submit successfully (tested with real data)
- [ ] Email capture triggers fire correctly
- [ ] Payment processing works end-to-end (if applicable)
- [ ] SSL certificate valid, no mixed content
- [ ] 404 pages redirect properly
- [ ] Favicon, meta tags, Open Graph images set

### 3. Conversion Path (20%)
- [ ] CTA buttons visible without scrolling on mobile
- [ ] Form validation works (error messages clear)
- [ ] Thank-you page / confirmation displayed
- [ ] Redirect after conversion is correct
- [ ] Abandon recovery in place (if applicable)
- [ ] Multiple conversion points available

### 4. Tracking & Analytics (15%)
- [ ] Google Analytics / tracking installed and firing
- [ ] Conversion events configured
- [ ] UTM parameters tested
- [ ] Goal tracking verified in GA
- [ ] Pixel fires confirmed (Meta, Google Ads if applicable)

### 5. Delivery & Fulfillment (10%)
- [ ] Lead magnet delivers within 60 seconds
- [ ] Email sequence starts on schedule
- [ ] Product/service delivery path works
- [ ] Customer support contact available
- [ ] Refund/cancellation process defined

### 6. Legal & Compliance (10%)
- [ ] Privacy policy exists and is current
- [ ] Terms of service (if selling)
- [ ] Cookie consent (if EU audience)
- [ ] Affiliate disclosure (if applicable)
- [ ] GDPR compliance (if EU data)

## Scoring

| Category | Weight | Status |
|----------|--------|--------|
| Offer & Value Prop | 20% | Pass/Partial/Fail |
| Technical | 25% | Pass/Partial/Fail |
| Conversion Path | 20% | Pass/Partial/Fail |
| Tracking | 15% | Pass/Partial/Fail |
| Delivery | 10% | Pass/Partial/Fail |
| Legal | 10% | Pass/Partial/Fail |

## Decision Matrix

| Result | Decision | Action |
|--------|----------|--------|
| All Pass, 0 Fail | 🟢 **GO** | Launch with confidence |
| ≤2 Partial, 0 Fail | 🟡 **CONDITIONAL GO** | Fix partials within 48h post-launch |
| Any Fail OR >2 Partial | 🔴 **NO-GO** | Fix blockers before launch |

## Output Template

```markdown
# Launch Readiness: [Site/Project]
Date: [date]

## Decision: 🟢 GO / 🟡 CONDITIONAL GO / 🔴 NO-GO

### Critical Path Status
✅ Value Prop → ✅ Capture → ✅ Delivery → ✅ Follow-up

### Category Scores
| Category | Status | Notes |
|----------|--------|-------|
| Offer | ✅ Pass | |
| Technical | 🟡 Partial | Mobile nav slow |
| Conversion | ✅ Pass | |
| Tracking | ✅ Pass | |
| Delivery | ✅ Pass | |
| Legal | ✅ Pass | |

### Blockers (if any)
1. [Issue] — Fix: [action] — Owner: [who]

### Open Risks
- [Risk] — Likelihood: [H/M/L] — Impact: [H/M/L]

### Next Steps
1. [Immediate action]
```

## Core Rules
- Default to NO-GO unless critical-path proof exists
- Nice design ≠ launch readiness
- Tracking and fulfillment count as launch scope
- Include remaining risk, not just current progress
- Proof > promises

## Output Contract
**Artifact**: Go/no-go checklist with evidence and scoring
**Evidence**: Pass/fail for each checkpoint with test results
**Decision**: Launch decision with confidence level
**Next**: Fix blockers or proceed with launch

## Performance Optimizations

### Speed Multipliers
- Use proven copy frameworks as starting point (don't start from blank)
- Generate 5 headline options simultaneously, pick best 2-3
- Pull customer language from existing reviews/testimonials
- Template-based copy structures for each page type
- Parallel research (audience, competitors, proof points)

### Self-Critique Scorecard (/25)
1. **Clarity** (1-5): Could a stranger understand in 10 seconds?
2. **Specificity** (1-5): Numbers/examples over vague claims?
3. **Persuasion** (1-5): Does it move toward the CTA?
4. **Proof** (1-5): Social proof near CTAs? Objections addressed?
5. **Polish** (1-5): No filler or corporate sludge?

**Target: 22+/25**

### Auto-Check
- [ ] No generic claims without specifics
- [ ] No feature dumps without outcomes
- [ ] CTA is obvious and action-oriented
- [ ] Proof elements placed near conversions
- [ ] Score logged to memory

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
