---
name: money-path-verification
description: Use when verifying that a revenue path, lead path, checkout, signup flow, booking flow, email automation, or product delivery flow actually works end to end. Triggers on requests to verify a launch, prove checkout, validate a funnel, test lead capture, confirm order creation, confirm delivery, or ensure a site's primary money path is truly working.
---

# Money Path Verification

## Purpose
Prove that a site's critical conversion path works in reality, not just in theory.

## Use this when
Final checks, launch proof, regression verification, or when trust is low and evidence matters. Not for ongoing analytics (use `analytics-reporting`) or designing the funnel (use `service-funnel-architecture`).

## Decision Tree

```
Verification needed?
├── Launch prep? → Full end-to-end verification of all paths
├── Post-change regression? → Verify the changed path specifically
├── "Something feels broken"? → Start with most critical path, work down
├── Periodic health check? → Rotate through paths, verify one per check
└── Before paid media spend? → Verify landing page → conversion path
```

## Verification Standard

**Do not call a path complete until you have evidence for the relevant end-to-end steps.**

Default to "not yet proven" when evidence is partial, stale, or indirect.

## Verification Scope by Path Type

### Product / Commerce Path
Test and prove each step:
- [ ] Add to cart works (product appears in cart)
- [ ] Cart updates correctly (quantity, variants, discounts)
- [ ] Checkout page loads with correct items and pricing
- [ ] Payment options appear and are selectable
- [ ] Test transaction processes (use sandbox/test mode)
- [ ] Order confirmation page/message appears
- [ ] Order record created in backend/admin
- [ ] Delivery/access path works (download link, account access, email)
- [ ] Post-purchase email fires (receipt, next steps)

### Lead Capture Path
Test and prove each step:
- [ ] CTA path opens correctly (button → form/modal/page)
- [ ] Form or bot submits successfully (no console errors)
- [ ] Success message or redirect occurs
- [ ] Contact record created in CRM/provider
- [ ] Correct tags/list/segment applied
- [ ] Automation or first follow-up triggers
- [ ] Welcome/delivery email sent and received
- [ ] Thank-you page displays with next-step CTA

### Booking / Service Path
Test and prove each step:
- [ ] Primary CTA path works (button → booking/inquiry form)
- [ ] Booking form or calendar loads correctly
- [ ] Time slots display accurately (timezone-correct)
- [ ] Submission creates record (in CRM, calendar, or email)
- [ ] Confirmation email or calendar invite sent
- [ ] Follow-up automation triggers
- [ ] Internal notification fires (Slack, email, CRM alert)

### Affiliate / Content Path
Test and prove each step:
- [ ] Affiliate links load correct destination
- [ ] Tracking parameters preserved (UTM, sub-ID)
- [ ] Link opens in correct target (new tab, same window)
- [ ] Mobile experience works (deep links, app opens)
- [ ] Disclosure visible and compliant

## Evidence Quality Hierarchy

### Strong Evidence (required for "verified" status)
- Success response payloads from API calls
- Created records visible via API or admin endpoints
- Live browser evidence showing post-submit state
- Fresh end-to-end proof using a new test input
- Screenshot or video of the complete path
- Email received in test inbox with correct content

### Medium Evidence (acceptable with caveats)
- Console showing successful network requests (2xx status)
- Admin dashboard showing recent entries
- Third-party tool confirmation (payment processor, CRM)
- Automated test script passing

### Weak Evidence (NOT sufficient alone)
- Button looks clickable
- Page loads without actually submitting
- Assumptions from static markup alone
- Old order/lead artifacts reused as proof
- Form HTML exists (doesn't mean it submits correctly)

## End-to-End Test Protocol

```
1. Open site in incognito/private browser (fresh session, no cache)
2. Navigate to the entry point of the money path
3. Complete each step, capturing evidence:
   a. Screenshot or note at each major step
   b. Record timestamps
   c. Note any delays, errors, or unexpected behavior
4. Verify backend state:
   a. Check admin/CRM for created record
   b. Verify email/notification delivery
   c. Confirm data matches what was submitted
5. Document results in verification template
```

### Test Data Best Practices
- Use identifiable test emails: `verify+timestamp@yourdomain.com`
- Use test payment methods (Stripe test card: 4242 4242 4242 4242)
- Clean up test data after verification
- Never test with real customer data or real payment methods

## Verification Checklist Template

```markdown
## Money Path Verification: [Site/Path Name]
**Date**: YYYY-MM-DD
**Path type**: [Commerce / Lead / Booking / Affiliate]
**Tester**: [who verified]

### Path Under Test
Entry point: [URL or trigger]
Expected outcome: [what should happen]

### Step-by-Step Results
| Step | Status | Evidence | Notes |
|---|---|---|---|
| Step 1: [name] | ✅/⚠️/❌ | [screenshot/response] | [notes] |
| Step 2: [name] | ✅/⚠️/❌ | [screenshot/response] | [notes] |
| Step N: [name] | ✅/⚠️/❌ | [screenshot/response] | [notes] |

### Backend Verification
| Check | Status | Evidence |
|---|---|---|
| Record created | ✅/❌ | [where found] |
| Data correct | ✅/❌ | [details] |
| Automation fired | ✅/❌ | [proof] |
| Notification sent | ✅/❌ | [received?] |

### Overall Status: ✅ VERIFIED / ⚠️ PARTIAL / ❌ BROKEN
### Issues Found: [list]
### Unverified Steps: [list with reason]
### Recommendations: [fixes needed before launch]
```

## Regression Verification

After changes to a site, verify the specific path that was affected:

1. **Identify what changed** — which page, form, plugin, code
2. **Map what could break downstream** — every connected path
3. **Test the changed element first** — does it still function?
4. **Test the full money path** — end-to-end, not just the changed part
5. **Compare to pre-change baseline** — if you have before evidence

## Common Failure Patterns

| Pattern | Symptom | Check |
|---|---|---|
| **AJAX form without handler** | Form submits, nothing happens | Network tab for API call, response code |
| **Plugin conflict** | Works on one page, breaks on another | Disable recent plugins, retest |
| **Cache serving stale code** | Old version loads | Hard refresh, CDN purge, incognito test |
| **Payment mode mismatch** | Test mode in prod or vice versa | Check payment gateway settings |
| **Missing environment variables** | API calls fail silently | Check server config, .env file |
| **Mobile-specific break** | Works desktop, fails mobile | Test on actual mobile device or emulator |
| **Third-party script blocking** | Checkout/payment fails | Ad blocker test, CSP check |

## Output Contract
**Artifact**: Verification report with pass/fail per step and evidence
**Evidence**: Screenshots, API responses, backend records, email receipts
**Decision**: Path verified / partially verified / broken — with specifics
**Next**: Fix identified issues, re-verify, or proceed to launch

## Checks and Common Mistakes
- Do not stop at UI polish when the underlying path is unproven.
- Do not use the wrong submission mechanism if the real system uses AJAX or JS-rendered behavior.
- Do not mark a path done from front-end appearance alone.
- Do not hide uncertainty; state it plainly.
- Do not assume because it worked last week it works today.
- Do not test only on desktop — mobile traffic is often 50%+ of real users.
- Do not skip cleanup of test data (test orders, test contacts).

## Resources
Read when needed:
- `references/evidence-standard.md`
- `references/site-special-cases.md`

Pair with `launch-readiness-audit` when the task is an overall go/no-go decision rather than proof of one path.
Pair with `email-automation-debugging` when the unresolved risk is signup-to-email execution.

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
