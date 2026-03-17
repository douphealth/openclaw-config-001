---
name: wordpress-growth-ops
description: Use when a WordPress site needs growth work that crosses content, funnel, plugin, form, CRM, checkout, performance, security, publishing, or verification layers and the task affects monetization, lead capture, or conversion. Triggers on WordPress conversion problems, funnel debugging, plugin conflicts affecting revenue, WP-CLI diagnostics, site speed affecting conversions, or multi-layer WordPress growth optimization.
---

# WordPress Growth Ops

## Purpose
Handle WordPress growth as an integrated system — diagnosis → fix → verify → improve — using deterministic procedures, WP-CLI-first operations, and self-critiquing quality gates to ensure every change actually moves the conversion needle.

## Use this when
- a WordPress task affects a lead path, checkout path, booking path, email capture path, or offer page
- the blocker could be copy, form behavior, plugin config, CRM wiring, performance, security, or publishing quality
- the work spans more than simple content editing but is not purely server infrastructure
- diagnosing why a WordPress site converts poorly despite traffic
- a plugin/theme update broke a money path
- site speed is impacting conversion rate or SEO rankings affecting revenue

## Do NOT use this for
- server or runtime infrastructure work (→ `infrastructure-ops`)
- standalone email platform setup (→ `email-marketing-engine`)
- pure end-to-end proof of a path after changes are done (→ `money-path-verification`)
- heavy single-article editorial work as the main task (→ `editorial-post-enhancement`)
- WordPress core/plugin development from scratch (use WordPress/agent-skills directly)

## Self-Improvement Protocol

After every WordPress growth operation, run this critique loop:

1. **Pattern capture:** Did this diagnosis reveal a new failure mode? Add it to `references/operational-traps.md`.
2. **Routing accuracy:** Did the first-pass diagnosis find the real issue, or did you need extra rounds? Log the miss in daily memory.
3. **Verification quality:** Did the verification step catch a regression? If not, strengthen the verification checklist.
4. **Speed:** Could the diagnosis have been faster with a different initial probe? Update the diagnostic order.
5. **Metric impact:** 48 hours after the fix, check if the conversion metric actually improved. If not, the fix addressed a symptom — escalate.

## Do this

### Phase 0: Triage and Detect (WP-CLI first)

Run deterministic detection before making ANY changes:

```bash
# Detect WP install, version, active plugins, theme
wp core version --path=<path>
wp plugin list --status=active --path=<path>
wp theme list --status=active --path=<path>

# Check for critical issues
wp doctor check --path=<path>          # autoload bloat, debug flags, update status
wp option get siteurl --path=<path>    # confirm correct URL
wp rewrite flush --dry-run --path=<path>  # check permalink structure
```

**Classify the site type** (routes to different growth strategies):
- **Content/Affiliate site:** revenue from ads, affiliates, display → focus on traffic→click paths
- **E-commerce (WooCommerce):** revenue from products → focus on product→cart→checkout→order
- **Service/Lead gen:** revenue from inquiries/bookings → focus on page→form→CRM→follow-up
- **SaaS/App:** revenue from signups/trials → focus on landing→signup→onboarding

### Phase 1: Map the Money Path

Identify the PRIMARY money path and trace every hop:

| Hop | What to check | WP-CLI / REST probe |
|---|---|---|
| Traffic entry | Which pages get traffic? | `wp db query "SELECT post_name, meta_value FROM wp_posts p JOIN wp_postmeta pm ON p.ID=pm.post_id WHERE pm.meta_key='_yoast_wpseo_focuskw' LIMIT 20"` |
| Offer/CTA | Is the offer clear? Does CTA render? | `curl -s <page-url> \| grep -i 'cta\|buy\|book\|sign.up'` |
| Form/Checkout | Does the form submit? Does Woo process? | Test via REST: `POST /wp-json/<form-plugin>/submit` or Woo `/wp-json/wc/v3/orders` |
| Plugin wiring | Does the form/checkout plugin fire hooks? | Check `wp cron event list` for scheduled sends, check plugin settings via `wp option get <plugin_option>` |
| CRM/Automation | Does data reach the CRM/ESP? | Check provider API for recent contacts, check automation trigger logs |
| Delivery | Does the user get what was promised? | Test with real email, check delivery logs |

**If the path design itself is weak,** route through `offer-positioning`, `service-funnel-architecture`, or `lead-magnet-delivery-ops` BEFORE touching WordPress.

### Phase 2: Diagnose by Layer (bottom-up)

Fix the lowest broken layer first:

#### Layer 1: Performance (site speed → conversion impact)
Slow sites kill conversion before the user sees the offer.

```bash
# Quick performance check
wp doctor check --path=<path>           # catches autoload bloat, debug flags
wp profile stage --path=<path>          # bootstrap / main_query / template timing

# Check autoloaded options (common bloat source)
wp db query "SELECT option_name, LENGTH(option_value) as size FROM wp_options WHERE autoload='yes' ORDER BY LENGTH(option_value) DESC LIMIT 20"

# Check object cache
wp cache flush --path=<path>            # only if safe and needed
```

**Critical WordPress 6.9+ considerations:**
- Classic themes now get on-demand CSS (30-65% CSS reduction)
- Block themes can load with zero render-blocking CSS
- If performance is poor despite these, check: unoptimized images, render-blocking plugins, excessive HTTP API calls on every request, cron spike overhead

#### Layer 2: Rendering (does the page actually show what it should?)
```bash
# Check for PHP errors
wp eval 'echo (WP_DEBUG ? "DEBUG ON" : "debug off");' --path=<path>

# Check for broken blocks/content
wp db query "SELECT post_id FROM wp_postmeta WHERE meta_key='_wp_old_slug' LIMIT 5"

# Verify critical shortcodes/blocks render
curl -s <page-url> | grep -c 'class="wp-block\|shortcode-error\|This block\|Invalid block'
```

Common failures:
- Plugin shortcodes broken after update
- Gutenberg "Invalid block" errors after theme/plugin changes
- Cached pages showing stale content (check cache plugin purge status)

#### Layer 3: Form/Checkout Wiring
```bash
# Check form plugin status
wp plugin list --name=<form-plugin> --path=<path>

# Check if form pages exist and are published
wp post list --post_type=page --s=<form-page-slug> --path=<path>

# Test REST API form submission
curl -X POST <site>/wp-json/<form-namespace>/v1/submit \
  -H "Content-Type: application/json" \
  -d '{"fields":{"email":"test@example.com","name":"Test"},"form_id":<id>}'
```

#### Layer 4: CRM/Email Automation Wiring
- Check if the form plugin has a CRM integration active
- Verify API keys/tokens are valid (not expired/revoked)
- Test with a fresh email address (stale contacts lie)
- Check automation trigger conditions (tags, segments, lists)

#### Layer 5: Performance Post-Fix Verification
After ANY fix:
```bash
# Re-measure the same metric
wp profile stage --path=<path>          # if performance fix
curl -s -o /dev/null -w "%{time_total}" <page-url>

# Verify the fix is live (not cached)
curl -s -H "Cache-Control: no-cache" <page-url> | grep <expected-change>
```

### Phase 3: Apply Fix + Self-Critique

Before declaring "fixed":

1. **Apply the smallest high-leverage change.** One layer at a time.
2. **Self-critique:** Did I verify on the REAL user path, not just the admin? (Yes/No)
3. **Self-critique:** Did I use a fresh test input, not stale data? (Yes/No)
4. **Self-critique:** Did I check for regression in other money paths? (Yes/No)
5. If any answer is No → fix the verification gap before proceeding.

### Phase 4: Publishing Quality (if content/funnel pages changed)

For any page that's part of a money path:
- Contextual internal links to supporting content
- Clear visual hierarchy (scannable headings, short paragraphs)
- Trust signals near CTA (testimonials, guarantees, social proof)
- Clean title / slug / focus keyphrase (SEO metadata)
- Fast-loading media (compressed images, lazy loading, proper sizes)
- Mobile-first rendering (check responsive layout)

### Phase 5: Post-Change Verification

```bash
# Verify critical paths
wp doctor check --path=<path>

# Test money path end-to-end with fresh input
curl -X POST <form-endpoint> -d '{"email":"verify-$(date +%s)@test.com"}'

# Check for new PHP errors
tail -20 <wp-content>/debug.log  # if WP_DEBUG_LOG enabled

# Verify no regression in other pages
wp eval 'echo get_option("siteurl");' --path=<path>
```

## Operating rules
- Start with the conversion target, not the WordPress admin.
- WP-CLI first — it's deterministic and doesn't lie like admin UIs do.
- Fix the lowest blocking layer first (performance → rendering → wiring → automation → copy).
- Money path before cosmetics. Always.
- Fresh test inputs beat stale contact records. Always.
- After meaningful changes, verify the live path, not just the admin config.
- Prefer stable plugin-supported mechanisms over brittle hacks.
- Document every non-obvious fix in `memory/YYYY-MM-DD.md` for pattern learning.

## Default layer order
1. Performance (speed kills conversion before the user sees the offer)
2. Rendering (broken blocks/shortcodes/theming)
3. Form/checkout wiring (submit transport, AJAX, nonces)
4. CRM/automation/delivery wiring
5. Offer/CTA clarity and copy
6. Publishing quality and trust signals
7. Proof/verification

## Build vs buyer rule
Separate internal build assets from buyer-facing delivery assets.
- Internal: manifests, implementation notes, launch docs, fulfillment specs
- Buyer: guided docs, examples, templates, bonuses, deliverables

Never ship internal scaffolding as if it were customer value.

## Resources
Read when needed:
- `references/common-wordpress-money-paths.md` — money path templates by site type
- `references/portfolio-wordpress-routing.md` — routing rules for multi-site operations
- `references/operational-traps.md` — learned failure modes (updated by self-improvement protocol)
- `references/wp-growth-diagnostic-checklist.md` — step-by-step diagnostic flowchart
- `references/conversion-layer-audit.md` — detailed conversion layer analysis patterns
- `references/wp-performance-growth.md` — performance optimizations that directly impact conversion

WordPress/agent-skills (official, for deep WP development work):
- `wp-performance` — profiling, caching, database optimization
- `wp-plugin-development` — plugin architecture, hooks, security
- `wp-rest-api` — REST endpoints, schema, auth
- `wp-wpcli-and-ops` — WP-CLI operations, automation, multisite
- `wp-block-development` — Gutenberg blocks, deprecations
- `wp-block-themes` — theme.json, templates, patterns

## Checks and common mistakes
- Do not mistake admin writability for real front-end success (verify on live path).
- Do not assume static HTML reflects JS/AJAX submit behavior (test actual form transport).
- Do not spend hours on styling while the money path is still broken (layers before cosmetics).
- Do not trust "subscriber exists" as proof of email delivery (check inbox/provider history).
- Do not fix copy before verifying the form actually submits and the CRM actually receives data.
- Do not declare "fixed" without a fresh successful end-to-end test.
- Do not ignore performance — a 3-second page load kills 40%+ of conversions before the offer is seen.
- Do not cache-purge in production during traffic peaks (schedule low-traffic windows).

## Output contract
**Artifact:** WordPress growth improvement with diagnostic report showing which layer was broken, what was fixed, and verification proof
**Evidence:** WP-CLI output confirming fix + live path test with fresh input + before/after performance metrics (if applicable)
**Decision:** Change is live and verified, blocked (with specific blocker), or needs deeper verification via `money-path-verification`
**Next:** Monitor conversion metric for 48h, run self-improvement protocol, or escalate to specialized skill for follow-up work
