---
name: lead-magnet-delivery-ops
description: Use when setting up or improving lead magnet capture, thank-you flow, email delivery, bonus delivery, gated asset access, or post-opt-in progression. Triggers on requests to launch a lead magnet, fix delivery flow, improve opt-in fulfillment, connect signup to asset delivery, or ensure lead capture actually delivers the promised asset.
---

# Lead Magnet Delivery Ops

## Do NOT Use This For
- creating the lead magnet content (use `conversion-copywriting`)
- designing email sequences (use `lifecycle-email-sequences`)
- debugging why automation fails (use `email-automation-debugging`)

## Purpose
Make sure opt-ins do not stop at capture — they deliver the promised asset cleanly and move the lead to the next step.

## Use this when
The task spans form capture, confirmation, delivery, and first next-step logic. Not for diagnosing why automation is broken; use `email-automation-debugging` for that.

## Decision Tree

```
Lead magnet delivery issue?
├── Asset never arrives? → Check delivery method → Email vs. instant access
├── Wrong asset delivered? → File/link mapping error
├── Delay too long? → Timing optimization needed
├── Thank-you page dead-ends? → Missing next-step CTA
├── Subscriber not created? → Capture hop failure (route to email-automation-debugging)
└── Low conversion from opt-in to next step? → Funnel gap after delivery
```

## Delivery Flow Template

```
[Visitor sees offer] → [Clicks CTA] → [Fills form]
→ [Contact created] → [Delivery triggered] → [Asset delivered]
→ [Thank-you page shown] → [Next-step CTA presented]
→ [Follow-up email with asset link] → [Nurture sequence begins]
```

### Delivery Method Decision Matrix

| Method | Speed | Reliability | Best For |
|---|---|---|---|
| **Instant (redirect)** | Immediate | High | PDFs, simple assets, low-friction |
| **Email delivery** | 1-5 min | Medium | Assets requiring record, multi-part delivery |
| **Account access** | Immediate | High | Courses, gated content, membership |
| **Hybrid (redirect + email)** | Immediate + backup | Highest | Critical assets where reliability matters |

**Rule**: If the asset is the core promise (not a bonus), use hybrid. The thank-you page delivers immediately AND a backup email is sent.

## Thank-You Page Optimization

### Structure (in order)
1. **Confirmation**: "You're in! Your [asset] is [here/downloading/being sent]"
2. **Delivery**: Direct link or embedded viewer (if instant method)
3. **Social proof**: Testimonial or stat reinforcing the asset's value
4. **Next CTA**: One clear action — book a call, join community, start trial, watch video
5. **Expectation setting**: "Check your email for [bonus/access details]"

### Thank-You Page Anti-Patterns
- ❌ "Thanks for subscribing." (dead end — no asset, no next step)
- ❌ Generic homepage redirect after form submission
- ❌ Asset only in email (forces waiting + email deliverability risk)
- ❌ Multiple competing CTAs on the thank-you page
- ✅ Direct asset delivery + one clear next step

## First-Email Timing

| Scenario | Recommended Delay | Reasoning |
|---|---|---|
| Asset delivery email | 0-2 minutes | Delays cause anxiety and support tickets |
| Welcome/relationship email | 5-15 minutes | Don't compete with delivery email |
| First nurture email | 24 hours | Let the asset sink in |
| First offer email | 48-72 hours (B2C) / 5-7 days (B2B) | After they've had time to engage with asset |

**Critical**: The delivery email and the welcome email should NOT be the same email. Separate them.

## Asset Delivery Verification Checklist

Before declaring the flow operational:

### Capture Verification
- [ ] Form renders correctly on mobile and desktop
- [ ] Form submits without errors (check browser console)
- [ ] Contact record created in provider within 60 seconds
- [ ] Tags/list membership applied correctly

### Delivery Verification (Instant Method)
- [ ] Thank-you page loads after submission
- [ ] Asset download link works (test clicking it)
- [ ] File is correct version (not stale/old)
- [ ] File opens correctly on mobile devices
- [ ] CDN/hosting not blocking access

### Delivery Verification (Email Method)
- [ ] Delivery email sends within 5 minutes
- [ ] Email contains correct asset link
- [ ] Link in email works and downloads correct file
- [ ] Email doesn't land in spam/promotions (test with Gmail + Outlook)
- [ ] Email subject line clearly references the asset

### Post-Delivery Verification
- [ ] Thank-you page has next-step CTA
- [ ] Follow-up sequence triggers (if configured)
- [ ] Contact correctly segmented for nurture
- [ ] Analytics tracking fires on thank-you page view

## End-to-End Test Protocol

```
1. Open landing page in incognito/private browser
2. Fill form with test email (test+timestamp@domain.com)
3. Submit and capture what happens:
   a. What page loads after submit?
   b. Can you access the asset immediately?
   c. How long until delivery email arrives?
   d. Does the email link work?
   e. What's the next CTA you see?
4. Check provider dashboard:
   a. Contact exists?
   b. Correct tags/lists?
   c. Automation triggered?
5. Document evidence at each step
```

## Delivery Timing Benchmarks

| Metric | Good | Needs Work | Broken |
|---|---|---|---|
| Asset access time (instant) | <3 seconds | 3-10 seconds | >10 seconds or fails |
| Delivery email time | <2 minutes | 2-10 minutes | >10 minutes or never |
| Thank-you page load | <2 seconds | 2-5 seconds | >5 seconds |
| Form to contact creation | <30 seconds | 30-120 seconds | >2 minutes or fails |

## Output Template

```markdown
## Lead Magnet Delivery: [Asset Name]
**Asset type**: [PDF / Video / Course / Template / Access]
**Delivery method**: [Instant / Email / Hybrid / Account]

### Flow Map
[Step-by-step flow with expected behavior]

### Verification Results
| Step | Status | Evidence |
|---|---|---|
| Form submit | ✅/❌ | [details] |
| Contact creation | ✅/❌ | [details] |
| Asset delivery | ✅/❌ | [details] |
| Thank-you page | ✅/❌ | [details] |
| Next-step CTA | ✅/❌ | [details] |
| Follow-up sequence | ✅/❌ | [details] |

### Asset Delivery Time: [X seconds/minutes]
### Thank-You Page Next CTA: [what it is]
### Follow-Up Sequence: [name, trigger]
### Gaps Identified: [list]
### Recommendations: [prioritized list]
```

## Core Rules
- The promised asset must arrive reliably.
- Delivery method should match user expectation and technical reliability.
- Thank-you pages should reinforce the next step, not dead-end.
- Asset delivery and list growth are one system, not separate chores.
- If the lead magnet is weak, no delivery flow will save it.

## Performance Optimizations

### Speed Multipliers
- Use proven email templates as starting point (subject lines, CTAs, structure)
- Batch API calls for email platform operations
- Pre-fetch subscriber data and sequence info in parallel
- Template-based email generation (don't start from blank)
- A/B test subject lines and CTAs

### Self-Critique Scorecard (/25)
1. **Functionality** (1-5): Does the email/sequence work perfectly?
2. **Quality** (1-5): Is the copy enterprise-grade?
3. **Verification** (1-5): Verified via API + test email + automation check?
4. **Speed** (1-5): Optimal execution?
5. **Learning** (1-5): Patterns documented?

**Target: 22+/25**

### Auto-Check
- [ ] Pre-flight checks (credentials, list/sequence exists)
- [ ] Verified via API + test send
- [ ] Subject line and CTA optimized
- [ ] Score logged to memory

## Output Contract
**Artifact**: Working lead magnet delivery flow with verification proof
**Evidence**: End-to-end test proof (signup to asset delivery to next CTA)
**Decision**: Flow operational or specific gaps identified
**Next**: Monitor conversion rates and optimize thank-you page CTA

## Checks and Common Mistakes
- Do not count form submission alone as successful fulfillment.
- Do not hide the promised asset behind broken or delayed flows.
- Do not leave the thank-you page commercially empty.
- Do not ship without testing with a fresh email.
- Do not treat delivery and monetization as unrelated; the thank-you and first follow-up should move the lead forward.
- Do not assume email delivery works — test with Gmail, Outlook, and a corporate domain.

## Resources
Read when needed:
- `references/delivery-method-decision.md`

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
