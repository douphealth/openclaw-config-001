---
name: revenue-site-execution
description: Use when working on a managed site in `ops/sites/` and the task affects monetization, lead capture, checkout, service funnels, offer clarity, lifecycle email, or another primary conversion path that should be prioritized over generic site work.
---

# Revenue Site Execution

## Purpose
Route site work through the correct site playbook so execution stays focused on the highest-value conversion path instead of generic busywork or cosmetic drift.

## Use this when
- a task touches a managed website and could affect revenue, leads, offers, checkout, email capture, delivery/access, CTA paths, or service inquiry flows
- site prioritization matters across the portfolio
- the right next move depends on the site’s business model and current monetization path

## Do NOT use this for
- pure content strategy work (→ `content-strategy-planning`)
- pure SEO diagnosis (→ `seo-audit-playbook`)
- isolated WordPress implementation with no portfolio/site-priority decision layer (→ `wordpress-growth-ops`)
- pure final proof of a path (→ `money-path-verification`)

## Do this first
1. Identify the exact site and requested outcome.
2. Read the matching file in `ops/sites/`.
3. Read the matching file in `ops/constraints/` if one exists.
4. Read the matching file in `ops/launch-packs/` if launch or verification work is involved.
5. State the primary money path in one sentence before changing anything.
6. Prioritize that money path unless the user explicitly wants something else.

## Execution model
Default sequence:
1. identify the primary monetization path
2. identify the current blocker
3. classify the path as commerce, lead automation, service funnel, or repo-backed app
4. choose the smallest high-leverage fix
5. verify the result on the real path
6. only then move to polish or secondary work

## Site routing priorities
Default priority order:
1. `efficientgptprompts.com`
2. `affiliatemarketingforsuccess.com`
3. `gearuptogrow.com`
4. remaining portfolio sites

## Worker routing
If using swarm execution, route by need:
- `tech-debugger` for checkout, forms, CRM, delivery, rendering traps, or plugin behavior
- `content-operator` for headlines, offer packaging, service pages, lead magnets, and copy blocks
- `publisher-operator` for publishing pages or content into the live path
- `verifier` for signup, checkout, booking, email, payment, delivery, or CTA proof
- `research-operator` when offer or audience positioning is still unclear

Use `offer-positioning`, `service-funnel-architecture`, or `lead-magnet-delivery-ops` when the blocker is strategic path design rather than simple page editing.

## Rules
- money path before cosmetics
- verification before “done”
- live-path proof beats assumptions
- prefer API / REST / direct checks before browser-only work
- avoid low-value blog polish on revenue-priority sites before funnel proof exists

## Resources
Read when needed:
- `references/portfolio-routing.md`
- `references/portfolio-money-paths.md`
- `references/site-priority-by-business-model.md`
- `references/verification-order.md`
- `references/site-file-map.md`

## Checks and common mistakes
- Do not start with design tweaks when checkout, lead capture, or CTA proof is unresolved.
- Do not treat all sites as equal priority.
- Do not ignore site-specific traps in `ops/constraints/`.
- Do not claim success from partial UI inspection when a real transaction or lead path can be tested.

## Output contract
**Artifact:** site improvement plan or executed site change tied to the primary money path
**Evidence:** site-specific context plus before/after or money-path proof
**Decision:** prioritized action taken, blocked, or ready for verification
**Next:** verify business impact, continue to next blocker, or hand off to the correct specialist skill
