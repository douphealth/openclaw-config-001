---
name: email-automation-debugging
description: Use when diagnosing broken or unreliable welcome emails, nurture automations, CRM triggers, list syncs, sender issues, delayed sends, missing subscribers, or plugin-to-provider automation paths. Triggers on requests to debug email automation, prove welcome flow works, fix signup-to-email delivery, diagnose Brevo/FluentCRM automation issues, or determine why a subscriber did not get the expected email.
---

# Email Automation Debugging

## Do NOT Use This For
- designing email sequences (use lifecycle-email-sequences)
general email marketing setup (use email-marketing-engine)

## Purpose
Find the real break in signup-to-email automation and prove the fix with fresh evidence.

## Use this when
Use this skill when the problem is not writing emails but making sure the automation actually fires and delivers.

## Do this
1. Identify the exact trigger event and expected first email.
2. Map form/bot submit -> contact creation -> segmentation/tagging -> automation trigger -> send -> inbox evidence.
3. Check whether the real submission path is HTML, AJAX, API, plugin hook, or JS-injected behavior.
4. Verify provider state, sender state, and automation conditions.
5. Test with a fresh email and capture evidence at each step.
6. Report the exact failing hop, not just the symptom.

## Core rules
- Plugin connectivity is not proof of end-to-end automation.
- Use the real submission mechanism, not the one that looks simplest.
- Fresh test inputs beat old contact records.
- Distinguish trigger failure from send failure from delivery failure.
- If sender/authentication is relevant, include it in the diagnosis.

## Output
Default output should include:
- expected path map
- proven working hops
- broken hop
- evidence
- likely root cause
- fix recommendation
- retest plan

## Resources
Read when needed:
- `references/debug-hop-order.md`
- `references/afms-special-case.md`


## Output Contract
**Artifact**: Working email automation with delivery proof
**Evidence**: Test signup result, email history record
**Decision**: Automation confirmed working
**Next**: Monitor for 24h
## Checks and common mistakes
- Do not stop at "subscriber exists" if the email never fired.
- Do not trust stale automations or old contacts as proof.
- Do not ignore hidden fields, tags, source params, or intent params that affect routing.
- Do not mark fixed without a fresh successful send path.
- **Delivery proof ≠ Content proof.** An email can show `status: "sent"` with `subject: "0"` and empty body. Always verify email_subject AND email_body in the history record.
- **FluentCRM funnel `send_custom_email` with `reference_campaign` is unreliable** — campaign objects are often shells with no content.
- **CRM bulk action `add_to_email_sequence` may require Pro** (`FLUENTCAMPAIGN` constant) — check if the REST API direct endpoint works instead.
- **Direct enrollment API is often more reliable than bulk actions** — e.g., `POST /sequences/{id}/subscribers` with `{"subscriber_ids": [N]}`.
- **Mailer settings may not be exposed via REST API** — check `wp_options` directly if possible.
- **User-Agent header required** for WordPress REST API from Python's urllib (curl works without it).

## WordPress REST API Gotchas
- `urllib` gets 403 where curl works → add `User-Agent: Mozilla/5.0` header
- `wp/v2/settings` only returns whitelisted options (no CRM/mailer settings)
- FluentCRM settings stored in `wp_options` table, not exposed via REST API
- WP-CLI not always available on hosting
- PHP file upload restricted to media types by default
