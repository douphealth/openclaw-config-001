---
name: wordpress-growth-ops
description: Enterprise WordPress growth operations. Covers REST API mastery, content publishing, theme/plugin management, CSS/JS injection, homepage deployment, blog optimization, conversion path hardening, auto-verification, error recovery, and self-improving execution. Use when a WordPress site needs growth work crossing content, design, plugins, publishing, conversion paths, or verification. NOT for: server infra (→infrastructure-ops), email setup (→email-marketing-engine), SEO auditing (→seo-audit-playbook).
---

# WordPress Growth Ops — Enterprise Autonomous Site Operations

## Purpose
Handle WordPress as a unified growth system: copy, design, plugins, publishing, conversion paths, verification, and autonomous error recovery. Every operation includes auto-verification, error pattern learning, and self-critique before claiming completion.

## When to Use
- Homepage redesigns and full-page deployments
- Blog post formatting, optimization, and SEO hardening
- Conversion path improvements (lead capture, checkout, CTAs)
- Plugin/theme conflicts affecting monetization
- CSS/JS injection and style overrides
- Content publishing and batch operations
- Site-wide template and layout changes
- WordPress troubleshooting and repair
- Multi-site portfolio operations

**Do NOT use for:** Server infrastructure (→`infrastructure-ops`), email marketing setup (→`email-marketing-engine`), SEO auditing (→`seo-audit-playbook`), general copywriting (→`conversion-copywriting`), API integrations (→`api-integration-builder`).

## Compatibility
- WordPress 6.9+ (REST API, WP-CLI, Application Passwords)
- PHP 8.0+ recommended
- WP-CLI preferred for backend operations
- Browser automation only when REST API insufficient

## Inputs Required (Pre-Flight)
- Target site URL and WordPress root path
- Authentication method (app password, WP-CLI, file access)
- Environment: production/staging (assume production unless stated)
- Constraints: no downtime, preserve SEO, preserve data

## Triage Protocol
Before ANY operation:
1. Identify content type (page vs post vs CPT) via body class or REST API
2. Check current state via API (GET before POST/PUT/DELETE)
3. Verify credentials work (test API call)
4. Check for conflicts (slug duplicates, concurrent modifications)
5. Plan rollback (how to undo if something breaks)

## Speed Optimizations (Official Patterns)
- Use `_fields` parameter to fetch only needed data (80%+ payload reduction)
- Batch operations: `per_page=100` for list endpoints
- Parallel API calls via `concurrent.futures` (max 10/site)
- WP-CLI for bulk operations (faster than REST API for many tasks)
- Cache post/category maps in session (don't re-fetch)
- Use `wp db query` for direct DB operations when REST API is too slow

## Self-Critique Scorecard (/25)
1. **Triage** (1-5): Was current state fully understood before changes?
2. **Execution** (1-5): Was the operation clean and efficient?
3. **Verification** (1-5): Verified via API + live page + body class?
4. **Rollback** (1-5): Can changes be undone if issues found?
5. **Learning** (1-5): Were new patterns documented?

**Target: 22+/25**

## Error Recovery (Auto-Learning)
- Track error patterns per site (404s, auth failures, cache issues)
- After 2 failures on same operation → try alternative approach
- Log recurring fixes to memory/YYYY-MM-DD.md
- Update error-patterns.md reference when new patterns discovered

## Output Contract
**Artifact**: WordPress operation completed and verified
**Evidence**: API response proof + live page verification + body class check
**Decision**: Operation successful or error pattern identified with recovery path
**Next**: Log pattern, update memory, or schedule follow-up verification

## Architecture

```
Request → Classify → Execute → Verify → Learn
                    ↓          ↓        ↓
               REST API    Live      Error DB
               + Direct    Check     + Pattern
               File Access            Matching
```

Every operation follows: **Plan → Execute → Verify → Self-Critique → Log**

## WordPress REST API — Complete Reference

### Authentication Methods
```bash
# App Password (preferred — REST API only)
AUTH=$(echo -n "user:xxxx xxxx xxxx xxxx xxxx xxxx" | base64)
curl -H "Authorization: Basic $AUTH" "https://site.com/wp-json/wp/v2/posts"

# Cookie auth (for wp-admin sessions — needed for certain endpoints)
# Not available via REST API — requires browser or wp-login.php POST
```

### Posts & Pages
```bash
# List posts (paginated, 10 per page)
GET /wp-json/wp/v2/posts?page=1&per_page=10

# Get single post
GET /wp-json/wp/v2/posts/{id}?_fields=id,title,content,status,template,categories

# Create/Update post
POST /wp-json/wp/v2/posts/{id}
{
  "title": "New Title",
  "content": "<!-- wp:html -->\n...content...\n<!-- /wp:html -->",
  "status": "publish",
  "categories": [1, 5],
  "template": "elementor_header_footer",
  "meta": {
    "_yoast_wpseo_metadesc": "Meta description",
    "_yoast_wpseo_focuskw": "focus keyword"
  }
}

# Trash (soft delete)
DELETE /wp-json/wp/v2/posts/{id}

# Force delete (permanent)
DELETE /wp-json/wp/v2/posts/{id}?force=true

# Pages use /wp-json/wp/v2/pages/ endpoint (same structure)
```

### Media Upload
```bash
# Upload file
curl -X POST -H "Authorization: Basic $AUTH" \
  -H "Content-Disposition: attachment; filename=image.jpg" \
  -H "Content-Type: image/jpeg" \
  --data-binary @image.jpg \
  "https://site.com/wp-json/wp/v2/media"

# CRITICAL: Never upload .html files — WordPress corrupts them with wpautop
# Use application/octet-stream or direct filesystem upload for HTML

# List media
GET /wp-json/wp/v2/media?per_page=100&media_type=image
```

### Taxonomies (Categories/Tags)
```bash
# List categories
GET /wp-json/wp/v2/categories?per_page=100

# Update category (name, slug, meta)
POST /wp-json/wp/v2/categories/{id}
{
  "name": "New Name",
  "slug": "new-slug",
  "meta": {
    "_yoast_wpseo_metadesc": "Category meta description"
  }
}
```

### WordPress Settings
```bash
# Get settings
GET /wp-json/wp/v2/settings

# Update settings
POST /wp-json/wp/v2/settings
{
  "title": "Site Title",
  "description": "Tagline",
  "permalink_structure": "/%postname%/"
}
```

### Elementor
```bash
# Elementor data stored in post meta: _elementor_data
# WARNING: Complex JSON structure — handle with care

# Get Elementor data
GET /wp-json/wp/v2/posts/{id} → check meta._elementor_data

# Elementor templates
GET /wp-json/wp/v2/elementor_library/{id}
```

### Yoast SEO via REST API
```bash
# Update Yoast settings
POST /wp-json/yoast/v1/configuration
{"noindex-author-wpseo": true}

# Update post meta
POST /wp-json/wp/v2/posts/{id}
{
  "meta": {
    "_yoast_wpseo_metadesc": "description",
    "_yoast_wpseo_focuskw": "keyword",
    "_yoast_wpseo_noindex": ""
  }
}
```

### Code Snippets Plugin
```bash
# List snippets
GET /wp-json/wp/v2/wpcode-snippets

# Create/Update snippet (WORKS — different storage from WPCode)
POST /wp-json/wp/v2/wpcode-snippets
{
  "title": "Snippet Name",
  "content": "/* CSS or JS code */",
  "status": "publish",
  "wpcode_type": "php"  # or "css", "js", "html"
}
```

## Critical WordPress Gotchas (Lessons Learned)

### Content Rendering
1. **wpautop()** — Wraps bare text in `<p>`, adds `<br>` on double newlines. Breaks CSS in `<style>` blocks and JS in `<script>` tags.
2. **`<!-- wp:html -->` block** — Prevents wpautop for enclosed content BUT strips ALL `<p>` tags from inside. Use only for self-contained HTML, not mixed content.
3. **`<script>` tags stripped** — WordPress REST API `wp_filter_post_kses` removes `<script>` tags from post content. Use Code Snippets plugin or mu-plugins instead.
4. **`<style>` block corruption** — wpautop injects `<p>`, `</p>`, `<br/>` inside style blocks. Must strip artifacts before deploying.
5. **Application passwords** — Work for REST API Basic Auth ONLY. Cannot use for wp-login.php form submission.
6. **`post_content` corruption** — If `content.raw` is 0 chars but `content.rendered` has content, another plugin is providing the content. Always check raw field for database integrity.

### Routing & Templates
7. **Pages beat Posts** — If a PAGE and POST share the same slug, WordPress routes to the PAGE. Even trashed pages can block routes.
8. **Trash ≠ Delete** — Trashed content still exists in DB and can still match URL routes. Force-delete to fully remove.
9. **`elementor_header_footer` template** — Only renders header + footer, NO content area. Appears blank if used incorrectly.
10. **Body class detection** — `page-id-{N}` = serving a page, `postid-{N}` = serving a post. Always check when debugging routing issues.
11. **Permalink flush** — After slug/template changes, rewrite rules may need flushing. Update permalink settings in WP admin.

### Theme & CSS
12. **Never embed CSS in page content `<style>` tags** — wpautop() wraps CSS rules in `<p>` tags, breaking everything.
13. **CSS injection via `<script>`** — Create `<style>` element via JS: `<script>(function(){var s=document.createElement("style");s.textContent="CSS";document.head.appendChild(s)})();</script>`
14. **Theme CSS battles** — GeneratePress has 13+ `body{}` declarations. Don't fight themes with overrides — replace entire document with `document.write()` + base64.
15. **`document.write()` with base64** — Most reliable full-page replacement. WP-safe (only `[A-Za-z0-9+/=]`), zero theme interference.

### Performance & Caching
16. **PhastPress** — HTML rewriter (not standard page cache). Changes may require manual purge.
17. **Cloudflare** — Edge cache. Add `?v=timestamp` for verification. Purge via CF API for immediate updates.
18. **LiteSpeed Cache** — Server-level cache. Purge via plugin settings or REST API if available.

## Auto-Verification Protocol

Every WordPress operation MUST pass verification before claiming completion:

### Content Operations
```
1. GET the post/page via REST API
2. Verify content.raw has expected length (> 0 chars)
3. Verify no wpautop artifacts in content.rendered
4. Fetch live page, check content appears between header/footer
5. Check body class matches expected content type (post vs page)
```

### Style/Template Operations
```
1. Verify template field is correct
2. Check body classes match expected template
3. Verify no CSS conflicts (theme CSS overriding injected styles)
4. Check mobile responsiveness via readability extraction
```

### Full Verification Script
```bash
verify_wp_page() {
    local site="$1" post_id="$2" expected_content="$3"
    local auth="$4"
    
    # 1. Check DB content
    local raw_len=$(curl -s -u "$auth" "$site/wp-json/wp/v2/posts/$post_id" | \
        python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d['content']['raw']))")
    
    # 2. Check live page
    local page_size=$(curl -s -o /dev/null -w "%{size_download}" "$site/?p=$post_id")
    
    # 3. Report
    if [ "$raw_len" -gt 0 ] && [ "$page_size" -gt 1000 ]; then
        echo "✅ VERIFIED: raw=$raw_len, live=${page_size}B"
        return 0
    else
        echo "❌ FAILED: raw=$raw_len, live=${page_size}B"
        return 1
    fi
}
```

## Error Recovery Patterns

### Pattern 1: Content Wiped (raw = 0)
```
Symptom: content.raw = 0, content.rendered = N chars
Cause: Batch operation corrupted post_content field
Recovery: Restore from rendered field
Action: POST /wp-json/wp/v2/posts/{id} with {"content": "<rendered content>"}
Verify: GET post, confirm raw > 0
```

### Pattern 2: Slug Conflict (wrong content served)
```
Symptom: Live page shows wrong content or blank
Cause: PAGE and POST share same slug
Detection: Body class shows page-id-N instead of postid-N
Recovery: Force-delete conflicting page
Action: DELETE /wp-json/wp/v2/pages/{id}?force=true
Verify: Check body class on live page
```

### Pattern 3: Template Blocking Content
```
Symptom: Page blank between header/footer
Cause: elementor_header_footer template (no content area)
Detection: Body shows page-template-elementor_header_footer
Recovery: Change template or force-delete page to serve post
Action: POST /wp-json/wp/v2/pages/{id} {"template": ""} or DELETE page
Verify: Check live page renders content
```

### Pattern 4: wpautop Artifacts in Style Blocks
```
Symptom: CSS broken, <p> tags inside <style>
Cause: wpautop() ran before content was saved with raw HTML
Detection: <p> or <br/> inside <style> blocks
Recovery: Extract style blocks, strip artifacts, re-embed
Action: Python script to clean and redeploy
Verify: Check style blocks have 0 artifacts after fix
```

## Batch Operations Protocol

For operations affecting multiple posts/pages:

### Pre-Batch
1. Scan total count of affected items
2. Estimate time (0.5s per item for simple REST API operations)
3. Create backup/rollback plan
4. Set rate limit (10 items per API page, pause 0.5s between pages)

### During Batch
1. Track progress: items completed / total
2. Log errors immediately, don't continue on critical failures
3. Pause if error rate > 10%
4. Verify first 3 items before continuing with rest

### Post-Batch
1. Sample verification (check 5% of affected items)
2. Report: total changed, errors, skipped
3. Update ops log with results

## Self-Critique Protocol

Before declaring any WordPress operation complete, run self-critique:

```markdown
## Self-Critique: [Operation]

1. **Did I verify the live page?** (Not just the API response)
2. **Did I check the correct content type?** (Post vs Page)
3. **Did I check for slug conflicts?** (Same slug on different content types)
4. **Did I verify on mobile viewport?** (responsive rendering)
5. **Did I check for caching issues?** (PhastPress, Cloudflare, LiteSpeed)
6. **Did I verify money path still works?** (CTAs, forms, checkout)
7. **Did I check for side effects?** (Other pages affected by template changes)
8. **Is my evidence solid?** (API response + live page + body class check)
```

If ANY answer is "no" → Fix it before claiming completion.

## Output Contract
**Artifact**: WordPress operation completed and verified
**Evidence**: API response proof + live page verification + body class check
**Decision**: Operation successful or error pattern identified with recovery path
**Next**: Monitor for 24h if critical operation, or log pattern for future learning

## Performance Optimizations

### Speed Multipliers
- **Always use `_fields` parameter** — fetch only what you need, reduces payload 80%+
- **Parallel API calls** — use `concurrent.futures` for independent operations (max 10/site)
- **Batch by site** — never context-switch mid-operation
- **Pre-fetch auth** — validate credentials before starting work
- **Cache category/post maps** — don't re-fetch data already available in session

### WP-CLI Speed Patterns
- `wp post list --field=ID` for fast ID-only queries
- `wp post meta get/update` for bulk meta operations
- `wp db query "SELECT..."` for complex data operations
- `wp cache flush` after major content changes
- `wp rewrite flush` after permalink changes
- `wp search-replace` for URL migrations (faster than REST API)

### Self-Critique Scorecard (/25)
1. **Functionality** (1-5): Does it work perfectly?
2. **Quality** (1-5): Enterprise-grade?
3. **Verification** (1-5): Verified via API + live + visual?
4. **Speed** (1-5): Optimal execution?
5. **Learning** (1-5): Patterns documented?

**Target: 22+/25**

### Auto-Check
- [ ] Pre-flight checks completed
- [ ] Verified via multiple methods
- [ ] Anti-patterns avoided
- [ ] Score logged to memory

### Homepage Deployment Anti-Patterns (LESSONS LEARNED)
- ❌ **NEVER put full HTML document (DOCTYPE/head/body) in WP page content** — causes nested documents
- ❌ **NEVER use `document.write()` base64 on themes that process meta descriptions from content** — script gets trapped in meta tags
- ✅ **Always use scoped CSS** (prefix all classes with site-specific prefix like `.mgg-`, `.ph-`, `.mw-`)
- ✅ **Use `all:initial` on container** to reset theme styles
- ✅ **iframe approach is most reliable** for standalone HTML in WP — works across all themes
- ✅ **`<!-- wp:html -->` Gutenberg block** prevents wpautop from processing content

### Verified Patterns (Use These)
- **Scoped HTML**: `<div class="PREFIX">` + `all:initial` + prefixed CSS classes → zero theme conflicts
- **iframe**: `<script>body.innerHTML='';iframe=document.createElement('iframe');iframe.src='...'</script>` → works on all themes
- **document.write()**: Only when meta description won't trap the script — test first
- **Media upload**: `application/octet-stream` MIME for binary files, `text/html` corrupted by WP

## Scripts
- `scripts/wp-content-fix.py` — Fix wpautop artifacts in style blocks
- `scripts/wp-batch-update.py` — Batch post/page updates with verification
- `scripts/wp-verify.py` — Full verification of WordPress content operations
- `scripts/wp-slug-check.py` — Check for slug conflicts across content types

## References
- `references/rest-api-complete.md` — Full REST API endpoint reference
- `references/error-patterns.md` — Known error patterns and recovery procedures
- `references/template-troubleshooting.md` — Template and theme debugging guide
- `references/performance-caching.md` — Cache management for each platform
- `references/security-hardening.md` — WordPress security best practices
