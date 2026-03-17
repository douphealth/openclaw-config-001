---
name: wp-rest-api-mastery
description: "Enterprise WordPress REST API reference and operations. Use when performing CRUD on posts/pages/media, managing categories/tags, handling meta fields (Yoast, custom), uploading media, managing settings, working with Gutenberg blocks, Kadence elements, WPCode blocks, FluentCRM integration, batch operations, or debugging REST API errors. Covers authentication, error patterns, speed optimizations, and verification protocols."
---

# WordPress REST API — Master Reference

## When to Use

Use this skill when you need to:

- Create, read, update, or delete posts, pages, or custom post types via REST API
- Upload media files (images, HTML, binary)
- Manage categories, tags, and taxonomy terms
- Read or update WordPress settings
- Handle meta fields: Yoast SEO, custom fields, Elementor data
- Work with Gutenberg blocks (especially `wp:html` for raw HTML)
- Manage Kadence elements, WPCode blocks, or code injection
- Integrate with FluentCRM (contacts, sequences, lists)
- Batch operations across multiple posts/pages/sites
- Debug REST API errors: 401/403/404, content corruption, slug conflicts
- Verify deployments (API response + live page + body class)

**Do NOT use for:** Server infrastructure (→`infrastructure-ops`), email marketing setup (→`email-marketing-engine`), SEO auditing (→`seo-audit-playbook`), on-page SEO (→`seo-on-page`).

## Inputs Required

- **Site URL** and credentials (from `.secrets/*.access.env`)
- **Post/Page ID** (if editing existing content)
- **Content** to publish or update
- **Authentication mode** (Application Passwords preferred for external clients)

## Authentication

```bash
# Application Passwords — preferred for REST API (Basic auth, base64)
AUTH=$(echo -n "username:xxxx xxxx xxxx xxxx xxxx xxxx" | base64)
curl -s -H "Authorization: Basic $AUTH" "https://site.com/wp-json/wp/v2/posts"

# Quick one-liner (no base64 variable needed)
curl -s -u "username:xxxx xxxx xxxx xxxx xxxx xxxx" "https://site.com/wp-json/wp/v2/posts"

# Cookie auth — only works for wp-admin sessions (browser-based)
# NOT available for external API calls via curl/scripts
```

**Critical:** Application passwords work for REST API Basic Auth ONLY. Cannot use for `wp-login.php` form submission.

## Posts & Pages CRUD

### List posts/pages
```bash
# Fetch only what you need (80% payload reduction)
GET /wp-json/wp/v2/posts?_fields=id,title,content,status,date,slug,template,categories,meta&per_page=100

# Pages use same structure
GET /wp-json/wp/v2/pages?_fields=id,title,content,status,slug,template&per_page=100
```

### Get single post/page
```bash
GET /wp-json/wp/v2/posts/{id}?_fields=id,title,content.raw,content.rendered,status,template,categories,meta
GET /wp-json/wp/v2/pages/{id}?_fields=id,title,content.raw,content.rendered,status,template,meta
```

### Create/Update post/page
```bash
POST /wp-json/wp/v2/posts/{id}
{
  "title": "Post Title",
  "content": "<!-- wp:html -->\n<pure HTML here, wpautop bypassed</p>\n<!-- /wp:html -->",
  "status": "publish",
  "categories": [1, 5],
  "tags": [3, 7],
  "template": "elementor_header_footer",
  "meta": {
    "_yoast_wpseo_metadesc": "Meta description",
    "_yoast_wpseo_focuskw": "focus keyword",
    "_yoast_wpseo_title": "Custom Title"
  }
}
```

### Delete / Trash
```bash
# Soft delete (trash) — recoverable
DELETE /wp-json/wp/v2/posts/{id}

# Force delete (permanent) — use when slug conflicts need clearing
DELETE /wp-json/wp/v2/posts/{id}?force=true
```

### Pages endpoint
Same structure as posts: `/wp-json/wp/v2/pages/{id}`

## Gutenberg Blocks — The `wp:html` Pattern

```html
<!-- wp:html -->
<style>.my-class { color: red; }</style>
<div class="my-class">Raw HTML without wpautop corruption</div>
<script>console.log('stripped by kses — see below')</script>
<!-- /wp:html -->
```

**Key rules:**
- `<!-- wp:html -->` block prevents `wpautop()` from wrapping content in `<p>` tags
- BUT it strips ALL `<p>` tags from inside the block (use `<div>` instead)
- `<script>` tags are STILL stripped by `wp_filter_post_kses` — use Code Snippets plugin or mu-plugins for JS
- For mixed content (HTML + paragraphs), use multiple `wp:html` blocks separated by `wp:paragraph` blocks

## Media Upload

```bash
# Upload image/file
curl -X POST -u "user:pass" \
  -H "Content-Disposition: attachment; filename=image.jpg" \
  -H "Content-Type: image/jpeg" \
  --data-binary @image.jpg \
  "https://site.com/wp-json/wp/v2/media"

# Upload HTML or binary files — MUST use application/octet-stream
curl -X POST -u "user:pass" \
  -H "Content-Disposition: attachment; filename=file.html" \
  -H "Content-Type: application/octet-stream" \
  --data-binary @file.html \
  "https://site.com/wp-json/wp/v2/media"
```

**Critical:** Never upload `.html` files with `text/html` MIME — WordPress corrupts them with `wpautop`. Always use `application/octet-stream`.

```bash
# List media
GET /wp-json/wp/v2/media?per_page=100&media_type=image&_fields=id,source_url,title,media_type,mime_type
```

## Categories & Tags

```bash
# List all categories
GET /wp-json/wp/v2/categories?per_page=100&_fields=id,name,slug,count

# Create category
POST /wp-json/wp/v2/categories
{"name": "New Category", "slug": "new-category"}

# Update category
POST /wp-json/wp/v2/categories/{id}
{"name": "Updated Name", "meta": {"_yoast_wpseo_metadesc": "Category description"}}

# Tags — same structure
GET /wp-json/wp/v2/tags?per_page=100
POST /wp-json/wp/v2/tags
```

## Settings API

```bash
# Get all settings
GET /wp-json/wp/v2/settings

# Update settings
POST /wp-json/wp/v2/settings
{
  "title": "Site Title",
  "description": "Site Tagline",
  "permalink_structure": "/%postname%/",
  "default_category": 1,
  "posts_per_page": 10
}
```

## Meta Fields

### Yoast SEO
```bash
POST /wp-json/wp/v2/posts/{id}
{
  "meta": {
    "_yoast_wpseo_metadesc": "SEO meta description",
    "_yoast_wpseo_focuskw": "primary keyword",
    "_yoast_wpseo_title": "Custom SEO title",
    "_yoast_wpseo_noindex": ""  # empty = index, "1" = noindex
  }
}
```

### Custom fields
```bash
# Register with show_in_rest in plugin/theme, then:
POST /wp-json/wp/v2/posts/{id}
{
  "meta": {
    "my_custom_field": "value"
  }
}
```

### Elementor content
**WARNING:** Elementor stores content in postmeta `_elementor_data`, NOT in `post_content`.
```bash
# Read Elementor data
GET /wp-json/wp/v2/posts/{id} → meta._elementor_data (complex JSON)

# Elementor library templates
GET /wp-json/wp/v2/elementor_library/{id}
```

## WPCode Blocks

```bash
# WPCode blocks API (for CSS/JS injection — NOT PHP snippets)
GET /wp-json/wp/v2/wpcode-blocks?per_page=100

# Create CSS/JS block
POST /wp-json/wp/v2/wpcode-blocks
{
  "title": "My Custom CSS",
  "content": ".my-class { color: red; }",
  "status": "publish",
  "wpcode_type": "css"  # or "js", "html"
}

# ⚠️ WPCode Pro PHP snippets are stored in a CUSTOM TABLE, NOT accessible
# via wpcode-blocks endpoint. Use WP-CLI or admin UI for PHP snippets.
```

## Kadence Elements

```bash
# Kadence uses custom post type
GET /wp-json/wp/v2/kadence_elements?per_page=100

# Create/update element
POST /wp-json/wp/v2/kadence_elements/{id}
{
  "title": "Element Title",
  "content": "<!-- wp:html -->...<!-- /wp:html -->",
  "status": "publish"
}
```

## FluentCRM Integration

```bash
# List contacts
GET /wp-json/fluent-crm/v2/subscribers?per_page=100

# Add contact to sequence (RELIABLE path)
POST /wp-json/fluent-crm/v2/sequences/{sequence_id}/subscribers
{
  "subscriber_ids": [123, 456]
}

# ⚠️ subscribers/do-bulk-action with add_to_email_sequence = BROKEN via REST
# Always use the sequences/{id}/subscribers endpoint instead

# Get lists
GET /wp-json/fluent-crm/v2/lists

# Add contact to list
POST /wp-json/fluent-crm/v2/subscribers
{
  "email": "user@example.com",
  "first_name": "John",
  "lists": [1]
}
```

## Batch Operations

### With concurrent.futures (Python)
```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

AUTH = ("user", "xxxx xxxx xxxx xxxx xxxx xxxx")
BASE = "https://site.com/wp-json/wp/v2"
MAX_WORKERS = 10  # max 10 parallel calls per site

def update_post(post_id, data):
    resp = requests.post(f"{BASE}/posts/{post_id}", json=data, auth=AUTH)
    resp.raise_for_status()
    return post_id, resp.json()

post_ids = [1, 2, 3, 4, 5]  # your post IDs
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
    futures = {pool.submit(update_post, pid, {"title": "Updated"}): pid for pid in post_ids}
    for f in as_completed(futures):
        pid, result = f.result()
        print(f"✅ Post {pid}: {result['title']['rendered']}")
```

### Batch protocol
1. **Pre-batch:** Scan count, estimate time (0.5s/item), set rate limit (10/page, 0.5s pause between pages)
2. **During:** Track progress, log errors immediately, pause if error rate > 10%
3. **Post-batch:** Sample 5% verification, report totals, log to memory

## Speed Optimizations

| Optimization | Impact | How |
|---|---|---|
| `_fields` parameter | 80% payload reduction | `?_fields=id,title,content.raw` |
| `per_page=100` | 10x fewer requests | `?per_page=100` (capped at 100) |
| Parallel calls | 5-10x speedup | `concurrent.futures`, max 10/site |
| Cache session data | Avoid re-fetching | Store category/post maps in session |
| Pre-fetch auth | Fail fast | Validate credentials before batch |

## Error Patterns & Recovery

### 1. wpautop corruption of HTML
```
Symptom: <p> and <br> tags injected inside <style> or raw HTML
Cause: wpautop() runs on content not wrapped in wp:html block
Recovery: Wrap content in <!-- wp:html -->...<!-- /wp:html -->
Fix script: scripts/wp-content-fix.py strips artifacts
```

### 2. Script tag stripping
```
Symptom: <script> tags removed from post content
Cause: wp_filter_post_kses sanitizes post_content
Recovery: Use Code Snippets plugin, mu-plugin, or inject via JS in wp:html block
Workaround: <script>(function(){var s=document.createElement("script");s.src="...";document.head.appendChild(s)})()</script>
```

### 3. BOM issues (utf-8-sig decoding)
```
Symptom: Content has invisible BOM character at start
Cause: File saved with UTF-8 BOM encoding
Recovery: Decode with utf-8-sig in Python: content.encode().decode('utf-8-sig')
```

### 4. wpcode-blocks ≠ WPCode Pro PHP snippets
```
Symptom: Can create blocks via API but PHP snippets don't execute
Cause: WPCode Pro stores PHP in custom database table, not post type
Recovery: Use WP-CLI or admin UI for PHP snippets; API only works for CSS/JS/HTML
```

### 5. Slug conflicts (pages vs posts)
```
Symptom: Wrong content served, or blank page
Cause: PAGE and POST share same slug — pages always win
Detection: Body class shows page-id-N instead of postid-N
Recovery: Force-delete conflicting page: DELETE /wp-json/wp/v2/pages/{id}?force=true
```

### 6. Elementor content in postmeta
```
Symptom: post_content is empty but page has content
Cause: Elementor stores content in _elementor_data meta, not post_content
Recovery: Check meta._elementor_data field, not content.raw
```

## Verification Protocol

Every operation MUST pass all three checks:

```bash
# 1. API Response Check
curl -s -u "user:pass" "https://site.com/wp-json/wp/v2/posts/{id}?_fields=id,title,content.raw,status"

# 2. Live Page Check
curl -s -o /dev/null -w "%{size_download}" "https://site.com/?p={id}"
# Size > 1000 bytes = content rendering

# 3. Body Class Check (debug routing)
curl -s "https://site.com/?p={id}" | grep -o 'class="[^"]*"' | head -1
# page-id-* = serving a page, postid-* = serving a post
```

### Verification helper (Python)
```python
def verify_wp_page(site, post_id, auth):
    import requests
    # API check
    r = requests.get(f"{site}/wp-json/wp/v2/posts/{post_id}?_fields=id,content.raw", auth=auth)
    raw_len = len(r.json().get("content", {}).get("raw", ""))
    # Live check
    live = requests.get(f"{site}/?p={post_id}")
    live_size = len(live.text)
    # Body class
    body_class = "unknown"
    for line in live.text.split("\n"):
        if "body" in line and "class=" in line:
            body_class = line
            break
    status = "✅" if raw_len > 0 and live_size > 1000 else "❌"
    print(f"{status} raw={raw_len}, live={live_size}B, body={body_class[:80]}")
    return raw_len > 0 and live_size > 1000
```

## Homepage Deployment — Proven Patterns

### ✅ What works
- **iframe approach:** JS clears body, creates `position:fixed` iframe → works on ALL themes
- **Scoped HTML:** `<div class="PREFIX">` + `all:initial` + prefixed CSS → zero conflicts
- **`<!-- wp:html -->` block:** Prevents wpautop from processing raw HTML
- **CSS injection via script:** `<script>(function(){var s=document.createElement("style");s.textContent="CSS";document.head.appendChild(s)})()</script>`

### ❌ What NEVER works
- Full HTML document (DOCTYPE/head/body) in page content → nested documents
- `document.write()` with base64 → trapped in og:description meta tag
- `wp_redirect()` → changes URL to ugly path
- Meta refresh → client-side redirect
- HTML upload via WP media → corrupted by wpautop

### Theme-specific lessons
- **GeneratePress:** 13+ `body{}` declarations — use `all:initial` on container
- **Astra:** Scripts trapped in og:description meta tag from post content
- **Kadence:** Elementor content in postmeta, not content field
- **Twenty Twenty-Four:** `.entry-content` has conflicting CSS

## Blank Page Debugging Checklist

1. Check body class: `page-id-*` (page) vs `postid-*` (post) → wrong content type?
2. Check `content.raw` vs `content.rendered` → DB wiped?
3. Check template: `elementor_header_footer` = no content area
4. Check slug conflicts between pages and posts
5. Check for trash: trashed content still matches URL routes
6. Flush permalinks after slug/template changes

## Cache Purging

After content changes, purge:
- **PhastPress:** HTML rewriter — requires manual purge
- **Cloudflare:** Add `?v=timestamp` for verification, purge via CF API for immediate updates
- **LiteSpeed Cache:** Via plugin settings or REST API if available
- **WordPress object cache:** `wp cache flush` via WP-CLI

## Self-Critique Scorecard (/25)

Before claiming any WP REST API operation complete:

| # | Criterion | Score |
|---|---|---|
| 1 | **Functionality** — Does it work perfectly? | /5 |
| 2 | **Quality** — Enterprise-grade execution? | /5 |
| 3 | **Verification** — API + live + body class checked? | /5 |
| 4 | **Speed** — Optimal execution (parallel, _fields, batched)? | /5 |
| 5 | **Learning** — New patterns documented to MEMORY.md? | /5 |

**Target: 22+/25**

### Auto-Check
- [ ] Pre-flight: credentials valid, target exists, rollback plan ready
- [ ] Verified via multiple methods (API response + live page + body class)
- [ ] Anti-patterns avoided (no full HTML docs, no bare `<script>`, no `document.write()` base64)
- [ ] Score logged to memory

## Quick Reference Card

```
Auth:       curl -u "user:pass" ...
Fields:     ?_fields=id,title,content.raw,status,meta
Batch:      ?per_page=100 (capped at 100)
HTML safe:  <!-- wp:html -->...<!-- /wp:html -->
No script:  Use Code Snippets plugin, NOT post_content
Media:      Content-Type: application/octet-stream for binary
Slug fix:   DELETE .../pages/{id}?force=true
Verify:     API → Live → Body Class → Self-Critique → Log
```
