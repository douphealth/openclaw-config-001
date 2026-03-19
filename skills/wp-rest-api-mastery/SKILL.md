---
name: wp-rest-api-mastery
description: Enterprise WordPress REST API execution for posts, pages, media, taxonomies, settings, meta fields, plugin endpoints, batch updates, and REST debugging. Use when doing API-first WordPress CRUD, schema/meta updates, media operations, plugin-specific REST work, or high-volume batch execution. NOT for: broader site growth strategy (→ wordpress-growth-ops), recovery-led debugging when the failure class is unclear (→ wp-error-recovery), or performance investigations (→ wordpress-performance).
---

# WordPress REST API Mastery

## Purpose
Execute WordPress changes through the safest, fastest API-first path possible. This skill is the operating doctrine for REST-first CRUD, batch changes, meta handling, media, plugin endpoints, verification, rollback discipline, and failure classification when the API itself is the primary work surface.

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
- Creating, updating, deleting, or verifying posts, pages, media, users, terms, or settings via REST API
- Managing WordPress meta fields including Yoast and registered custom fields
- Working with Gutenberg block payloads, Kadence Elements, WPCode blocks, or plugin-specific endpoints
- Running batch content or taxonomy operations across many records
- Uploading media or files through API endpoints
- Diagnosing 400/401/403/404/409/5xx REST failures
- Verifying whether an API write actually reached the database and the live route


## Do NOT Use For
- Portfolio/site-level growth work spanning copy, templates, money paths, and UX decisions → `wordpress-growth-ops`
- Recovery work when the failure class is still unknown and could be routing/cache/template/theme/plugin related → `wp-error-recovery`
- Performance diagnosis, cache strategy, or Core Web Vitals work → `wordpress-performance`
- Infrastructure/server hardening or host-level access problems → `infrastructure-ops`

## Inputs Required
1. Target site, environment, and exact endpoint or content type
2. Authentication model (application password, cookie auth, wp-admin nonce, plugin auth, or WP-CLI fallback)
3. Current state from a GET before any write
4. Constraints: no downtime, preserve slugs/SEO/data, no irreversible deletes unless approved
5. Success criteria and rollback path

## Triage Protocol
1. Identify the object class: core post type, taxonomy, settings, media, plugin CPT, or plugin endpoint.
2. Confirm auth with the cheapest decisive request, ideally `/users/me` or a scoped GET.
3. Read current state with `_fields` and save decisive identifiers: `id`, `slug`, `status`, `template`, `meta`, `modified`.
4. Classify the intended write as safe patch, structural mutation, batch update, or destructive change.
5. Decide rollback before writing: previous JSON payload, cloned record, exported meta, or trash/restore path.
6. Define verification ladder: API write confirmation, fresh GET, live route check if front-end relevant, cache check if needed.

## Core Framework

### 1. Access + Endpoint Mapping
- Prefer application passwords for external automation.
- Prefer REST over browser automation.
- Prefer WP-CLI when the plugin endpoint is absent, custom tables are involved, or rollback needs DB-level precision.
- Treat plugin endpoints as separate products: validate exact route shape before assuming core WP semantics.

### 2. Read-Minimum, Write-Once
- Use `_fields=` on every discovery read.
- Use `per_page=100` for list operations.
- Build a complete patch locally, then send one coherent write instead of repeated production edits.
- For batches, read all targets first, then write in controlled waves.

### 3. Write Classes
#### Safe Patch
Examples: title/meta/category/status updates.
- Snapshot current values.
- Send minimal delta.
- Re-GET exact changed fields.

#### Structural Mutation
Examples: slug/template/content model changes, plugin config changes, homepage swaps.
- Snapshot full record.
- Check for routing/template/plugin side effects.
- Verify on live route, not just API.

#### Batch Mutation
Examples: 50+ post meta changes, taxonomy normalization, mass republishing.
- Pre-scan total scope.
- Dry-run candidate list.
- Write in batches of 10 max concurrent requests/site.
- Abort if hard-failure rate exceeds 10% or unknown failures repeat.

#### Destructive Change
Examples: force delete, slug-clearing deletes, settings resets.
- Require clear justification.
- Preserve recovery data.
- Prefer trash over force delete unless slug/routing conflict specifically requires permanent removal.

### 4. Verification Ladder
1. **Transport verified** — response code and JSON shape are sane.
2. **Persistence verified** — fresh GET shows the intended value.
3. **Render verified** — live page/API consumer reflects the change when applicable.
4. **Routing verified** — body class / canonical / permalink path matches intended object.
5. **Cache verified** — stale-cache ruled out if API and live disagree.

## Performance Optimizations
### Speed Multipliers
- Apply `skills/api-efficiency-protocol.md`
- Always use `_fields`
- Use `per_page=100` on list endpoints
- Reuse ID maps within session; do not re-fetch known objects
- Batch reads first, then writes
- Use `concurrent.futures` or equivalent with max 10 workers/site
- Prefer `HEAD`/small GETs for verification before large content fetches
- Prefer WP-CLI for custom-table plugins or mass operations where REST adds overhead

## Failure Classification
### Auth Failures
- **401**: bad/missing auth, wrong application password format, endpoint protected unexpectedly
- **403**: authenticated but blocked by capability, security plugin, Cloudflare/WAF, or endpoint policy

### Shape / Validation Failures
- **400**: malformed payload, unsupported field, bad JSON, invalid enum, missing required property
- **409-like behavior**: slug collision, state conflict, duplicate unique field, concurrent edit collision
- **422-like plugin behavior**: plugin-level validation failed even if WP core does not formally return 422

### Discovery Failures
- **404**: wrong endpoint, object missing, CPT not exposed in REST, plugin route disabled
- Empty list with 200: pagination/filter mismatch, wrong status filter, missing context

### Runtime Failures
- **5xx**: plugin fatal, server timeout, memory issue, upstream protection, custom callback crash
- Partial success in batch: treat as failure until verified target-by-target for the affected set

## Plugin / Theme-Specific Gotchas
- **Yoast**: meta keys only work when registered and exposed; distinguish post meta from Yoast indexables side effects.
- **Elementor**: visible content may live in `_elementor_data`, not `post_content`; avoid blind `content` edits.
- **Kadence**: templates/elements often use CPT/meta combinations; verify route and output context.
- **WPCode**: REST-accessible blocks are not the same as all executable snippets; PHP storage may live outside normal posts.
- **FluentCRM**: treat CRM routes as separate APIs; batch add/remove actions can differ from core WP conventions.
- **Themes**: theme template or page builder assignment can make a correct API write appear invisible on the front end.

## Batch Patterns
### Pre-Batch
- Fetch target universe and save it locally
- Build rollback artifact per record or per batch
- Run sample write on 1-3 records first
- Define stop conditions before starting

### During Batch
- Max 10 concurrent writes/site
- Separate hard failures from soft/stale-cache anomalies
- Stop immediately on unknown repeated failures, auth drift, or unexpected content loss
- Log successes/failures with IDs, slugs, and error class

### Post-Batch
- Verify 100% of failures and a sample of successes
- For structural changes, verify first 3, middle, and last 3 items live
- Record net counts: attempted / succeeded / failed / rolled back / pending manual review

## Rollback Discipline
- Always retain the last-known-good payload for anything non-trivial
- For content, snapshot `title`, `slug`, `status`, `template`, `content.raw`, important `meta`, and taxonomy IDs
- For settings, export current settings subset before mutation
- For destructive cleanup, document why trash is insufficient
- If verification fails and cause is unclear, stop and route to `wp-error-recovery`

## Output Contract
**Artifact**: Executed REST plan or completed API mutation with rollback data
**Evidence**: Request/response proof, fresh GET proof, and live verification when front-end relevant
**Decision**: Safe, blocked, partially complete, rolled back, or escalated
**Next**: Additional verification, cache purge, recovery routing, or follow-up batch wave

## Anti-Patterns
- ❌ Repeatedly patching production records instead of preparing one clean final payload
- ❌ Treating API 200 as success without a fresh GET
- ❌ Editing `post_content` on builder-managed content without checking builder meta
- ❌ Force deleting when trash would preserve recovery options
- ❌ Running large batches before a 1-3 item canary
- ❌ Assuming plugin REST routes behave like core endpoints
- ❌ Skipping live-route verification on slug, template, content, or homepage changes

## References
- `references/rest-decision-tree.md`
- `references/plugin-gotchas.md`
- `../api-efficiency-protocol.md`

## Self-Critique Scorecard (/25)
1. **Triage** (1-5): Did I classify endpoint/object/write type correctly before mutating?
2. **Execution** (1-5): Were reads minimal and writes coherent, fast, and safe?
3. **Verification** (1-5): Did I prove persistence and live effect where relevant?
4. **Rollback** (1-5): Could I restore the prior state quickly?
5. **Learning** (1-5): Did I capture any new endpoint/plugin behavior worth reusing?

**Target: 22+/25**
