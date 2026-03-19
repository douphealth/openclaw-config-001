# Site Ops Registry

Durable per-site operating dossiers for execution, recovery, and safe routing.

## How to Use
For any site operation, consult this file before mutation. Update it when a site reveals new quirks, cache traps, plugin conflicts, or preferred execution patterns.

Each site dossier should include:
- stack
- auth source of truth
- cache/CDN behavior
- plugin/theme quirks
- preferred skills
- preferred execution pattern
- common failure modes
- verification traps
- backup location

---

## plantastichaven.com
- **Stack:** WordPress + LiteSpeed + Cloudflare + CyberPanel
- **Auth source:** `.secrets/plantastichaven.access.env`
- **Origin IP:** `107.173.167.3`
- **Cache/CDN:** Cloudflare proxied; origin HTTPS historically unstable
- **Known quirk:** origin HTTP works, origin HTTPS has timed out / LiteSpeed redirect issues
- **Known content issue:** duplicate Link Whisper related-post blocks, duplicated modules, broken wrapper states
- **Preferred skills:** `site-audit-director`, `wp-rest-api-mastery`, `content-integrity-cleanup`, `batch-mutation-controller`, `failure-recovery-director`
- **Preferred execution pattern:** canary → small wave → verify live → continue
- **Common failure modes:** 524/timeout, partial saves, duplicate blocks, render corruption
- **Verification traps:** raw content may differ from render due to plugin-injected modules
- **Backup location:** `ops/backups/ph-posts/`

## micegoneguide.com
- **Stack:** WordPress + Cloudflare
- **Auth source:** `.secrets/micegoneguide.access.env`
- **Known quirk:** cache may lag after changes; verify cache-busted and canonical URL
- **Known issue class:** markdown remnants, raw tables, invalid YouTube embeds from bad batch automation
- **Preferred skills:** `wordpress-growth-ops`, `wp-rest-api-mastery`, `content-integrity-cleanup`, `seo-audit-playbook`
- **Preferred execution pattern:** batch with backup + live verification
- **Backup location:** `ops/backups/mgg-posts/`, `ops/backups/mgg-optimize/`

## affiliatemarketingforsuccess.com
- **Stack:** WordPress + FluentCRM + Cloudflare
- **Auth source:** `.secrets/affiliatemarketingforsuccess.access.env`
- **Known quirk:** FluentCRM automation path requires verification beyond REST success
- **Preferred skills:** `revenue-site-execution`, `email-automation-debugging`, `lead-magnet-delivery-ops`

## gearuptofit.com
- **Stack:** WordPress + Elementor + Cloudflare
- **Known quirk:** content may live in Elementor structures, not just post body
- **Preferred skills:** `wordpress-growth-ops`, `editorial-post-enhancement`, `wp-rest-api-mastery`

## mysticaldigits.com
- **Stack:** WordPress + GeneratePress + Seraphinite + Cloudflare
- **Known quirk:** cache behavior and server-side acceleration can delay visible changes
- **Preferred skills:** `seo-audit-playbook`, `schema-ops`, `wp-error-recovery`


## Expanded Site Dossiers

## affiliatemarketingforsuccess.com
- **Role:** High-priority service + email monetization site.
- **Monetization path:** affiliate revenue audit / monetization service; lead magnet + deterministic welcome flow; later affiliate monetization
- **Default swarm pattern:** tech-debugger -> Brevo / FluentCRM / plugin path; content-operator -> audit offer pages; publisher-operator -> publish monetization pages; verifier -> signup -> email -> CTA path
- **Highest-value tasks:** Deterministic signup -> welcome email proof; Service positioning pages; CTA clarity and offer packaging
- **Avoid:** getting distracted by Woo/store work unless it directly affects the money path
- **Verify first:** form submission; contact creation; automated first email; sender/domain authentication state

## efficientgptprompts.com
- **Role:** High-priority digital product + consulting funnel.
- **Monetization path:** digital product sales; consulting upsell; lead magnet -> email capture
- **Default swarm pattern:** tech-debugger -> commerce / checkout / delivery; content-operator -> sales copy and product support copy; media-operator -> visual polish only where conversion-relevant; verifier -> cart / checkout / delivery / payment visibility
- **Highest-value tasks:** End-to-end purchase proof; Delivery/access flow for the product; Product page clarity and trust
- **Avoid:** pushing complex marketing HTML into WooCommerce product descriptions when it breaks rendering; spending time on non-converting blog polish before store proof exists
- **Verify first:** add to cart; checkout; payment method availability; order creation

## frenchyfab.com
- **Role:** Low-priority unclear-direction property.
- **Monetization path:** unknown until positioning is clarified
- **Default swarm pattern:** research-operator -> business model clarification; director decides whether to invest further
- **Highest-value tasks:** Clarify offer and audience before doing execution work
- **Avoid:** random content production without a monetization thesis

## gearuptofit.com
- **Role:** Low-priority affiliate/content property.
- **Monetization path:** long-tail content; affiliate reviews/comparisons; lead magnets later
- **Default swarm pattern:** research-operator -> keyword/intent map; content-operator -> affiliate content batches; verifier -> render + links
- **Highest-value tasks:** Only work when top-priority sites are stable; Focus on high-intent comparison content if touched
- **Avoid:** treating it as an urgent cash engine

## gearuptogrow.com
- **Role:** High-priority service-monetization site.
- **Monetization path:** growth audit / conversion triage; sprint offer; B2B service funnel
- **Default swarm pattern:** research-operator -> offer + audience gaps; content-operator -> homepage/service page copy; publisher-operator -> publish funnel pages; verifier -> CTA + form + booking path
- **Highest-value tasks:** Homepage repositioning around a paid offer; Service page / triage page; Booking / payment path
- **Avoid:** spending too much time polishing generic blog content before the offer exists
- **Verify first:** homepage CTA path; service inquiry / booking path; payment or lead capture path

## mysticaldigits.com
- **Role:** Secondary / optional monetization property.
- **Monetization path:** direct paid reports/readings if intentionally pursued; niche lead capture
- **Default swarm pattern:** research-operator -> offer angle validation; content-operator -> direct-response pages only if chosen; verifier -> lead/payment path
- **Highest-value tasks:** Do not spend heavy execution here unless a direct offer is chosen; If worked, focus on monetizable offer pages, not broad content

## openclaw-skillshub.com
- **Role:** Repo-managed app / distribution property tied to the OpenClaw ecosystem.
- **Monetization path:** distribution hub; authority / acquisition layer; productized skill marketplace or lead capture
- **Default swarm pattern:** research-operator -> positioning + product/distribution model; ACP coding session -> code, build, deployment, app changes; verifier -> live app path / CTA / signup checks
- **Highest-value tasks:** Inspect repo and deployment model; Clarify commercial goal; Improve strongest CTA path around discovery, signup, or marketplace action
- **Avoid:** WordPress assumptions; wp-admin / REST workflows

## outdoormisting.com
- **Role:** Likely niche commercial / product-led site. Access and monetization path still need validation.
- **Monetization path:** product-led landing pages; buyer guides / comparisons; quote or inquiry path if service-based
- **Default swarm pattern:** research-operator -> site/business model validation; publisher-operator or tech-debugger only after access is confirmed; verifier -> conversion path
- **Highest-value tasks:** Validate access; Identify whether this is ecommerce, lead-gen, or affiliate; Build around the shortest conversion path
- **Avoid:** large execution before access + business model are validated
