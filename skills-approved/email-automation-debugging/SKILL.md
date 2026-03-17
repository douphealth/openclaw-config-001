---
name: email-automation-debugging
description: Use when diagnosing broken or unreliable welcome emails, nurture automations, CRM triggers, list syncs, sender issues, delayed sends, missing subscribers, or plugin-to-provider automation paths that need fresh end-to-end proof.
---

# Email Automation Debugging

## Purpose
Find the real break in a signup-to-email automation path and prove the fix with fresh evidence rather than stale records or optimistic provider status.

## Use this when
- a welcome email or nurture automation is not firing reliably
- a subscriber exists but did not get the expected email
- CRM tags, segments, or automation triggers may be misconfigured
- plugin-to-provider automation paths are failing or inconsistent
- sender state, delivery state, or delayed-send behavior may be involved

## Do NOT use this for
- designing email sequences (→ `lifecycle-email-sequences`)
- general email marketing setup (→ `email-marketing-engine`)
- pure launch go/no-go checks without debugging a broken hop (→ `launch-readiness-audit`)

## Debug order
1. Identify the exact trigger event and expected first email.
2. Map the path: submit → contact creation → tagging/segmentation → automation trigger → send → inbox evidence.
3. Check the real submission mechanism: HTML, AJAX, API, plugin hook, or JS-rendered behavior.
4. Verify provider state, sender state, and automation conditions.
5. Test with a fresh email input.
6. Capture proof at each hop.
7. Report the exact failing hop, root cause, and retest plan.

## Core rules
- Plugin connectivity is not proof of end-to-end automation.
- Fresh test inputs beat old contact records.
- Distinguish trigger failure from send failure from delivery failure.
- Delivery proof is not content proof; verify subject/body when relevant.
- Do not mark fixed without a fresh successful send path.

## Useful gotchas
- Hidden fields, tags, source params, or intent params may affect routing.
- Some CRM bulk actions are less reliable than direct enrollment endpoints.
- Provider “sent” status can still hide broken content or wrong campaign references.
- REST/API settings exposure may be incomplete; some systems require checking underlying stored config.
- WordPress REST requests from Python/urllib may need a real `User-Agent` header where curl works.

## Resources
Read when needed:
- `references/debug-hop-order.md`
- `references/afms-special-case.md`

## Checks and common mistakes
- stopping at “subscriber exists” when the email never fired
- trusting stale contacts as proof
- ignoring sender/authentication state when delivery is the issue
- using the wrong submission path when the real system depends on AJAX or JS hooks
- reporting “fixed” without fresh inbox or provider-history evidence

## Output contract
**Artifact:** email automation debug report with path map and failing hop
**Evidence:** fresh test result plus proof for each working/broken hop
**Decision:** root cause identified, fix applied or recommended, and automation confirmed or still blocked
**Next:** retest, monitor for recurrence, or escalate to provider/platform-specific fix
