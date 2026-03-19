---
name: auto-verification
description: Enterprise automated verification and QA testing. Use when proving fixes, deployments, WordPress renders, form submissions, checkout flows, email delivery, or batch operations actually work. Triggers on verification requests, QA checks, deployment validation, batch proof, or “prove it works.”
---

# Auto Verification

## Purpose
Produce proof, not vibes. This skill verifies that a change really works in the live environment, with special discipline for WordPress sites where editor state, cache state, and rendered state can disagree.

## Shared Doctrine References
- `skills/shared/wordpress/verification-ladder.md`
- `skills/shared/wordpress/cache-plugin-gotchas-matrix.md`
- `skills/shared/wordpress/rollback-recovery-protocol.md`


## Enterprise Protocols (MANDATORY)

Before executing, read `skills/shared/enterprise-protocol.md` and follow:
- Pre-flight health check (site accessible, creds valid, state captured)
- Mandatory backup before any modification
- Retry with exponential backoff (max 3 attempts per API call)
- Progress reporting every 10 operations
- Verification after each modification
- Health checks every 50 items in long operations
- Rollback plan identified before starting

## Superpower Layer

For complex or high-risk work, also follow:
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`

Default execution mode:
1. clarify/spec first if ambiguous
2. write a short plan before large execution
3. dispatch parallel workers for independent subtasks
4. review output for spec compliance and quality
5. verify in reality before claiming complete

## When to Use
- Verifying WordPress page, post, template, schema, or plugin-output changes
- Proving a form, lead flow, checkout path, redirect, or booking path works end to end
- Confirming deployment results after code, CMS, or settings changes
- Validating batch updates across many WordPress posts/pages/items
- Checking downstream effects such as CRM capture, email delivery, analytics events, or schema eligibility


## Do NOT Use For
- Building or editing the WordPress asset itself (`wp-rest-api-mastery` or `wordpress-growth-ops`)
- Broad launch go/no-go decisions (`launch-readiness-audit`)
- Deep root-cause debugging when the failure source is still unknown (`wp-error-recovery`, `email-automation-debugging`, or the relevant debugger)
- Analytics interpretation without a verification objective (`analytics-reporting`)

## Inputs Required
1. Target URL, page/post ID, endpoint, or money path to verify
2. Environment and risk level: staging vs production
3. Access model: public URL only, REST auth, WP-CLI, admin, CRM, inbox, payment sandbox, etc.
4. Expected outcome and pass/fail criteria
5. Rollback or escalation owner if verification fails

## Triage Protocol
1. Identify verification type: render, behavior, downstream, or batch
2. Confirm environment and whether caches/CDNs may delay visible truth
3. Read current state before testing so the expected result is concrete
4. Choose the minimum decisive evidence set
5. For production paths, use safe test data and note cleanup requirements

## Core Framework
### 1. Define the proof standard
- What exactly must be true?
- What would count as a fail or partial pass?
- Is editor/API success enough, or must live rendering and downstream delivery also be proven?

### 2. Run the verification ladder
1. **Write proof** — REST/CLI/admin shows the intended change exists
2. **Render proof** — live HTML/source reflects it after cache-aware checking
3. **Behavior proof** — the interaction works for a real user
4. **Downstream proof** — CRM, email, analytics, payment, schema validation, or notifications also confirm success

### 3. Apply WordPress-specific checks
- Compare REST/editor state to rendered front-end output
- Watch for Gutenberg block corruption, shortcode stripping, page-builder meta dependencies, and plugin/theme overrides
- Check if cache, minification, or CDN layers are masking stale output
- Confirm schema or scripts are not duplicated, stripped, or deferred into breakage

### 4. Use the right verification pattern
#### A. WordPress render verification
- HTTP status is correct
- live HTML contains the expected block/class/text/script
- no obvious broken layout or blank-state rendering
- assets load without 404s
- mobile-critical sections remain usable

#### B. Funnel / form / booking verification
- submit with controlled test data
- verify response + thank-you/redirect
- confirm WordPress/plugin/backend record creation
- confirm CRM/list/tag/automation handoff
- confirm email delivery or booking notification

#### C. Batch verification
- count expected targets before and after
- verify success totals
- spot-check representative samples, including edge cases
- escalate to wider audit if any sample fails

#### D. Schema / SEO verification
- confirm only one intended schema layer renders
- validate JSON-LD syntax and rich-result eligibility
- compare source HTML to plugin/admin configuration

## Performance Optimizations
### Speed Multipliers
- Apply `skills/api-efficiency-protocol.md` before verification waves
- Reuse session snapshots instead of re-fetching the same WordPress objects
- Verify the smallest decisive evidence set first, then expand only if ambiguous
- Batch by site and by verification type
- For large batches, sample intelligently before brute-force checking everything

## Output Contract
**Artifact**: Verification report with pass/fail by checkpoint
**Evidence**: REST/CLI proof, live HTML/render proof, and downstream proof where relevant
**Decision**: Pass / partial pass / fail with exact blocker
**Next**: Fix, re-test, monitor, or escalate

## Anti-Patterns
- ❌ Trusting editor/admin state without checking rendered output
- ❌ Trusting a rendered page without checking downstream capture or delivery
- ❌ Testing production forms with junk data that pollutes CRM or automations
- ❌ Ignoring cache layers when live output appears stale
- ❌ Sampling only easy pages after a batch write
- ❌ Declaring success from one screenshot when the path includes redirects, email, or CRM steps

## References
- `skills/references/wp-live-ops-verification.md`
- `skills/shared/wordpress/verification-ladder.md`
- `scripts/verify-url.py`

## Self-Critique Scorecard (/25)
1. **Triage** (1-5): Was the real verification target understood before testing?
2. **Execution** (1-5): Was the verification clean, safe, and efficient?
3. **Verification** (1-5): Did the evidence prove reality, not assumptions?
4. **Rollback** (1-5): If failure was found, is escalation or recovery clear?
5. **Learning** (1-5): Were reusable verification traps or fixes captured?

**Target: 22+/25**
