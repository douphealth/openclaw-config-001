---
name: editorial-post-enhancement
description: Enterprise blog post audit and enhancement. Use when upgrading a published or draft article for stronger rankings, better readability, richer media, smarter internal links, stronger FAQ/design structure, and production-safe WordPress publishing.
---

# Editorial Post Enhancement

## Purpose
Upgrade an existing article into a stronger ranking and user-experience asset without breaking WordPress rendering, existing metadata, internal links, schema layers, or site templates. This skill covers editorial improvement plus production-safe publishing discipline.

For serious content programs, this skill should not just improve copy. It should sequence the work intelligently: audit first, identify the highest-value weaknesses, prepare a coherent replacement, validate the result, and leave enough state that the next run can continue through the backlog without rethinking the entire editorial strategy.

## Shared Doctrine References
- `skills/shared/seo-aeo-geo-superpowers.md`
- `skills/shared/seo-aeo-geo-checklist.md`
- `skills/shared/seo-aeo-geo-research-workflow.md`
- `skills/shared/seo-aeo-geo-scorecard.md`
- `skills/shared/premium-human-content-standard.md`
- `skills/shared/flagship-article-rebuild-standard.md`
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
- `skills/shared/autonomous-task-state-standard.md`
- `skills/shared/validation-gate-standard.md`
- `skills/shared/response-excellence-standard.md`
- `skills/shared/skill-efficiency-standard.md`

Default execution mode:
1. clarify/spec first if ambiguous
2. write a short plan before large execution
3. dispatch parallel workers for independent subtasks
4. review output for spec compliance and quality
5. verify in reality before claiming complete

## When to Use
- Improving an existing WordPress post that needs stronger rankings, depth, readability, or internal linking
- Reworking an article for clearer structure, better FAQ coverage, richer media, and stronger on-page SEO
- Refreshing older content while preserving live URL equity and production stability
- Enhancing editorial assets where publishing safety matters as much as the copy itself

## Do NOT Use For
- Net-new content strategy or topic planning (`content-strategy-planning` or `keyword-research-mastery`)
- Pure line editing with no structural/content upgrade (`copy-editing-sweeps`)
- Schema-only implementation with no editorial work (`schema-ops`)
- Raw WordPress REST/meta/media mechanics (`wp-rest-api-mastery`)

## Inputs Required
1. Target post ID or canonical URL
2. Environment and publication risk: draft, staging, or live production
3. Primary keyword or topic target
4. Access model: REST, WP-CLI, builder/plugin layer, media library
5. Constraints: preserve existing URL, schema, design system, affiliate links, author data, or ad placements

## Triage Protocol
1. Fetch current post state before editing, including content, important meta, taxonomy, and featured media
2. Identify the rendering model: classic editor, Gutenberg, shortcode-heavy, or page-builder-driven post
3. Check for existing SEO/schema/plugin layers before adding new ones
4. Capture rollback content and note any custom HTML or shortcode dependencies
5. Decide whether this is a light refresh, deep rewrite, or rebuild inside existing structure

## Core Framework
### 1. Audit before touching content
Check for weak headline structure, thin sections, stale entities, weak internal links, poor FAQ coverage, image gaps, fragile WordPress markup, slug/topic mismatch, CTA overload, low content-to-noise ratio, and whether the article is so weak that it needs a flagship rebuild rather than a refresh.

### 2. Preserve publish-safe structure
- Keep Gutenberg block comments intact
- Respect shortcode wrappers and reusable patterns
- Avoid injecting markup likely to be mangled by `wpautop`, sanitizers, or builder filters
- If custom HTML is needed, use patterns that match the site's actual editor/rendering constraints

### 3. Upgrade the content
Typical enhancement layers:
- stronger intro / TL;DR / quick-answer block near the top
- cleaner H2/H3 structure
- missing topic depth and entity coverage
- internal links distributed through the full article
- tables, FAQs, examples, and useful media
- stronger meta assets if this skill owns them for the task
- PAA-style question coverage for the target query family
- clearer quotable answer blocks for AI extraction
- fewer low-value visual interruptions and cleaner HTML flow
- stronger excerpt quality for search and AI surfaces
- snippet-length FAQ expansion, not one-line throwaway answers
- bolding of key entities on first meaningful use when it improves scanability
- cluster-correct related guides instead of loose adjacent-topic links
- explicit review of CTA overload and content-to-noise ratio
- References section with high-quality clickable resources where appropriate
- stronger premium HTML composition using safe modern callouts, summary cards, and better section rhythm

### 4. Handle WordPress publishing rigor
- Confirm whether Yoast/Rank Math/custom meta already controls title, description, schema, or breadcrumbs
- Do not create duplicate schema with editorial additions; route to `schema-ops` when schema work is substantial
- Verify image placement, alt text, and responsive behavior in rendered output
- Watch for builder/plugin conflicts, excerpt quirks, and auto-generated table-of-contents behavior

### 5. Verify live safely
For live posts, verify:
- rendered HTML and layout
- internal links and media
- meta/schema ownership boundaries
- mobile readability
- no broken shortcode/block output after publish
- whether visible title/excerpt/content improvements also propagate to the live search-facing layer or remain blocked behind a separate SEO-meta owner

### 6. Batch refresh pattern
For multiple posts:
- audit all targets first
- group by template/rendering type
- batch similar fixes
- verify samples from each pattern before rolling wider
- maintain per-post status markers and publish-validation rules so a fresh rerun can continue the queue cleanly

## Performance Optimizations
### Speed Multipliers
- Apply `skills/api-efficiency-protocol.md` for posts, media, taxonomy, and link-candidate fetches
- Fetch only decisive fields first, then enrich as needed
- Reuse proven HTML/content patterns already safe for the site's editor stack
- Separate research, drafting, and publishing passes to reduce accidental production mistakes
- For large refresh waves, batch by category/template and spot-check edge cases

## Output Contract
**Artifact**: Enhanced article with safer structure, stronger SEO/editorial quality, and publish-ready formatting
**Evidence**: Before/after summary plus rendered-output verification
**Decision**: Publish-ready / needs schema help / needs deeper WP implementation support
**Next**: Publish or hand off to `schema-ops`, `wp-rest-api-mastery`, or `auto-verification` as needed

For premium article work, include or explicitly decide:
- title tag
- meta description
- slug recommendation
- schema recommendations
- internal linking opportunities
- cluster-post opportunities where relevant

## Anti-Patterns
- ❌ Rewriting directly in production without capturing the original content
- ❌ Breaking Gutenberg, shortcode, or builder structure with pretty-but-fragile HTML
- ❌ Adding schema blindly when the SEO plugin already injects it
- ❌ Clumping all internal links or FAQs at the bottom with no editorial flow
- ❌ Treating editor content as final truth without checking rendered output
- ❌ Running wide post refreshes without grouping by template or verification pattern

## References
- `references/eeat-checklist.md`
- `references/faq-html-patterns.md`
- `references/html-pattern-library.md`
- `references/internal-linking-rules.md`
- `references/publish-readiness-checklist.md`
- `references/serp-optimization-guide.md`
- `skills/references/wp-live-ops-verification.md`

## Self-Critique Scorecard (/25)
1. **Triage** (1-5): Was the article's current rendering and SEO state understood first?
2. **Execution** (1-5): Was the enhancement materially better without overcomplicating the post?
3. **Verification** (1-5): Was rendered output checked after changes?
4. **Rollback** (1-5): Could the original post be restored safely?
5. **Learning** (1-5): Were reusable editorial/WP publishing patterns captured?

**Target: 22+/25**
