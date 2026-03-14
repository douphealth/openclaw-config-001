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
