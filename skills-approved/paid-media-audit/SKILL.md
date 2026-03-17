---
name: paid-media-audit
description: Use when auditing Google Ads, Meta Ads, Microsoft Ads, or paid acquisition programs for wasted spend, tracking problems, structural issues, bidding mistakes, creative gaps, audience problems, or scale readiness. Triggers on requests for ad account audits, CAC problems, wasted spend reviews, campaign diagnostics, account takeovers, or "why is paid underperforming?".
---

# Paid Media Audit

## Do NOT Use This For
- setting up tracking (use `tracking-measurement`)
- general analytics reporting (use `analytics-reporting`)

## Purpose
Find the highest-impact paid media problems before more budget gets wasted.

## Use this when
Diagnosing or auditing paid acquisition performance. If tracking is unreliable, pair with `tracking-measurement` first. If the landing page, offer, or checkout path is the suspected bottleneck, pair with `revenue-site-execution`, `money-path-verification`, or `offer-positioning`.

## Decision Tree

```
Paid media underperforming?
├── Tracking broken? → route to tracking-measurement FIRST
├── Low CTR? → Creative problem → Creative audit section
├── High CPC? → Audience/bidding problem → Bid Strategy section
├── Low conversion rate? → Landing page mismatch → LP review
├── High CAC? → Full-funnel analysis → CAC/LTV section
└── Can't scale? → Audience saturation → Overlap detection
```

## Audit Framework (6 Layers)

### Layer 1: Tracking & Conversion Quality
Before anything else, verify:
- [ ] Conversion actions are real business events (not pageviews)
- [ ] Pixel/CAPI is firing and deduplicating correctly
- [ ] Conversion counts match backend data (±10%)
- [ ] Attribution window matches sales cycle length
- [ ] No duplicate or ghost conversions inflating numbers

**If tracking is broken, stop here.** No audit finding is trustworthy without measurement quality.

### Layer 2: Bid Strategy Analysis

| Strategy | Best For | Risk | Audit Check |
|---|---|---|---|
| Manual CPC | Testing phase, low volume | Under-optimization | Are bids stale (>30 days unchanged)? |
| Target CPA | Stable conversion volume | Bid ceiling too low → no delivery | Is CPA target within 20% of actual? |
| Target ROAS | Ecommerce with value data | Under-delivery if ROAS too aggressive | Is ROAS target realistic for current funnel? |
| Max Conversions | Scaling with budget | CPC inflation, quality drop | Is CPC increasing week-over-week? |
| Max Clicks | Awareness, traffic building | Low-quality clicks | What's bounce rate on paid traffic? |

**Audit questions**:
- Has the strategy been in learning phase for >7 days? (Google needs ~50 conversions/week)
- Are bid adjustments (device, location, time) being used or defaulted?
- Is there budget competition between campaigns targeting the same audience?

### Layer 3: Creative Performance Scoring

Score each creative on a 1-5 scale:

| Criterion | 1 (Weak) | 5 (Strong) |
|---|---|---|
| Relevance | Generic stock photo | Audience-specific visual |
| Hook strength | No pattern interrupt | Stops scroll in 1-2 seconds |
| Message clarity | Feature-dumps | One clear benefit or outcome |
| CTA clarity | "Learn more" | Specific action with value ("Get free audit") |
| Format match | Wrong aspect ratio | Native to placement (Stories, Feed, Search) |

**Creative rotation rule**: If top creative has >60% of spend with declining CTR over 2+ weeks, it's fatigued. Rotate.

**Platform-specific creative notes**:
- **Google Search**: Ad copy relevance to keyword intent matters more than cleverness. Check RSAs have strong pinning.
- **Meta Feed**: Video outperforms static for awareness; static outperforms for retargeting. Test both.
- **TikTok**: Must look native — UGC style, no polished ads. Hook in first 1.5 seconds.

### Layer 4: Audience Overlap & Saturation

**Detection signals**:
- Frequency >3 (Meta) or >5 (display) within 7 days → saturation
- CPC increasing while CTR stable → competition/auction pressure
- Impression share <50% with max budget → audience is too small or bid is too low

**Overlap check (Meta)**:
- Use Audience Overlap tool in Ads Manager
- >30% overlap between prospecting campaigns = audience duplication waste
- Fix: consolidate into one campaign with ad set segmentation, or create exclusions

### Layer 5: CAC/LTV Calculations

```
CAC = Total ad spend + sales/marketing labor / New customers acquired
LTV = Average order value × Purchase frequency × Customer lifespan
LTV:CAC Ratio = LTV / CAC
```

| LTV:CAC Ratio | Assessment | Action |
|---|---|---|
| < 1:1 | Losing money | Stop or fix fundamentals |
| 1:1 - 2:1 | Barely viable | Improve retention or reduce CAC |
| 3:1 - 5:1 | Healthy | Scale with confidence |
| > 5:1 | Under-investing | Can afford to bid more aggressively |

**Breakdown by channel** if possible — CAC varies dramatically between Google Search (intent-heavy) and Meta Prospecting (demand creation).

### Layer 6: Platform-Specific Optimization

**Google Ads**:
- Check Search Terms report for irrelevant queries eating budget (aim for <15% wasted spend)
- Verify Quality Scores (below 5/10 = ad/keyword/landing page mismatch)
- Review ad extensions — sitelinks, callouts, structured snippets add ~10-15% CTR
- Check negative keyword lists are maintained monthly

**Meta Ads**:
- Review placement breakdown — disable Audience Network if CTR is <0.5%
- Check learning phase status — campaigns need ~50 optimization events/week
- Verify pixel events match campaign objectives
- Look for creative fatigue (CTR decline over 7-14 days)

**TikTok Ads**:
- Video completion rate >30% indicates good creative fit
- Check Spark Ads vs. non-Spark — Spark typically gets better CPMs
- Audience size should be >1M for prospecting (platform needs scale)
- Review dayparting if running 24/7 — engagement varies wildly by hour

## Output Template

```markdown
## Paid Media Audit: [Account/Platform]
**Date**: YYYY-MM-DD
**Period analyzed**: [date range]

### Tracking Health: [PASS / FAIL / PARTIAL]
[Details on conversion tracking quality]

### Top 3 Findings
1. [Highest-impact issue + estimated waste/upside]
2. [Second issue + evidence]
3. [Third issue + evidence]

### Bid Strategy Assessment
[Current strategy, issues, recommendation]

### Creative Health Score: [X/25 average]
[Brief breakdown by criterion]

### Audience & Overlap Issues
[Saturation signals, overlap %, recommendations]

### CAC/LTV Snapshot
| Channel | CAC | Est. LTV | Ratio |
|---|---|---|---|
[Data or "insufficient data"]

### Action Plan (Priority Order)
1. [Highest ROI fix] — estimated impact
2. [Second fix] — estimated impact
3. [Third fix] — estimated impact

### Dependencies
[Tracking fixes needed, landing page issues, offer changes]
```

## Core Rules
- Do not judge paid performance without checking measurement quality first.
- Separate structural issues from strategy issues from creative issues.
- Flag budget waste, learning resets, and poor optimization signals explicitly.
- Diagnose using recent data, but look for trend shifts and change-history clues.
- Avoid fake precision on upside projections.

## Output Contract
**Artifact**: Ad account audit report with prioritized recommendations
**Evidence**: Waste analysis, ROAS data, audience insights, creative scoring
**Decision**: Action plan prioritized by impact with estimated upside
**Next**: Implement top-3 fixes, re-measure in 7-14 days

## Checks and Common Mistakes
- Do not give generic "test more creatives" advice without identifying the actual gap.
- Do not ignore landing page mismatch when diagnosing ad performance.
- Do not confuse lead volume with lead quality.
- Do not call an account healthy just because CTR looks fine.
- Do not audit only the last 7 days — seasonality and learning phases need 30-90 day views.

## Resources
Read when needed:
- `references/audit-priority-stack.md`
- `references/portfolio-paid-diagnosis.md`

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
