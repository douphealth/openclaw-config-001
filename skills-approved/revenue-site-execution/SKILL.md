---
name: revenue-site-execution
description: Use when working on one of the managed websites in `ops/sites/` and the task affects monetization, lead capture, checkout, service funnels, offer clarity, lifecycle email, or conversion paths. Triggers on requests to improve a site, fix a funnel, optimize a money path, ship a launch task, harden a lead flow, or prioritize work across portfolio websites.
---

# Revenue Site Execution

## Do NOT Use This For
- content strategy (use `content-strategy-planning`)
- SEO auditing (use `seo-audit-playbook`)

## Purpose
Route website work through the correct site playbook so execution focuses on the highest-value conversion path instead of generic busywork.

## Use this when
A task touches a managed website and the work could affect revenue, leads, offers, checkout, email capture, delivery/access, CTA paths, or service inquiry flows.

## Decision Tree

```
Site work request?
├── Is it a managed site in ops/sites/? → Continue below
├── Not in ops/sites/ → Ask for site details, treat as one-off
├── Affects money path? → Revenue Site Execution flow
├── Content-only, no conversion impact? → Route to content-strategy-planning
└── SEO-only, no conversion impact? → Route to seo-audit-playbook
```

## Pre-Execution Checklist (Do This First)

1. **Identify the site** — exact URL and matching file in `ops/sites/`
2. **Read site playbook** — `ops/sites/[site-name].md`
3. **Read constraints** — `ops/constraints/[site-name].md` (if exists)
4. **Read launch pack** — `ops/launch-packs/[site-name].md` (if launch/verification work)
5. **State the money path** in one sentence before changing anything
6. **Check execution queue** — `ops/portfolio/execution-queues.md` for existing priorities

**Never skip step 5.** If you can't state the primary money path in one sentence, you don't understand the site well enough to edit it.

## Portfolio Site Priority

Default priority order:
1. `efficientgptprompts.com` — highest revenue per visitor
2. `affiliatemarketingforsuccess.com` — affiliate revenue
3. `gearuptogrow.com` — ecommerce/service hybrid
4. Remaining portfolio sites by revenue potential

### Priority Override Rules
- A broken money path on ANY site jumps to #1 regardless of site rank
- Active launch/deadline overrides revenue ranking
- Security or downtime issues override everything

## Money Path Classification

Classify the site's primary monetization model before choosing execution approach:

| Model | Primary Path | Key Metrics | Verification Method |
|---|---|---|---|
| **Commerce** | Product → Cart → Checkout → Delivery | Revenue, AOV, conversion rate | Test transaction |
| **Lead Automation** | CTA → Form → Email → Conversion | Lead volume, lead-to-close rate | Test signup + automation proof |
| **Service Funnel** | Homepage → Service page → Inquiry → Booking | Qualified leads, booking rate | Test inquiry submission |
| **Affiliate** | Content → Click → External conversion | RPM, CTR to affiliate, EPC | Click tracking verification |
| **Hybrid** | Multiple paths | Weighted by revenue contribution | Test highest-revenue path first |

## Execution Model (5-Step Sequence)

### Step 1: Identify Primary Money Path
```
"What is the #1 way this site makes money right now?"
→ Answer must be specific: "Users buy [product] via [checkout path]"
→ Not: "It gets traffic and does stuff"
```

### Step 2: Identify Current Blocker
```
"What is preventing this money path from converting at full potential?"
→ Check: Is it broken, slow, unclear, untrustworthy, or missing?
→ Evidence: Actual test result, analytics data, or user behavior signal
```

### Step 3: Classify & Choose Fix Size
```
Money path type: [commerce/lead/service/affiliate/hybrid]
Blocker category: [technical/content/offer/funnel/tracking]
Fix size: [quick (<1h) / medium (1-4h) / large (>4h) / strategic (needs planning)]
```

**Rule**: Always choose the smallest fix that unblocks the money path. Don't redesign the homepage when the checkout button is broken.

### Step 4: Execute the Fix
- Make the change
- Document what changed and why
- Note any side effects or dependencies

### Step 5: Verify on the Live Path
- Test the actual money path end-to-end
- Capture evidence (screenshot, API response, test transaction)
- Only declare done after verification passes

## Worker Routing (Swarm Mode)

If using parallel execution, route by specialty:

| Worker | Use For | Not For |
|---|---|---|
| `tech-debugger` | Checkout, forms, CRM, delivery, rendering, plugins | Copy, strategy, offers |
| `content-operator` | Headlines, offer packaging, service pages, lead magnets, copy blocks | Technical debugging, publishing |
| `publisher-operator` | Publishing pages or content into the live path | Strategy, copywriting, debugging |
| `verifier` | Signup, checkout, booking, email, payment, delivery, CTA proof | Initial implementation |
| `research-operator` | Offer or audience positioning still unclear | Execution |
| `offer-positioning` | Strategic offer clarity | Tactical page edits |
| `service-funnel-architecture` | Full funnel design/redesign | Single-page fixes |
| `lead-magnet-delivery-ops` | Lead capture + delivery flows | General page work |

## Priority Queue Management

When multiple sites need work, score each task:

| Factor | Weight | Scoring |
|---|---|---|
| Revenue impact | 40% | High = 3, Medium = 2, Low = 1 |
| Urgency/deadline | 25% | Active deadline = 3, Soon = 2, No deadline = 1 |
| Effort to fix | 20% | Quick = 3, Medium = 2, Large = 1 |
| Risk if delayed | 15% | Broken path = 3, Degraded = 2, Optimize = 1 |

**Priority Score** = (Revenue × 0.4) + (Urgency × 0.25) + (Effort × 0.2) + (Risk × 0.15)

Work highest score first.

## Batch Execution Workflow

For multi-site or multi-task work:

```
1. Scan all sites for blockers (quick audit, 5 min per site)
2. Score and sort by priority queue
3. Group by worker type (all tech fixes together, all content together)
4. Execute in batches with verification after each batch
5. Document results in ops/portfolio/execution-queues.md
```

## Execution Queue Tracking

After each execution, update the queue:

```markdown
## [Site Name] — [Date]
**Task**: [what was done]
**Money path affected**: [which path]
**Status**: ✅ verified / ⚠️ needs follow-up / ❌ failed
**Evidence**: [link or description]
**Next**: [what needs to happen next]
```

## Core Rules
- Money path before cosmetics.
- Verification before "done."
- Live-path proof beats assumptions.
- Prefer API / REST / direct checks before browser-only work.
- Avoid low-value blog polish on revenue-priority sites before funnel proof exists.
- State the money path in one sentence before touching anything.

## Output Template

```markdown
## Site Execution: [Site Name]
**Date**: YYYY-MM-DD
**Request**: [what was asked]
**Money path**: [one-sentence description]

### Pre-Execution State
[What the money path looked like before]

### Action Taken
[What was changed and why]

### Verification Result
[End-to-end test result with evidence]

### Impact Estimate
[Expected effect on conversion/revenue]

### Remaining Work
[Any follow-up needed]
```

## Output Contract
**Artifact**: Site improvement with verification proof
**Evidence**: Before/after state, money path test result
**Decision**: Change deployed and verified or gaps identified
**Next**: Revenue impact tracking, follow-up tasks, or move to next priority

## Performance Optimizations

### Speed Multipliers
- **Pre-fetch site playbook** — read ops/sites/[site].md before any other work
- **Batch verification** — check money path + API + live page simultaneously
- **Queue management** — always check execution-queues.md before starting (avoids conflicts)
- **Parallel portfolio ops** — when working multiple sites, batch similar operations

### Self-Critique Protocol
After every revenue site operation:
1. Did I state the money path before starting?
2. Did I verify the money path still works after changes?
3. Did I check site-specific constraints?
4. Did I prioritize by revenue impact?
5. Score: /25 using quality framework

## Checks and Common Mistakes
- Do not start with design tweaks when checkout, lead capture, or CTA proof is unresolved.
- Do not treat all sites as equal priority.
- Do not ignore site-specific traps in `ops/constraints/`.
- Do not claim success from partial UI inspection when a real transaction or lead path can be tested.
- Do not work on site #4's blog when site #1's checkout is broken.
- Do not skip the money path statement — it prevents scope creep.

## Resources
Read when needed:
- `references/portfolio-routing.md`
- `references/portfolio-money-paths.md`
- `references/site-priority-by-business-model.md`
- `references/verification-order.md`
- `references/site-file-map.md`

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
