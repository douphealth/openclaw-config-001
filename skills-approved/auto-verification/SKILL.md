---
name: auto-verification
description: Enterprise automated verification and QA testing. Use when verifying fixes, deployments, form submissions, checkout flows, email delivery, page renders, or any process needing proof of completion. Triggers on verification requests, QA checks, fix verification, deployment validation, batch operation validation, or "prove it works."
---

# Auto Verification — Enterprise QA & Proof of Completion

## Purpose
Prove that work was completed correctly with automated verification, not assumptions. Default to evidence over promises.

## When to Use
- Verifying form submissions, checkouts, or conversion paths
- Confirming email delivery and automation triggers
- Validating page renders and CSS/JS after deployment
- Testing API endpoints and data flows
- QA checks on batch operations (100+ posts updated correctly)

**Do NOT use for:** Designing features (→ `wordpress-growth-ops`), debugging (→ `email-automation-debugging`), launch readiness (→ `launch-readiness-audit`).

## Verification Framework

### Level 1: Functional Proof
- HTTP status check (200 OK, 302 redirect — not 4xx/5xx)
- Page content renders (no broken HTML, no blank pages)
- CSS classes present in output (not stripped by wpautop)
- Images and assets load correctly
- No JavaScript console errors

### Level 2: Data Proof
- Data written to database correctly (check via API)
- API returns expected response structure
- Form data captured in CRM or database
- Email sent and received (check delivery headers)
- Contact created with correct tags/lists

### Level 3: End-to-End Proof
- Complete a real user action (form submit, checkout, signup)
- Verify trigger → capture → delivery → notification chain
- Check timing (within expected SLA)
- Verify all expected follow-up actions (emails, tags, sequences)

### Level 4: Cross-Platform Proof
- Desktop and mobile rendering match
- Cross-browser check (Chrome, Safari, Firefox)
- Ad platform receives conversion data
- Analytics fires correct events with correct parameters

## Verification Templates

### Page Deployment Verification
```
1. Fetch live URL → HTTP status = 200 ✅
2. Check CSS classes render (not stripped by autop) ✅
3. Verify images load (accessible, not 404) ✅
4. Mobile viewport meta tag present ✅
5. No console errors on load ✅
```

### Form/Conversion Path Verification
```
1. Submit form with test data ✅
2. Check HTTP response (200/302, not error) ✅
3. Verify data in backend/CRM/WordPress ✅
4. Check confirmation page or thank-you redirect ✅
5. Verify email/automation trigger fired ✅
6. Check email content and delivery status ✅
```

### Batch Update Verification
```
1. Check count of updated posts (expected vs actual) ✅
2. Spot-check 5-10 random posts for correct content ✅
3. Verify no data loss (content length similar to before) ✅
4. Check for autop artifacts (removed, not added) ✅
```

## Evidence Quality Hierarchy
| Level | Evidence | Reliability |
|-------|----------|-------------|
| **Strong** | Live URL screenshot, API response, database record | ✅ Definitive |
| **Medium** | HTTP status, response time, content length check | ✅ Good |
| **Weak** | "It should work", "I submitted it" | ❌ Unreliable |

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
**Artifact**: Verification report with pass/fail per checkpoint
**Evidence**: Screenshots, HTTP responses, API data, or database records
**Decision**: Verified working / needs fix / partial pass
**Next**: Fix failed checkpoints, or close verification

## Anti-Patterns
- ❌ "I submitted it" without checking backend delivery
- ❌ Checking admin dashboard without front-end verification
- ❌ Assuming static HTML = functional page
- ❌ Not testing the complete user journey
- ❌ No evidence (just claiming "it works")
- ❌ Verifying once and never rechecking after changes

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
