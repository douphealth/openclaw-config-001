---
name: email-automation-debugging
description: Use when diagnosing broken or unreliable welcome emails, nurture automations, CRM triggers, list syncs, sender issues, delayed sends, missing subscribers, or plugin-to-provider automation paths. Triggers on requests to debug email automation, prove welcome flow works, fix signup-to-email delivery, diagnose Brevo/FluentCRM automation issues, or determine why a subscriber did not get the expected email.
---

# Email Automation Debugging

## Do NOT Use This For
- designing email sequences (use `lifecycle-email-sequences`)
- general email marketing setup (use `email-marketing-engine`)

## Purpose
Find the real break in signup-to-email automation and prove the fix with fresh evidence.

## Use this when
The problem is not writing emails but making sure the automation actually fires and delivers.

## Decision Tree

```
Email automation not working?
├── Subscriber not created? → Capture hop failure → Form/API debugging
├── Subscriber created, no email? → Trigger hop failure → Automation conditions
├── Email sent, not delivered? → Delivery hop failure → Sender/DKIM/deliverability
├── Wrong email received? → Routing failure → Segmentation/tags/conditions
└── Delayed email? → Queue/timing → Provider status, scheduling rules
```

## Flow Mapping Template

Map the expected path before debugging. Fill this in first:

```
[User action] → [Form/bot submit] → [Contact creation] → [Segmentation/tag]
→ [Automation trigger] → [Send event] → [Delivery] → [Inbox evidence]

Example:
Visit landing page → Fill form "Free Guide" → Contact in Brevo
→ Tag: "lead-magnet-guide" → Automation "Welcome Series" fires
→ Email #1 sent → Delivered to inbox → Email received
```

Each arrow is a **hop**. Your job is to prove each hop works or find the first one that breaks.

## Hop-by-Hop Verification

### Hop 1: Capture (Form → Contact Creation)
- [ ] Form exists on the correct page (not a staging/draft URL)
- [ ] Form submits via correct mechanism (HTML POST, AJAX, API, JS-injected)
- [ ] Hidden fields present (utm_source, referrer, intent params)
- [ ] No browser console errors during submission
- [ ] Contact record appears in provider within 60 seconds
- **Test method**: Submit with a fresh email (use `test+timestamp@domain.com`)

### Hop 2: Segmentation/Tagging
- [ ] Contact received expected tags or list membership
- [ ] No conflicting tags that would exclude from automation
- [ ] Source/medium fields populated if routing depends on them
- **Check**: Look at the contact record directly in the provider dashboard

### Hop 3: Automation Trigger
- [ ] Automation is active (not draft/paused)
- [ ] Trigger condition matches the contact's tags/fields
- [ ] No audience exclusion blocking the contact
- [ ] Automation entry limit not exceeded (some have "enter once" rules)
- **Check**: Provider automation logs or activity feed

### Hop 4: Send Event
- [ ] Email content exists and is published (not draft)
- [ ] Sender address is verified and not blacklisted
- [ ] No suppression list blocking the recipient
- [ ] **Verify email_subject AND email_body exist** — some systems show `status: "sent"` with empty content
- **Check**: Email history/activity log in provider

### Hop 5: Delivery & Inbox
- [ ] Check spam/junk folder
- [ ] Verify DKIM, SPF, DMARC records are passing
- [ ] Check sender reputation via provider tools
- [ ] Test with a different email domain (Gmail, Outlook) to rule out domain-level blocks
- **Tool**: mail-tester.com for deliverability scoring

## Provider-Specific Debugging

### Brevo (Sendinblue)
- Check Automation logs: Automations → [name] → Logs tab
- Contact must be in the correct list AND have the trigger attribute
- Transactional vs. Marketing emails have different sender configurations
- API key permissions: ensure `automation` scope is included
- Common failure: form integration creates contact but doesn't add to list

### Mailchimp
- Check Customer Journey → [name] → View reports
- Automation triggers can be "added to audience" or "tag added" — verify which
- Contact must pass audience settings (double opt-in, cleaned status)
- Merge tag mismatches cause silent personalization failures
- Common failure: audience field mapping doesn't match form field names

### ConvertKit (Kit)
- Check Automations → [name] → Subscriber history
- Forms, tags, and sequences are separate — a form can exist without a sequence
- Visual automations have explicit entry/exit rules — check both
- Sequences have delay rules that override automation timing
- Common failure: subscriber added to form but no sequence attached

### FluentCRM (WordPress)
- Contact must be in the CRM database (check `wp_fcrm_contacts`)
- Sequences need explicit enrollment — form submission alone doesn't trigger
- `send_custom_email` with `reference_campaign` is unreliable — campaigns are often shells
- Bulk action `add_to_email_sequence` may require Pro (`FLUENTCAMPAIGN` constant)
- Direct enrollment API: `POST /sequences/{id}/subscribers` with `{"subscriber_ids": [N]}`
- Mailer settings stored in `wp_options`, not exposed via REST API

## WordPress REST API Gotchas
- `urllib` gets 403 where curl works → add `User-Agent: Mozilla/5.0` header
- `wp/v2/settings` only returns whitelisted options (no CRM/mailer settings)
- FluentCRM settings in `wp_options` table, not exposed via REST API
- WP-CLI not always available on hosting
- PHP file upload restricted to media types by default

## Delivery Proof Checklist

Before declaring "it works":
- [ ] Fresh test submission with new email address
- [ ] Contact record verified in provider dashboard
- [ ] Tags/list membership confirmed on contact record
- [ ] Automation log shows entry event
- [ ] Email history shows send event with subject AND body
- [ ] Test email received in primary inbox (not spam)
- [ ] All personalization fields rendered correctly
- [ ] Links in email work and track correctly
- [ ] Result replicable (second test email works too)

## Test Execution Order

1. **Map the expected flow** (fill in flow template above)
2. **Test with fresh email** — never reuse old contacts as proof
3. **Capture evidence at each hop** — screenshots or API responses
4. **Report the exact failing hop** — not just "emails aren't sending"
5. **Fix the break** — not adjacent issues
6. **Retest with fresh email** — prove the fix, not just the change

## Output Template

```markdown
## Email Automation Debug: [Automation Name]
**Provider**: [Brevo/Mailchimp/ConvertKit/FluentCRM]
**Test email**: [test address used]

### Expected Path
[Flow map from trigger to inbox]

### Hop Results
| Hop | Status | Evidence |
|---|---|---|
| Capture | ✅/❌ | [details] |
| Segmentation | ✅/❌ | [details] |
| Trigger | ✅/❌ | [details] |
| Send | ✅/❌ | [details] |
| Delivery | ✅/❌ | [details] |

### Broken Hop: [which one]
### Root Cause: [specific failure]
### Fix Applied: [what changed]
### Retest Result: [pass/fail with evidence]
```

## Core Rules
- Plugin connectivity is not proof of end-to-end automation.
- Use the real submission mechanism, not the one that looks simplest.
- Fresh test inputs beat old contact records.
- Distinguish trigger failure from send failure from delivery failure.
- If sender/authentication is relevant, include it in the diagnosis.

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
**Artifact**: Working email automation with delivery proof
**Evidence**: Test signup result, email history record, inbox receipt
**Decision**: Automation confirmed working or specific failure identified
**Next**: Monitor for 24h or fix the identified hop

## Checks and Common Mistakes
- Do not stop at "subscriber exists" if the email never fired.
- Do not trust stale automations or old contacts as proof.
- Do not ignore hidden fields, tags, source params, or intent params that affect routing.
- Do not mark fixed without a fresh successful send path.
- Do not assume delivery = inboxed. Check spam, promotions tab, and different email providers.

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
