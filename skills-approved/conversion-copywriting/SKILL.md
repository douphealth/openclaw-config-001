---
name: conversion-copywriting
description: Enterprise conversion-focused copywriting for homepages, landing pages, pricing pages, product pages, feature pages, CTAs, and offer pages. Use when writing or rewriting marketing copy to increase conversions, sharpen value propositions, improve headline quality, reduce fluff, or create premium SOTA marketing copy that moves people to action.
---

# Conversion Copywriting — Enterprise Marketing Copy

## Purpose
Write clear, persuasive page copy that moves a specific audience toward a specific action. Prioritize clarity, specificity, and proof over cleverness.

## When to Use
- New marketing copy for pages or offers
- Headline, subhead, CTA, or section copy improvements
- Value proposition sharpening
- Homepage, pricing, or product page copy
- Landing page and offer page copy
- Blog-to-conversion bridge copy

**Do NOT use for:** Email sequences (→ `lifecycle-email-sequences`), line-by-line editing of existing drafts (→ `copy-editing-sweeps`), content planning (→ `content-strategy-planning`), offer definition (→ `offer-positioning`), service path design (→ `service-funnel-architecture`), article optimization (→ `editorial-post-enhancement`).

## Copy Framework

### Voice: Hormozi/Ferriss Copy Style
Conversion copy must be punchy, practical, and direct:

**Headlines:**
- Lead with the result: "How We Increased Revenue 340% in 90 Days"
- Use specific numbers: "12,847 Customers Can't Be Wrong"
- Address pain directly: "Stop Losing Sales to Slow Page Speed"

**Body Copy:**
- Short paragraphs (2-3 sentences)
- Bullet points for features/benefits
- Bold key claims
- Include social proof inline: "4.8/5 stars from 2,000+ reviews"

**CTAs:**
- Action-oriented: "Get My Free Audit" not "Submit"
- Value-forward: "Start Saving $500/mo Today"
- Low-friction: "No credit card required"

### Phase 1: Define the Target
1. **Page type**: Homepage, landing page, pricing page, product page, feature page, or CTA section
2. **Primary action**: One clear conversion goal (sign up, buy, book, download, contact)
3. **Audience**: Specific role, context, and current frustration
4. **Traffic source**: Where visitors come from determines what they already know

### Phase 2: Research & Foundation
5. **Problem framing**: Describe the pain in the buyer's language, not yours
6. **Outcome statement**: What changes after they say yes?
7. **Objection map**: What stops them from converting right now?
8. **Proof inventory**: What evidence do you have? (testimonials, data, case studies, logos)

### Phase 3: Write the Copy

**Default page flow:**
```
Headline → Subheadline → CTA → Proof → Problem → Solution → Benefits → How it works → Objections/FAQ → Final CTA
```

**Headline rules:**
- One clear promise or outcome
- Specific > vague (27% faster > significantly faster)
- Test 2-3 options when stakes are high
- Target <= 60 characters for SEO

**Body copy rules:**
- One idea per section
- Feature → Outcome → Value chain (what it does → what that means → why they care)
- Mirror customer language from reviews, support tickets, interviews
- Numbers and specifics over vague claims
- Short paragraphs (2-3 sentences max)

**CTA rules:**
- One primary action per page section
- Action verbs: Start, Get, Try, Book, Download — not Submit or Click
- Reduce friction near CTAs (no competing links, clear next step)

### Phase 4: Proof & Polish
9. Add social proof near CTAs (testimonial, number, logo)
10. Remove filler, corporate sludge, and vague claims
11. Read aloud — if it sounds unnatural, rewrite
12. Final QA: Is the CTA obvious? Could a stranger explain this page in 10 seconds?

## Performance Optimizations

### Speed Multipliers
- **Template-based approach**: Use proven page flow as starting point (don't start from blank)
- **Parallel headline generation**: Write 5 headlines simultaneously, pick best 2-3
- **Research shortcut**: Pull customer language from existing reviews/testimonials on the site
- **Copy patterns library**: Maintain proven patterns for each page type (homepage, pricing, etc.)

### Self-Critique Scorecard (/25)
1. **Clarity** (1-5): Could a stranger explain this in 10 seconds?
2. **Specificity** (1-5): Are claims backed by numbers/examples, not vague?
3. **Persuasion** (1-5): Does the copy move toward the CTA naturally?
4. **Proof** (1-5): Is social proof near CTAs? Are objections addressed?
5. **Polish** (1-5): No filler, corporate sludge, or redundancy?

**Target: 22+/25 before deployment**

### Auto-Check
- [ ] No generic claims without specifics
- [ ] No feature dumps without outcomes
- [ ] CTA is obvious and action-oriented
- [ ] Proof elements placed near conversions
- [ ] Score logged to memory

## Anti-Patterns
- ❌ Generic claims: "streamline your workflow" — be specific
- ❌ Feature dumps without outcomes
- ❌ Multiple competing CTAs on one section
- ❌ Corporate sludge: "leverage synergies to optimize outcomes"
- ❌ Copy that could fit 50 other products (too generic)

## Output Contract
**Artifact**: Conversion copy for target page(s) with headline options, body copy, and CTA variations
**Evidence**: Before/after comparison, persuasion framework used
**Decision**: Copy approved for implementation
**Next**: A/B test if possible, or proceed with deployment

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
