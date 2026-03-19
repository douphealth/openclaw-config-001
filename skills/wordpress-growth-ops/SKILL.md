---
name: wordpress-growth-ops
description: Enterprise WordPress execution for growth-critical site work across content, templates, conversion paths, plugin/theme behavior, and deployment verification. Use when a WordPress site needs revenue-impacting work that spans publishing, page structure, UX, money paths, or coordinated plugin/theme changes. NOT for: pure REST endpoint execution (→ wp-rest-api-mastery), performance diagnosis (→ wordpress-performance), or recovery-first debugging when the failure class is unclear (→ wp-error-recovery).
---

# WordPress Growth Ops

## Purpose
Operate WordPress like a production growth surface, not a blogging UI. This skill handles cross-functional execution where content, templates, plugins, verification, monetization paths, and rollout safety all matter at once.

## Shared Doctrine References
- `skills/shared/wordpress/execution-decision-tree.md`
- `skills/shared/wordpress/api-first-safe-write-protocol.md`
- `skills/shared/wordpress/verification-ladder.md`
- `skills/shared/wordpress/cache-plugin-gotchas-matrix.md`
- `skills/shared/wordpress/rollback-recovery-protocol.md`


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
- Homepage, landing page, service page, or funnel changes inside WordPress
- Content deployments that affect routing, templates, CTAs, forms, offers, or lead capture
- Plugin/theme configuration work tied to conversions or growth outcomes
- Blog/article publishing where structure, formatting, internal modules, and verification matter
- Coordinated page-builder/template/content changes across one site
- Multi-step WordPress work where API writes must be tied to live-path verification


## Do NOT Use For
- Pure API CRUD and endpoint-specific WordPress work → `wp-rest-api-mastery`
- Dedicated performance, cache, and Core Web Vitals investigation → `wordpress-performance`
- Failure-led diagnosis when you do not yet know if the issue is content, routing, cache, template, or plugin breakage → `wp-error-recovery`
- Non-WordPress external integrations as the main task → `api-integration-builder`

## Inputs Required
1. Target site, environment, and exact asset(s) in scope
2. Access paths available: REST, WP-CLI, filesystem, admin UI, plugin UI
3. Current money path or growth objective being protected/improved
4. Constraints: preserve SEO/routing/data, no downtime, no checkout/lead-flow breakage
5. Success criteria with live verification checkpoints

## Triage Protocol
1. Define the business-critical path affected: lead capture, CTA click, booking, opt-in, service inquiry, checkout, or content discovery.
2. Map the implementation surface: post/page/CPT, template, theme area, snippet/plugin, form, CRM hook, or cache layer.
3. Read current state before editing anything.
4. Check for hidden ownership layers: Elementor, Kadence, theme template, code-snippet plugin, form plugin, cache/plugin rewrites.
5. Decide the safest execution path: REST first, WP-CLI second, browser/admin only when necessary.
6. Define rollback and verification before mutating production.

## Core Framework

### 1. Growth-Surface Classification
Classify the work before acting:
- **Content layer**: copy, layout, blocks, media, internal modules
- **Template layer**: page template, header/footer, theme builder, archive/single template
- **Behavior layer**: forms, scripts, redirects, snippets, CTA behavior
- **Trust layer**: page integrity, social/meta output, visible proof, styling coherence
- **Money-path layer**: opt-in, inquiry, booking, checkout, delivery confirmation

### 2. Execution Order
1. Read current state
2. Identify the controlling layer
3. Prepare the full change set
4. Apply a minimal coherent set of writes
5. Verify the intended user path live
6. Purge or bypass cache only if verification indicates stale output

### 3. Decision Rules
#### Use REST API when
- the object is exposed and the change is CRUD/meta/taxonomy/content safe
- verification can happen quickly through GET + live route

#### Use WP-CLI when
- plugin/theme data is not reliably exposed in REST
- bulk operations or direct inspection are materially faster
- rollback precision matters

#### Use admin UI/browser when
- the controlling system is UI-only
- nonce-heavy configuration pages or visual builders own the actual state
- REST/CLI cannot safely express the intended change

## Verification Ladder
1. **Save verified** — API/CLI/UI reports success
2. **State verified** — fresh read shows intended values
3. **Route verified** — target URL resolves to intended object/template
4. **Experience verified** — human path works: CTA, form, content block, booking step, etc.
5. **After-effects verified** — cache/social head/meta/plugin side effects acceptable

## Failure Classification
- **Content-layer failure**: content missing, corrupted, wrong blocks, broken shortcodes
- **Template-layer failure**: blank areas, wrong headers/footers, builder template masking content
- **Behavior-layer failure**: CTA/form/script/snippet/redirect does not execute
- **Routing-layer failure**: wrong object serves URL, slug conflict, canonical mismatch
- **Cache-layer failure**: DB and live disagree
- **Integration-layer failure**: form submit works but downstream CRM/email/redirect path fails

## Batch Patterns
### Single-Site Batch
- Batch by site, not by task type across sites
- Verify first 3 items before full rollout
- Stop on unknown errors above 10%
- Re-verify business-critical pages, not just arbitrary samples

### Portfolio Work
- Finish one site’s change + verification loop before switching sites
- Reuse shared payload patterns but do not assume plugin parity across sites
- Record site-specific quirks to references or memory when discovered

## Rollback Discipline
- Snapshot original content/template/meta before any structural mutation
- For growth-critical pages, preserve both data rollback and route rollback
- If a change touches forms/snippets/templates and live behavior regresses, roll back first, then diagnose
- Escalate to `wp-error-recovery` if the controlling layer is ambiguous after first-pass checks

## Performance Optimizations
### Speed Multipliers
- Apply `../api-efficiency-protocol.md`
- Read minimum decisive data first
- Reuse known site/plugin maps within the session
- Batch reads, then writes
- Prefer one clean publish/update over multiple iterative production edits
- Verify the smallest decisive user path first

## Output Contract
**Artifact**: Completed WordPress growth change or rollout plan with protected rollback path
**Evidence**: State proof plus live-path proof on the user-facing route that matters
**Decision**: Shipped, blocked, rolled back, or escalated with reason
**Next**: Monitor, validate downstream delivery, or queue adjacent growth improvements

## Anti-Patterns
- ❌ Treating WordPress like pure content storage when the real owner is a template/plugin/builder
- ❌ Declaring success from admin/API feedback without testing the real user path
- ❌ Editing production copy/templates repeatedly instead of preparing one coherent final state
- ❌ Flushing every cache layer before confirming a cache problem exists
- ❌ Solving a trust/conversion problem with technical edits that ignore the money path
- ❌ Switching sites mid-operation and losing rollback/context clarity

## References
- `references/common-wordpress-money-paths.md`
- `references/operational-traps.md`
- `references/template-troubleshooting.md`
- `references/error-patterns.md`

## Self-Critique Scorecard (/25)
1. **Triage** (1-5): Did I identify the controlling layer and business-critical path correctly?
2. **Execution** (1-5): Was the change coherent, efficient, and minimal?
3. **Verification** (1-5): Did I verify the real user path, not just the save state?
4. **Rollback** (1-5): Could I reverse quickly without making the site worse?
5. **Learning** (1-5): Did I capture useful site/plugin/theme quirks for reuse?

**Target: 22+/25**
