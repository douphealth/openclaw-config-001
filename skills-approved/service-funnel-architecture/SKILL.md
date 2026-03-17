---
name: service-funnel-architecture
description: Use when designing or repairing a service funnel across homepage, service page, audit page, triage page, booking flow, inquiry path, or CTA architecture. Triggers on requests to build a service funnel, improve consultation flow, turn traffic into leads, structure a B2B service path, or connect positioning, CTA, and lead capture into one path.
---

# Service Funnel Architecture

## Do NOT Use This For
- writing conversion copy (use `conversion-copywriting`)
- setting up email automation (use `email-marketing-engine`)
- defining the offer itself (use `offer-positioning` first)

## Purpose
Design service funnels that move visitors from interest to qualified inquiry without muddled pages or broken CTA logic. Every page has one job; every step earns the next.

## Use this when
Designing or repairing a service funnel (homepage → service page → inquiry/booking), improving consultation flow or lead quality, structuring a B2B service path, or connecting positioning, CTA, and lead capture into one coherent path.

## Decision Tree

```
Service funnel needed or broken?
├── No funnel exists? → Design from scratch (full 5-phase process)
├── Funnel exists but low conversion? → Friction audit (Phase 4)
├── Wrong leads coming in? → Qualification redesign (Phase 1, step 3)
├── High drop-off at specific stage? → Stage-specific CTA optimization
├── No clear entry offer? → Route to offer-positioning FIRST
└── Just need to verify it works? → Route to money-path-verification
```

## Funnel Model Selection

Choose the shortest viable path:

| Model | Path | Use When |
|---|---|---|
| **Direct** | Homepage → CTA → Booking | Simple, well-known service. Low friction. |
| **Explained** | Homepage → Service page → CTA → Inquiry | Service needs explanation. Buyer needs education. |
| **Audited** | Homepage → Audit page → CTA → Qualification → Booking | Complex/expensive service. Trust needed before buy. |
| **Triaged** | Homepage → Triage → Segmented paths → Booking | Multiple services. Different buyers need different paths. |
| **Content-led** | Content → CTA → Service page → Inquiry | Inbound/content-driven. Reader → lead → buyer. |

**Rule**: Start with the simplest model that works. Complexity is a cost, not a feature.

## Phase 1: Define the Path

1. **Primary paid service or entry offer** — everything else routes to this
2. **Funnel model** — choose from table above
3. **Qualification criteria** — what makes a lead real:

| Criterion | Weak Signal | Strong Signal |
|---|---|---|
| **Budget** | "Looking for affordable" | "Budget approved: $X" |
| **Timeline** | "Someday maybe" | "Need to start within 30 days" |
| **Authority** | "I'll ask my boss" | "I make the decision" |
| **Fit** | "Just exploring" | "We specifically need [your service]" |

**Define qualification before building any forms** — the form fields and follow-up logic depend on it.

## Phase 2: Conversion Math

Work backwards from revenue:

```
Revenue Goal: $X/month
÷ Average Deal Size: $Y
= Required Closed Deals: Z/month
÷ Close Rate (qualified → closed): W%
= Required Qualified Leads: Z÷W/month
÷ Lead Qualification Rate: V%
= Required Form Submissions: (Z÷W)÷V/month
÷ Visit-to-Submission Rate: U%
= Required Traffic: ((Z÷W)÷V)÷U/month
```

### Benchmark Conversion Rates Per Step

| Step | Typical Range | Red Flag |
|---|---|---|
| Page visit → CTA click | 3-8% (hero), 8-15% (inline/exit) | <2% |
| CTA click → Form start | 40-60% | <25% |
| Form start → Submission | 50-70% | <35% |
| Submission → Qualified lead | 30-60% | <20% |
| Qualified lead → Closed deal | 10-30% | <8% |

**Size the gap**: Current conversion × current traffic vs. target conversion × needed traffic. This tells you whether the problem is traffic (volume) or conversion (path quality).

## Phase 3: CTA Architecture

### CTA Progression
Map the emotional journey, not just the buttons:

```
Attention (Homepage hero): "Get a free [audit/assessment]"
    ↓
Interest (Service page): "See how we approach [problem]"
    ↓
Desire (Social proof section): "See [similar company]'s results"
    ↓
Action (Inquiry/booking CTA): "Book your [specific next step]"
```

### CTA Rules
- **One primary CTA per page** and at most one secondary CTA
- **Homepage routes, doesn't explain** — sell the click to the next page
- **Service pages sell the next step**, not the full service — the inquiry/booking IS the product
- **Secondary CTA** = lower commitment version of primary (download vs. book, email vs. call)
- **Never use "Contact Us"** as primary CTA — it signals "I don't know what you need"

### Page-by-Page CTA Map

| Page | Primary CTA | Secondary CTA | Purpose |
|---|---|---|---|
| Homepage | → Service page or Audit | Download lead magnet | Route to next step |
| Service page | → Inquiry/Booking | → Case studies | Sell the next step |
| Audit page | → Qualification form | → Service page | Build trust + qualify |
| Inquiry form | Submit | → FAQ (new tab) | Capture + reduce friction |
| Thank-you page | → Calendar / Resource | — | Confirm + advance |

## Phase 4: Friction Audit

### Form Friction
- Every field above 3 reduces submission rate ~10%
- Name + Email = minimum viable form
- Phone number kills B2C forms; B2B tolerates it with qualification value
- "Company name" and "Website" are good B2B qualifiers without high friction

### Mobile Friction
- [ ] CTAs thumb-reachable (bottom 40% of screen)
- [ ] No horizontal scroll
- [ ] Form fields don't zoom off-screen on focus
- [ ] Page load <3 seconds on 4G
- [ ] Tap targets ≥44px

### Trust & Confirmation Friction
- Testimonials near CTAs (not on a separate page) with specific results (numbers, names)
- Guarantee or risk-reversal near action point
- Automated confirmation email within 5 minutes
- CRM alert to team for new inquiries
- **Self-test**: Walk the path yourself. Every hesitation = a friction point.

## Phase 5: Build Order

Recommended implementation sequence:

```
1. Positioning/offer clarity (if not defined)
2. Service page (the core selling page)
3. Primary CTA → Inquiry/booking form
4. Follow-up automation (confirmation email, CRM routing)
5. Homepage routing (CTAs pointing to service page)
6. Thank-you page with next-step CTA
7. Triage page (only if multiple services need routing)
8. Secondary content (case studies, FAQ, testimonials)
```

**Do not build the homepage first.** The service page is the core — everything routes to it.

## Funnel Mapping Template

```markdown
## Service Funnel: [Business/Service Name]
**Funnel model**: [Direct / Explained / Audited / Triaged / Content-led]
**Revenue target**: $X/month
**Average deal**: $Y

### Conversion Math
Traffic → CTA clicks → Form starts → Submissions → Qualified → Closed (fill targets + current + gap)

### Page Map
Page | Role | Primary CTA | Secondary CTA (fill table)

### Qualification Criteria
[What makes a lead real]

### Friction Points
Location | Issue | Severity | Fix (fill table)

### Build Order + Verification Plan
[Implementation sequence and how to confirm the path works live]
```

## Core Rules
- One primary path per page — don't split attention.
- Homepage routes, service pages sell the next step.
- Qualification logic matters as much as lead volume.
- If booking exists, confirmation and follow-up are part of the funnel, not afterthoughts.
- Do not call the funnel done without testing the lead path end-to-end.
- Build the service page before the homepage.

## Output Contract
**Artifact**: Funnel architecture with page map, CTA architecture, and conversion math
**Evidence**: Conversion benchmarks, friction audit results, qualification criteria
**Decision**: Funnel design approved with build order and success metrics
**Next**: Implement in build order, verify with money-path-verification, then optimize

## Verification Steps
- [ ] Conversion math is realistic (not aspirational) and benchmarked
- [ ] Every page has exactly one primary CTA
- [ ] Qualification criteria are defined before any form is built
- [ ] Follow-up automation exists for every submission type
- [ ] The path has been walked end-to-end by a human
- [ ] Mobile experience tested on actual device
- [ ] Thank-you page advances the lead (not dead-ends)

## Checks and Common Mistakes
- Do not send cold traffic into a vague contact page.
- Do not treat a form as a funnel — a funnel is a path with logic.
- Do not add secondary offers before the main service path is clear.
- Do not skip the conversion math — guessing leads to traffic waste.
- Do not forget mobile — most B2B buyers research on phones first.
- Do not build the homepage before the service page.

## Resources
Read when needed:
- `references/funnel-models.md`
- `references/conversion-benchmarks.md`

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
