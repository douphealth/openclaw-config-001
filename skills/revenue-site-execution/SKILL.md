---
name: revenue-site-execution
description: Use when working on one of the managed websites in `ops/sites/` and the task affects monetization, lead capture, checkout, service funnels, offer clarity, lifecycle email, or conversion paths. Triggers on requests to improve a site, fix a funnel, optimize a money path, ship a launch task, harden a lead flow, or prioritize work across portfolio websites.
---

# Revenue Site Execution

## Purpose
Operate managed revenue sites with ruthless focus on the highest-value live money path. This skill coordinates site-specific execution, prioritization, and verification discipline; it should not become a generic WordPress catch-all.

## Strategic Entry Point
Use this as the **business/revenue entrypoint** for managed-site work.
- Use `wordpress-growth-ops` when the task is primarily WordPress implementation.
- Use `wp-rest-api-mastery` when the task is low-level API state reading/writing.
- Use this skill when the real question is what will move revenue, leads, or monetization fastest.

## Shared Doctrine References
- `skills/shared/wordpress/api-first-safe-write-protocol.md`
- `skills/shared/wordpress/verification-ladder.md`
- `skills/shared/wordpress/cache-plugin-gotchas-matrix.md`


## Enterprise Protocols (MANDATORY)

Before executing, read `skills/shared/enterprise-protocol.md` and follow:
- Pre-flight health check (site accessible, creds valid, state captured)
- Mandatory backup before any modification
- Retry with exponential backoff (max 3 attempts per API call)
- Progress reporting every 10 operations
- Verification after each modification
- Health checks every 50 items in long operations
- Rollback plan identified before starting

## Superpower Layer

For complex or high-risk work, also follow:
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`

Default execution mode:
1. clarify/spec first if ambiguous
2. write a short plan before large execution
3. dispatch parallel workers for independent subtasks
4. review output for spec compliance and quality
5. verify in reality before claiming complete

## When to Use
- A request touches a managed site in `ops/sites/`
- The work affects checkout, lead capture, booking, delivery, service inquiry, affiliate clicks, or offer-to-action flow
- Multiple portfolio tasks must be prioritized by revenue impact and risk
- A launch or fix requires site playbook discipline before any WordPress changes are made


## Do NOT Use For
- Raw WordPress CRUD, meta, media, taxonomy, or REST implementation details (`wp-rest-api-mastery`)
- Broad WordPress implementation work outside the managed portfolio (`wordpress-growth-ops`)
- Full autonomous multi-worker WordPress execution programs (`wordpress-autonomous-ops` or `swarm-orchestrator`)
- Pure SEO, content-planning, or copy-only tasks with no direct money-path impact (`seo-audit-playbook`, `content-strategy-planning`, `conversion-copywriting`)

## Inputs Required
1. Exact site and matching `ops/sites/` playbook
2. Environment: staging vs production and any release constraints
3. Primary money path affected
4. Current blocker, evidence, and urgency
5. Rollback path for live assets being touched

## Triage Protocol
1. Identify the site and read its playbook before anything else
2. State the money path in one sentence
3. Classify blocker type: technical, routing, trust, offer, content, tracking, or delivery
4. Decide if execution belongs here or should route to a core WP skill
5. Choose smallest safe fix that materially improves the money path

## Core Framework
### 1. Site-first preflight
Read in this order when present:
1. `ops/sites/[site].md`
2. `ops/constraints/[site].md`
3. `ops/launch-packs/[site].md` for launch-sensitive work
4. `ops/portfolio/execution-queues.md`

### 2. Priority discipline
Prioritize by:
- broken money path
- active deadline / launch
- revenue impact
- effort to unblock
- risk if delayed

A broken checkout, lead form, or delivery path outranks cosmetic work every time.

### 3. Route the execution correctly
- Use this skill to frame, prioritize, and govern the work
- Use `wp-rest-api-mastery` for the actual REST/meta/media mechanics
- Use `wordpress-growth-ops` for broader WordPress build/fix work
- Use `service-funnel-architecture`, `offer-positioning`, or `lead-magnet-delivery-ops` when the issue is architectural rather than tactical

### 4. Live-site execution discipline
For production WordPress assets:
- capture current state before write
- watch for builder/global-template side effects
- account for cache/CDN/plugin behavior
- prefer smallest reversible change
- verify editor state and rendered money path after the write

### 5. Verification standard
No task is done until the affected money path is tested at the right level:
- **page/path proof** for messaging, CTA, and render fixes
- **behavior proof** for forms, bookings, affiliate clicks, or checkouts
- **downstream proof** for CRM, email, notifications, delivery, or orders

### 6. Batch portfolio workflow
When multiple sites or tasks are involved:
- score all tasks first
- batch by site and by work type
- avoid context-switching mid-operation
- update the execution queue after each verified change

## Performance Optimizations
### Speed Multipliers
- Apply `skills/api-efficiency-protocol.md` for CMS, CRM, email, and checkout systems
- Pre-fetch playbook + constraints before implementation discussions
- Batch similar fixes on the same site before verifying once through the live path
- Reuse rollback snapshots for related changes in one session
- When a task expands beyond one site or one specialist, hand off to `swarm-orchestrator`

## Output Contract
**Artifact**: Verified site change, priority decision, or execution plan tied to a money path
**Evidence**: Before/after state and live-path verification proof
**Decision**: What was changed, deferred, or routed elsewhere
**Next**: Queue update, monitoring, or next highest-impact task

## Anti-Patterns
- ❌ Starting with design polish when the money path is broken
- ❌ Treating this skill like a generic WordPress editor
- ❌ Skipping `ops/sites/` playbooks and site constraints
- ❌ Making production changes without a rollback snapshot
- ❌ Claiming success from CMS state alone without testing the live path
- ❌ Working low-value portfolio tasks while a higher-value site has a broken conversion path

## References
- `references/portfolio-routing.md`
- `references/portfolio-money-paths.md`
- `references/site-priority-by-business-model.md`
- `references/verification-order.md`
- `references/site-file-map.md`
- `skills/references/wp-live-ops-verification.md`

## Self-Critique Scorecard (/25)
1. **Triage** (1-5): Was the highest-value money path identified correctly?
2. **Execution** (1-5): Was the fix scoped to the smallest high-impact move?
3. **Verification** (1-5): Was the real path verified after the change?
4. **Rollback** (1-5): Could the live change be reversed safely?
5. **Learning** (1-5): Were site-specific traps or patterns captured?

**Target: 22+/25**
