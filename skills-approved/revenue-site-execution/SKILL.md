---
name: revenue-site-execution
description: Use when working on one of the managed websites in `ops/sites/` and the task affects monetization, lead capture, checkout, service funnels, offer clarity, lifecycle email, or conversion paths. Triggers on requests to improve a site, fix a funnel, optimize a money path, ship a launch task, harden a lead flow, or prioritize work across portfolio websites.
---

# Revenue Site Execution

## Do NOT Use This For
- content strategy (use content-strategy-planning)
SEO auditing (use seo-audit-playbook)

## Purpose
Route website work through the correct site playbook so execution focuses on the highest-value conversion path instead of generic busywork.

## Use this when
Use this skill whenever a task touches a managed website and the work could affect:
- revenue
- leads
- offers
- checkout
- email capture
- delivery / access
- CTA paths
- service inquiry flows

## Do this first
1. Identify the exact site and the current requested outcome.
2. Read the matching file in `ops/sites/`.
3. Read the matching file in `ops/constraints/` if one exists.
4. Read the matching file in `ops/launch-packs/` if launch or verification work is involved.
5. State the primary money path in one sentence before changing anything.
6. Prioritize only the money path unless the user explicitly wants something else.

## Site routing priorities
Default priority order:
1. `efficientgptprompts.com`
2. `affiliatemarketingforsuccess.com`
3. `gearuptogrow.com`
4. remaining portfolio sites

## Execution model
For site work, default to this sequence:
1. identify primary monetization path
2. identify current blocker
3. classify the path as commerce, lead automation, service funnel, or repo-backed app
4. choose smallest high-leverage fix
5. verify the result on the real path
6. only then move to polish or secondary content

## Worker routing
If using swarm execution, route by site playbook:
- `tech-debugger` for checkout, forms, CRM, delivery, rendering traps, or plugin behavior
- `content-operator` for headlines, offer packaging, service pages, lead magnets, copy blocks
- use `offer-positioning`, `service-funnel-architecture`, or `lead-magnet-delivery-ops` when the blocker is strategic path design rather than simple page editing
- `publisher-operator` for publishing pages or content into the live path
- `verifier` for signup, checkout, booking, email, payment, delivery, or CTA proof
- `research-operator` when offer or audience positioning is still unclear

## Rules
- Money path before cosmetics.
- Verification before “done.”
- Live-path proof beats assumptions.
- Prefer API / REST / direct checks before browser-only work.
- Avoid low-value blog polish on revenue-priority sites before funnel proof exists.

## Resources
Read when needed:
- `references/portfolio-routing.md`
- `references/portfolio-money-paths.md`
- `references/site-priority-by-business-model.md`
- `references/verification-order.md`
- `references/site-file-map.md`


## Output Contract
**Artifact**: Site improvement with verification
**Evidence**: Before/after metrics, money path proof
**Decision**: Change deployed and verified
**Next**: Revenue impact tracking
## Checks and common mistakes
- Do not start with design tweaks when checkout, lead capture, or CTA proof is unresolved.
- Do not treat all sites as equal priority.
- Do not ignore site-specific traps in `ops/constraints/`.
- Do not claim success from partial UI inspection when a real transaction or lead path can be tested.
