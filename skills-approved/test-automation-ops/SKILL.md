---
name: test-automation-ops
description: Use when testing website functionality, verifying deployments, running regression tests, validating API responses, checking link integrity, or automating quality assurance.
---

# Test Automation Ops

## Purpose
Run automated tests and QA checks across websites, APIs, and content — producing clear pass/fail reports with evidence.

## Use this when
- Testing a site after deployment or changes
- Running regression checks on critical paths
- Validating API responses and status codes
- Checking for broken links across a site
- Verifying content integrity (meta tags, headings, images)
- Pre-launch QA passes

## Do NOT use this for
- Tasks that belong to a more specific skill (check skill-router)
- General research (use web_search directly)

## Do this

### 1. Choose test category
| Category | Use when | Script |
|----------|----------|--------|
| Smoke | Quick health check after deploy | `test-api.py` |
| Regression | Verify nothing broke | `test-links.py` + manual |
| Integration | Test full user flows | `test-api.py` + curl |
| Content | Check links, meta, images | `test-links.py` |

### 2. Define the test plan
Before running, document:
- **Target**: URL(s) or API endpoint(s)
- **Checks**: What should be true (status, content, links)
- **Threshold**: What counts as failure (≥1 broken link? any 5xx?)

### 3. Run smoke / API tests
```bash
python3 scripts/test-api.py "https://api.example.com/health" "https://example.com" --expect 200
```

### 4. Run link checks
```bash
python3 scripts/test-links.py "https://example.com" --max-pages 20
```

### 5. Run content checks (manual pattern)
Check these for each key page:
- `<title>` present and unique
- `<meta name="description">` present
- All `<img>` have `alt` attributes
- No console errors (use `curl -s | head` or browser)

### 6. Compile report
Summarize results as:
```
Test Report — [date]
====================
Target: [URL]
Category: [smoke|regression|integration|content]

✅ [check that passed]
❌ [check that failed] — evidence: [snippet]
⚠️  [warning]

Summary: X passed, Y failed, Z warnings
```

## Resources
- `scripts/test-links.py` — Crawl and check links on a site
- `scripts/test-api.py` — Validate API endpoints with expected status

## Checks / common mistakes
- Testing staging but reporting as production
- Not specifying `--max-pages` — crawlers can go deep
- Forgetting to test both `www` and non-`www` variants
- Treating 301/302 as failures (redirects are fine — check 404s)
- Not running tests after changes — always verify

## Output contract
Pass/fail report with: target URL, checks performed, results with evidence, summary count.

## Output Contract
**Artifact**: Skill-specific deliverable (report, fix, config, or document)
**Evidence**: Proof that the work was completed correctly
**Decision**: What was decided or recommended
**Next**: Follow-up action or monitoring period

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
