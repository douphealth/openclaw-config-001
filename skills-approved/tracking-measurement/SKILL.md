---
name: tracking-measurement
description: Use when auditing, planning, or fixing measurement across GA4, GTM, ad platforms, pixels, conversion actions, event taxonomies, consent-aware tagging, or attribution flows. Triggers on requests for conversion tracking audits, measurement plans, tracking discrepancies, event design, tag debugging, enhanced conversions, CAPI, or "is this tracked correctly?".
---

# Tracking & Measurement

## Purpose
Make conversion and behavior tracking trustworthy enough to optimize from. If the data lies, the optimization misleads.

## Use this when
- Auditing conversion tracking across GA4, GTM, ad platforms, or pixels
- Designing event taxonomies or measurement plans
- Debugging tag fires, discrepancies, or missing conversions
- Setting up enhanced conversions, CAPI, or consent-aware tagging
- Verifying "is this tracked correctly?"



## Do this

### Phase 1: Map the measurement landscape
1. Identify business-critical events: purchases, qualified leads, core activations, sign-ups.
2. Map each event from source (page/app) → transformation (GTM/data layer) → destination (GA4, ad platforms, CRM).
3. List all platforms involved: GA4, GTM, Meta Pixel, Google Ads, LinkedIn Insight Tag, CRM, CDP.
4. Document current event names, parameters, and triggers.

### Phase 2: Event taxonomy design
5. Design a consistent event taxonomy following this pattern:
   - **Naming**: `category_action_detail` (e.g., `form_submit_lead gen`, `purchase_complete`)
   - **Parameters**: Always include `event_id` (dedup), `value`, `currency`, `source`, `medium`
   - **User properties**: `user_type`, `account_tier`, `segment` where applicable
   - **Custom dimensions**: Map every parameter to a GA4 custom dimension before it's needed

6. Taxonomy rules:
   - One event per meaningful user action (not one event with 15 parameters)
   - Standard events first (`page_view`, `click`, `form_submit`, `purchase`), custom events only when standard doesn't fit
   - Never use spaces or capital letters in event names
   - Document every event in a shared taxonomy sheet

### Phase 3: GTM/GA4 implementation checklist
7. **Container setup**:
   - [ ] GTM container installed on all pages (not just marketing site)
   - [ ] GA4 configuration tag fires on all pages
   - [ ] Cross-domain tracking configured if multiple domains
   - [ ] Debug mode / GTM preview verified in staging

8. **Event tracking**:
   - [ ] All business-critical events have GTM triggers
   - [ ] Events fire on the correct trigger type (click, form submit, timer, custom event)
   - [ ] Parameters are populated with actual values, not defaults
   - [ ] `event_id` is unique per event instance (for deduplication)

9. **Conversion setup**:
   - [ ] Key events marked as conversions in GA4
   - [ ] Conversion values are populated (static or dynamic)
   - [ ] Google Ads conversion actions import from GA4 (or are independently tagged)
   - [ ] Meta Conversions API configured alongside pixel (not just pixel)

10. **Data quality**:
    - [ ] No duplicate events firing (check GTM preview + GA4 debug)
    - [ ] Internal/team traffic excluded via filter or GTM condition
    - [ ] Referral exclusions set for payment processors and own domains
    - [ ] Consent mode configured and respected (EU/privacy-sensitive audiences)

### Phase 4: Validate
11. Perform a test conversion on each critical path.
12. Check GA4 Realtime to confirm the event arrived with correct parameters.
13. Verify the event appears in the correct ad platform (Google Ads, Meta).
14. Check for duplication: one action should produce one event_id across platforms.
15. Quantify discrepancies: if platform numbers disagree, calculate the gap.

### Phase 5: Report & prioritize
16. Report what is tracked correctly, incorrectly, and not at all.
17. Prioritize fixes by business impact: purchases/leads > activations > vanity events.
18. Define a validation plan for ongoing monitoring.

## Core rules
- Bad tracking is worse than missing tracking when it misleads optimization.
- Check deduplication and cross-platform consistency before trusting counts.
- Treat privacy and consent behavior as part of measurement quality, not a side note.
- If platform numbers disagree, quantify the discrepancy instead of hand-waving.
- Do not mark tracking "fixed" without a validation pass.

## Output contract
Deliver:
1. **Measurement map** — events → parameters → destinations (table format)
2. **Event taxonomy** — documented event names, parameters, triggers
3. **Critical discrepancies** — platform number gaps with quantified delta
4. **Likely root causes** — why each discrepancy exists
5. **Priority fixes** — ranked by business impact, with effort estimate
6. **Validation plan** — how to confirm each fix works
7. **Remaining risks** — what's still unmeasured or uncertain

## Verification steps
- [ ] Every business-critical event fires exactly once per user action
- [ ] All events have `event_id` for cross-platform deduplication
- [ ] GA4 Realtime shows the event with correct parameter values
- [ ] Ad platform conversion counts are within 10% of GA4 (document larger gaps)
- [ ] Consent mode blocks events for non-consented users (test with cleared cookies)
- [ ] Taxonomy is documented in a shared reference (not just in someone's head)

## Resources
Read when needed:
- `references/measurement-debug-order.md`
- `references/portfolio-measurement-priorities.md`

## Checks and common mistakes
- Do not assume tags firing equals accurate reporting — verify end-to-end.
- Do not optimize campaigns against secondary or noisy conversion actions by accident.
- Do not ignore transaction IDs, event IDs, value, currency, or source metadata.
- Do not skip consent/privacy checks — they cause silent data loss.
- Do not use different event naming conventions across platforms — pick one taxonomy and enforce it.

## Do NOT Use This For
- Reporting on already-trusted data (→ analytics-reporting)
- Paid media strategy or audit (→ paid-media-audit)
- Writing or editing content (→ editorial-post-enhancement)
- Funnel architecture or offer positioning (→ service-funnel-architecture or offer-positioning)
- Email automation setup (→ email-marketing-engine)

## Output Contract
**Artifact**: Measurement map, event taxonomy, and prioritized fix list with root causes
**Evidence**: Event firing verification, parameter validation, and discrepancy quantification
**Decision**: What is tracked correctly, incorrectly, and not at all
**Next**: Implement fixes, then validate each critical path end-to-end
