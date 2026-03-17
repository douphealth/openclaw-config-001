---
name: tracking-measurement
description: Enterprise conversion and behavior measurement auditing and fixing. Use when auditing, planning, or fixing measurement across GA4, GTM, ad platforms, pixels, conversion actions, event taxonomies, consent-aware tagging, or attribution flows. Triggers on conversion tracking audits, measurement plans, tracking discrepancies, event design, tag debugging, enhanced conversions, CAPI, or "is this tracked correctly?"
---

# Tracking & Measurement — Enterprise Instrumentation

## Purpose
Make conversion and behavior tracking trustworthy enough to optimize from. If data lies, optimization misleads.

## When to Use
- Auditing conversion tracking (GA4, GTM, ad platforms, pixels)
- Designing event taxonomies or measurement plans
- Debugging tag fires, discrepancies, or missing conversions
- Setting up enhanced conversions, CAPI, or consent-aware tagging
- Verifying "is this tracked correctly?"

**Do NOT use for:** Reporting on trusted data (→ `analytics-reporting`), paid media strategy (→ `paid-media-audit`).

## Measurement Framework

### Phase 1: Map the Landscape
1. Identify business-critical events: purchases, leads, activations, sign-ups
2. Map each event: source (page) → transformation (GTM/data layer) → destination (GA4, ad platforms, CRM)
3. List all platforms: GA4, GTM, Meta Pixel, Google Ads, LinkedIn Insight Tag, CRM, CDP
4. Document current event names, parameters, and triggers

### Phase 2: Event Taxonomy Design
5. Follow this naming pattern: `category_action_detail` (e.g., `form_submit_lead_gen`, `purchase_complete`)
6. Always include: `event_id` (dedup), `value`, `currency`, `source`, `medium`
7. User properties: `user_type`, `account_tier`, `segment` where applicable
8. Map every parameter to a GA4 custom dimension before it's needed

**Taxonomy rules:**
- One event per meaningful user action
- Standard events first, custom only when standard doesn't fit
- No spaces or capital letters in event names
- Document every event in a shared taxonomy sheet

### Phase 3: Implementation Checklist

**Container setup:**
- [ ] GTM container installed on all pages
- [ ] GA4 configuration tag fires on all pages
- [ ] Cross-domain tracking configured if multiple domains
- [ ] Debug mode verified in staging

**Event tracking:**
- [ ] All business-critical events have GTM triggers
- [ ] Events fire on correct trigger type (click, form submit, timer, custom)
- [ ] Parameters populated with actual values, not defaults
- [ ] `event_id` is unique per event instance

**Conversion setup:**
- [ ] Key events marked as conversions in GA4
- [ ] Conversion values populated (static or dynamic)
- [ ] Google Ads conversion actions import from GA4
- [ ] Meta Conversions API configured alongside pixel

**Data quality:**
- [ ] No duplicate events firing
- [ ] Internal/team traffic excluded
- [ ] Referral exclusions for payment processors and own domains
- [ ] Consent mode configured and respected

### Phase 4: Validate
11. Test conversion on each critical path
12. Check GA4 Realtime for event arrival with correct parameters
13. Verify event appears in correct ad platform
14. Check for duplication: one action = one event_id across platforms
15. Quantify discrepancies: calculate gap if platform numbers disagree

### Phase 5: Report & Prioritize
16. Report: tracked correctly, incorrectly, and not at all
17. Prioritize by business impact: purchases/leads > activations > vanity events
18. Define ongoing validation plan

## Performance Optimizations

### Speed Multipliers
- Parallel data fetching from multiple sources
- Pre-compute common metrics for the session
- Template-based reports and dashboards
- Batch API calls for platform operations
- Automated threshold alerts for significant changes

### Self-Critique Scorecard (/25)
1. **Functionality** (1-5): Does it work perfectly?
2. **Quality** (1-5): Enterprise-grade analysis?
3. **Verification** (1-5): Data validated from multiple sources?
4. **Speed** (1-5): Optimal execution?
5. **Learning** (1-5): Patterns documented?

**Target: 22+/25**

### Auto-Check
- [ ] Data quality validated before conclusions
- [ ] Comparison periods consistent
- [ ] Confidence levels stated
- [ ] Actionable recommendations provided
- [ ] Score logged to memory

## Output Contract
**Artifact**: Measurement plan, event taxonomy, or tracking fix documentation
**Evidence**: GA4 Realtime verification, cross-platform consistency check
**Decision**: Tracking validated and working
**Next**: Monitor for 1-2 weeks, recheck after major changes

## Anti-Patterns
- ❌ Tags firing ≠ accurate reporting (verify end-to-end)
- ❌ Optimizing against noisy secondary conversion actions
- ❌ Ignoring event_id, value, currency, source metadata
- ❌ Skipping consent/privacy checks (causes silent data loss)
- ❌ Different event naming conventions across platforms

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
