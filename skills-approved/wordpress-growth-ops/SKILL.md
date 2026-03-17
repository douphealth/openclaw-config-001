---
name: wordpress-growth-ops
description: Use when a WordPress site needs growth work that crosses content, funnel, plugin, form, CRM, checkout, publishing, or verification layers and the task affects monetization or lead capture.
---

# WordPress Growth Ops

## Purpose
Handle WordPress growth work as one integrated system so copy, funnel logic, plugin behavior, publishing quality, and verification all support the same conversion path.

## Use this when
- a WordPress task affects a lead path, checkout path, booking path, email capture path, or offer page
- the blocker could be copy, form behavior, plugin config, CRM wiring, delivery flow, or publishing quality
- the work spans more than simple content editing but is not purely infrastructure

## Do NOT use this for
- server or runtime infrastructure work (→ `infrastructure-ops`)
- standalone email platform setup (→ `email-marketing-engine`)
- pure end-to-end proof of a path after changes are done (→ `money-path-verification`)
- heavy single-article editorial work as the main task (→ `editorial-post-enhancement`)

## Operating rules
- Start with the conversion target, not the WordPress admin.
- Fix the smallest blocking layer first.
- Money path before cosmetics.
- Prefer stable plugin-supported mechanisms over brittle hacks when reliability is comparable.
- After meaningful changes, verify the live path.

## Do this
1. Define the target path: checkout, lead capture, booking, consultation, or email capture.
2. Identify the current blocker: copy, CTA logic, rendering, form wiring, plugin config, CRM/automation, or delivery.
3. If the path design itself is weak, route through `offer-positioning`, `service-funnel-architecture`, or `lead-magnet-delivery-ops` before tinkering.
4. Apply the smallest high-leverage fix.
5. Improve publishing quality if it materially affects conversion clarity or trust.
6. Verify the real user path using `money-path-verification` principles.

## Default layer order
1. offer / CTA clarity
2. form / checkout wiring
3. CRM / automation / delivery wiring
4. proof / verification
5. secondary polish

## Build vs buyer rule
Separate internal build assets from buyer-facing delivery assets.
- internal assets: manifests, implementation notes, launch docs, fulfillment specs
- buyer assets: guided docs, examples, templates, bonuses, deliverables

Never ship internal scaffolding as if it were customer value.

## Publishing-quality rule
For major editorial or landing-page upgrades, improve both content and publishing quality where relevant:
- contextual internal links
- clear visual structure
- relevant media
- useful examples and implementation guidance
- clean title / slug / focus-keyphrase logic
- plugin-aware SEO title/meta handling without spam

## Resources
Read when needed:
- `references/common-wordpress-money-paths.md`
- `references/portfolio-wordpress-routing.md`
- `references/operational-traps.md`

## Checks and common mistakes
- Do not mistake admin writability for real front-end success.
- Do not assume static HTML reflects JS/AJAX submit behavior.
- Do not spend hours on styling while the money path is still broken.
- Do not bury critical conversion logic inside fragile content blobs when a cleaner implementation exists.

## Output contract
**Artifact:** WordPress site improvement tied to a real conversion path
**Evidence:** before/after change summary plus path proof or verification handoff
**Decision:** change is live, blocked, or needs deeper verification
**Next:** monitor conversion impact or re-verify the affected path
