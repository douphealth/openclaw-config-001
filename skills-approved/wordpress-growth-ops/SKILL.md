---
name: wordpress-growth-ops
description: Use when a WordPress site needs growth work that crosses content, funnel, plugin, form, CRM, checkout, or publishing layers. Triggers on requests to improve a WordPress site’s conversion path, fix form or plugin issues affecting monetization, ship offer pages, harden lead capture, or connect copy, tech, and verification into one execution pass.
---

# WordPress Growth Ops

## Do NOT Use This For
- server infrastructure (use infrastructure-ops)
email marketing setup (use email-marketing-engine)

## Purpose
Handle WordPress growth work as one integrated system: copy, funnel, plugin behavior, publishing, and verification.

## Use this when
Use this skill when a WordPress task is not purely content and not purely technical, but sits on the conversion path.

For heavy editorial upgrade work on a specific article, pair with `editorial-post-enhancement`.

## Do this
1. Define the target path: checkout, lead capture, booking, or email capture.
2. Identify whether the blocker is copy, plugin/config, rendering, form wiring, CRM wiring, or verification.
3. If the path itself is weak, route through `offer-positioning`, `service-funnel-architecture`, or `lead-magnet-delivery-ops` before tinkering.
4. Fix the smallest blocking layer first.
5. Verify on the live path using `money-path-verification` principles.

## Default layer order
- offer / CTA clarity
- form / checkout wiring
- CRM / automation / delivery wiring
- proof / verification
- secondary polish

## Build vs buyer rule
Separate internal build assets from buyer-facing delivery assets.
- internal assets: manifests, implementation notes, launch docs, fulfillment specs
- buyer assets: guided core docs, examples, templates, bonuses, deliverables
Never ship internal scaffolding as if it were customer value.

## Rules
- Avoid isolated WordPress tinkering with no conversion target.
- Do not bury critical conversion logic inside fragile content blobs when a cleaner implementation exists.
- Prefer stable plugin-supported mechanisms over hacks when speed and reliability are comparable.
- After major changes, verify the live path.
- For major editorial upgrades, improve both the content and its publishing quality: contextual internal links, evenly distributed link placement, relevant media, embedded video, higher-quality references, visually structured HTML, standout FAQ design, richer semantic entity coverage, concrete examples, stronger implementation guidance, a single optimized overhead title, a short keyword-relevant slug, a clear focus keyphrase, and plugin-aware SEO title/meta description handling without becoming spammy.

## Resources
Read when needed:
- `references/common-wordpress-money-paths.md`
- `references/portfolio-wordpress-routing.md`
- `references/operational-traps.md`


## Output Contract
**Artifact**: WordPress site improvement
**Evidence**: Before/after comparison, money path proof
**Decision**: Changes live and verified
**Next**: Monitor conversion impact
## Checks and common mistakes
- Do not mistake admin writability for real front-end success.
- Do not assume static HTML reflects JS/AJAX submit behavior.
- Do not spend hours on styling when the money path is broken.
