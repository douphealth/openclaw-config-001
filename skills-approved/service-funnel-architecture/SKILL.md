---
name: service-funnel-architecture
description: Use when designing or repairing a service funnel across homepage, service page, audit page, triage page, booking flow, inquiry path, or CTA architecture. Triggers on requests to build a service funnel, improve consultation flow, turn traffic into leads, structure a B2B service path, or connect positioning, CTA, and lead capture into one path.
---

# Service Funnel Architecture

## Do NOT Use This For
- writing conversion copy (use conversion-copywriting)
setting up email automation (use email-marketing-engine)

## Purpose
Design service funnels that move visitors from interest to qualified inquiry without muddled pages or broken CTA logic. Every page has one job; every step earns the next.

## Use this when
- Designing or repairing a service funnel (homepage → service page → inquiry/booking)
- Improving consultation flow, lead quality, or CTA progression
- Structuring a B2B service path from traffic to qualified lead
- Connecting positioning, CTA, and lead capture into one coherent path

Do **not** use for: offer definition (use `offer-positioning` first), copy-level writing (use `conversion-copywriting`), or verifying the live path works (use `money-path-verification` after implementation).

## Do this

### Phase 1: Define the path
1. Define the primary paid service or entry offer — everything else routes to this.
2. Choose the shortest viable path:
   - **Homepage → CTA → booking/inquiry** (simple services)
   - **Homepage → service page → CTA → inquiry** (needs explanation)
   - **Homepage → audit page → CTA → qualification → booking** (complex/expensive)
   - **Homepage → triage page → segmented path → booking** (multiple services)

3. Define what qualifies as a real lead (firmographic, budget, timeline, authority criteria).

### Phase 2: Conversion math
4. Set the funnel target: Revenue goal → required deals → required qualified leads → required traffic.
5. Benchmark conversion rates per step:
   - Page visit → CTA click: 3–8% (hero), 8–15% (inline/exit-intent)
   - CTA click → form start: 40–60%
   - Form start → submission: 50–70%
   - Submission → qualified lead: 30–60% (depends on qualification criteria)
   - Qualified lead → closed deal: 10–30% (depends on sales cycle)

6. Work backwards from revenue to identify the bottleneck step.
7. Size the gap: current conversion × current traffic vs. target conversion × needed traffic.

### Phase 3: CTA architecture
8. Map CTA progression: attention → interest → desire → action (not all on one page).
9. Each page has ONE primary CTA and at most one secondary CTA.
10. Homepage should route, not explain everything — sell the click to the next page.
11. Service pages sell the next step, not the full service — the inquiry/booking is the product.

### Phase 4: Friction audit
12. Count fields: every form field above 3 reduces submission rate ~10%.
13. Check mobile flow: thumb-reachable CTAs, no horizontal scroll, fast load.
14. Verify confirmation/follow-up exists: automated email, calendar invite, or CRM alert.
15. Test the path yourself — if you hesitate at any step, the user will too.

### Phase 5: Build order
16. Recommended sequence: positioning → service page → CTA → inquiry/booking form → follow-up automation → homepage routing → triage page (if needed).

## Core rules
- One primary path per page — don't split attention.
- Homepage routes, service pages sell the next step.
- Qualification logic matters as much as lead volume.
- If booking exists, confirmation and follow-up are part of the funnel, not afterthoughts.
- Do not call the funnel done without testing the lead path end-to-end.

## Output contract
Deliver:
1. **Funnel goal** — revenue target, deal size, timeline
2. **Conversion math** — backwards from revenue to traffic needs
3. **Page map** — role of each page, primary CTA per page
4. **CTA path map** — visual flow from entry to qualified lead
5. **Qualification criteria** — what makes a lead real
6. **Friction points** — identified issues with severity rating
7. **Build order** — phased implementation sequence
8. **Verification plan** — how to confirm the path works live

## Verification steps
- [ ] Conversion math is realistic (not aspirational) and benchmarked
- [ ] Every page has exactly one primary CTA
- [ ] Qualification criteria are defined before any form is built
- [ ] Follow-up automation exists for every submission type
- [ ] The path has been walked end-to-end by a human

## Resources
Read when needed:
- `references/funnel-models.md` — funnel patterns and page-type definitions

## Checks and common mistakes
- Do not send cold traffic into a vague contact page.
- Do not treat a form as a funnel — a funnel is a path with logic.
- Do not add secondary offers before the main service path is clear.
- Do not skip the conversion math — guessing leads to traffic waste.
- Do not forget mobile — most B2B buyers research on phones first.

## Output Contract
**Artifact**: Skill-specific deliverable (report, fix, config, or document)
**Evidence**: Proof that the work was completed correctly
**Decision**: What was decided or recommended
**Next**: Follow-up action or monitoring period
