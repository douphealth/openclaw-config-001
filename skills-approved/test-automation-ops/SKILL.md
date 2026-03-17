---
name: test-automation-ops
description: Use when testing website functionality, verifying deployments, running regression tests, validating API responses, checking link integrity, or automating QA with pass/fail evidence.
---

# Test Automation Ops

## Purpose
Run automated and semi-automated QA checks across websites, APIs, and critical paths, producing explicit pass/fail reports with evidence.

## Use this when
- testing a site after deployment or content/system changes
- running regression checks on critical paths
- validating API responses, health endpoints, and expected status codes
- checking for broken links or obvious content integrity issues
- running pre-launch or post-fix QA
- proving that a claimed change did or did not work

## Do NOT use this for
- broad monitoring/alerting programs (→ `monitoring-ops`)
- pure routing or skill-selection questions (→ `skill-router`)
- verification where `auto-verification` is the primary wrapper and testing is only one sub-step

## Test categories
| Category | Use when | Typical method |
|---|---|---|
| Smoke | Quick health check after deploy/change | health/status and key page checks |
| Regression | Verify nothing important broke | repeatable multi-page/API checks |
| Integration | Test a real end-to-end flow | API + browser or API + state validation |
| Content | Check links, meta, images, rendering basics | crawl + page checks |

## Do this
1. Define the target, environment, and failure threshold.
2. Choose the smallest test set that can prove the outcome.
3. Run smoke checks first, then deeper checks only if needed.
4. Record failures with exact evidence, not vague summaries.
5. Report pass/fail/warnings clearly.
6. If the task was proving a fix, hand off to `auto-verification` or include equivalent proof structure.

## Test plan minimum
Before running, document:
- **target** — URL(s), endpoint(s), or flow
- **environment** — production, staging, preview, etc.
- **checks** — what should be true
- **failure threshold** — what counts as failure

## Example methods
### API / smoke
```bash
python3 scripts/test-api.py "https://api.example.com/health" "https://example.com" --expect 200
```

### Link checks
```bash
python3 scripts/test-links.py "https://example.com" --max-pages 20
```

### Content checks
Check these for key pages:
- `<title>` present and sensible
- `<meta name="description">` present
- important images render and have `alt` attributes where appropriate
- expected headings/content appear
- no important console/runtime issue when browser access is needed

## Resources
- `scripts/test-links.py` — crawl and check links on a site
- `scripts/test-api.py` — validate API endpoints with expected status
- browser and fetch tools when rendered proof matters

## Checks and common mistakes
- testing staging but reporting as production
- not specifying crawl limits
- treating redirects as failures without context
- reporting a passing status code while the user-visible page is broken
- not re-running tests after changes
- vague summaries with no evidence snippet

## Output contract
**Artifact:** pass/fail QA report
**Evidence:** exact targets tested, checks performed, and failure/pass evidence
**Decision:** pass, fail, or partial with specific blocker
**Next:** fix, monitor, or deeper test scope if needed
