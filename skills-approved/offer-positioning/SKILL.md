---
name: offer-positioning
description: Enterprise offer positioning and value proposition design. Use when clarifying, strengthening, or reframing an offer for a homepage, service page, product page, audit offer, sprint offer, lead magnet, or monetization path. Triggers on sharpening positioning, improving value proposition clarity, defining target audience, reducing generic messaging, or turning vague capability into a concrete sellable offer.
---

# Offer Positioning — Enterprise Value Proposition Design

## Purpose
Turn vague capability into a concrete, understandable offer people can say yes to. Make the next step obvious and the value undeniable.

## When to Use
- Clarifying, strengthening, or reframing a service/product/monetization offer
- Positioning an audit, sprint, consulting package, lead magnet, or upsell
- The offer exists operationally but not persuasely
- Messaging is generic, audience is unclear, or value prop is fuzzy

**Do NOT use for:** Page-level copy (→ `conversion-copywriting`), funnel structure (→ `service-funnel-architecture`), lead delivery setup (→ `lead-magnet-delivery-ops`).

## Positioning Framework

### Phase 1: Buyer & Problem
1. **Buyer profile**: Role, context, what they've already tried
2. **Pain in their words**: What's frustrating, costly, or risky right now
3. **Desired outcome**: What changes after they say yes
4. **Urgency**: Why now vs. someday?

### Phase 2: Value Proposition Canvas
5. Map against four axes:
   - **Job to be done**: What is the buyer trying to accomplish?
   - **Pains**: What frustrates them about the current situation?
   - **Gains**: What does success look like?
   - **Offer fit**: How does this offer address pains and deliver gains?

6. Lead with the parts of the offer that matter most to the buyer

### Phase 3: Define the Offer
7. **Type**: Audit, sprint, retainer, product, lead magnet, or upsell
8. **Deliverables**: What's included, what's not, what makes this different
9. **Naming**: Plain language — no jargon, no internal terminology
10. **Quantification**: "5-page audit" > "comprehensive review"
11. **Price anchoring**: Show value before price (ROI framing, cost-of-inaction)

### Phase 4: Differentiation Depth Ladder

Pick the deepest level you can truthfully claim:

| Level | Type | Example |
|-------|------|---------|
| Surface | "We're better" | "Higher quality, better support" |
| Feature | Unique capability | "Only tool with real-time co-editing" |
| Mechanism | How it works differently | "AI-assisted, not AI-generated" |
| Outcome | Provable result | "First qualified lead in 48 hours" |
| Category | Redefine the space | "Not another CRM — a revenue OS" |

### Phase 5: Sharpen
12. Tighten promise: one clear outcome the buyer gets
13. Add proof: case studies, testimonials, before/after
14. Reduce risk: guarantee, freemium tier, low-commitment entry
15. Make CTA obvious: one primary action in buyer-language
16. If the offer can't be explained in 2 sentences, it's not ready

## Output Contract
**Artifact**: Offer positioning document with value prop, differentiators, and CTA
**Evidence**: Buyer profile, problem/outcome framing, differentiation ladder level
**Decision**: Offer positioned and ready for copy
**Next**: Hand to conversion-copywriting for page implementation

## Anti-Patterns
- ❌ "We're the best" without mechanism or outcome proof
- ❌ For everyone = for no one
- ❌ Feature dump without pain/outcome framing
- ❌ Multiple offers competing for attention
- ❌ No quantified deliverables
- ❌ Vague CTAs: "Learn more" without clear path

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
