# WordPress Error Patterns — Complete Reference

Auto-updated by `wordpress-autonomous-ops` error-tracker. Every pattern includes symptoms, cause, prevention, and auto-fix.

---

## EP-001: Slug Conflict (Page vs Post)
**Frequency:** 4 occurrences | **Severity:** CRITICAL | **Confidence:** 0.99

### Symptoms
- Page is blank between header/footer despite content in DB
- Body class shows `page-id-{N}` instead of `postid-{N}`
- URL resolves to wrong content type
- REST API shows correct content but live page is empty

### Root Cause
PAGE and POST share the same slug. WordPress URL routing prioritizes pages. Even trashed pages can block posts.

### Prevention
```python
# Before modifying content at a URL, ALWAYS check:
# 1. Is this a PAGE or POST?
# 2. Are there other content types with the same slug?
# Use wp-slug-check.py to scan for conflicts proactively
```

### Auto-Fix
```bash
# Force-delete the conflicting page
curl -X DELETE -u "$AUTH" "$SITE/wp-json/wp/v2/pages/{page_id}?force=true"
```

### Detection Script
```bash
python3 scripts/wp-slug-check.py --site "$SITE" --auth "$AUTH" --check-orphaned
```

---

## EP-002: wpautop Style Block Corruption
**Frequency:** 380+ occurrences | **Severity:** MEDIUM | **Confidence:** 0.95

### Symptoms
- CSS rules broken (selectors separated by `</p>` or `<br />`)
- Visual artifacts on page
- Theme styles not applying correctly
- `<p>` tags inside `<style>` blocks

### Root Cause
`wpautop()` runs on post content before saving. It wraps text in `<p>` tags, including CSS rules inside `<style>` blocks.

### Prevention
```html
<!-- WRONG: bare CSS in content -->
<style>
  .my-class { color: red; }
  <p>body { font-size: 16px; }</p> <!-- wpautop artifact -->
</style>

<!-- CORRECT: wrapped in wp:html block -->
<!-- wp:html -->
<style>
  .my-class { color: red; }
  body { font-size: 16px; }
</style>
<!-- /wp:html -->
```

### Auto-Fix
```bash
python3 scripts/wp-content-fix.py --site "$SITE" --auth "$AUTH" --scan --fix-all
```

---

## EP-003: post_content Wiped to 0
**Frequency:** 2 occurrences | **Severity:** CRITICAL | **Confidence:** 0.98

### Symptoms
- `content.raw` returns 0 chars
- `content.rendered` has data (from plugin cache or other source)
- Page appears completely blank
- No errors in WordPress debug log

### Root Cause
Batch operations or API errors can wipe `post_content` field while leaving post meta intact. The `rendered` field may still show data because a plugin (like PhastPress) serves cached content.

### Prevention
```python
# After every batch operation, verify raw content:
post = api.get(f"posts/{id}")
assert len(post['content']['raw']) > 0, "Content was wiped!"
```

### Auto-Fix
```python
# Restore from rendered field
api.post(f"posts/{id}", {"content": post['content']['rendered']})
```

---

## EP-004: Elementor Template Blocking Content
**Frequency:** 1 occurrence | **Severity:** HIGH | **Confidence:** 0.90

### Symptoms
- Page blank between header/footer
- `page-template-elementor_header_footer` in body class
- Page has content in DB but nothing renders
- Header and footer display correctly

### Root Cause
`elementor_header_footer` template only renders header + footer, no content area. The post/page content is stored but never output by the template.

### Prevention
```python
# Check template before applying
# elementor_header_footer = header + footer ONLY (no content)
# Use default template or leave template field empty for content
```

### Auto-Fix
```bash
# Option A: Change template to default
curl -X POST -u "$AUTH" "$SITE/wp-json/wp/v2/pages/{id}" \
  -d '{"template": ""}'

# Option B: Force-delete if it's an orphaned page blocking a post
curl -X DELETE -u "$AUTH" "$SITE/wp-json/wp/v2/pages/{id}?force=true"
```

---

## EP-005: Script Tag Sanitization
**Frequency:** 10+ occurrences | **Severity:** MEDIUM | **Confidence:** 0.92

### Symptoms
- JavaScript not executing in post content
- `<script>` tags absent from rendered HTML
- Code Snippets plugin snippet not appearing
- Custom JS not running

### Root Cause
WordPress `wp_filter_post_kses` strips ALL `<script>` tags from post content via REST API. The REST API is designed for content, not code.

### Prevention
```python
# NEVER put <script> tags in post content via REST API
# Instead, use:
# 1. Code Snippets plugin (REST API available for wpcode-snippets)
# 2. mu-plugins (direct filesystem)
# 3. WP admin dashboard (manual creation)
```

### Auto-Fix
```bash
# If code was in post content, migrate to Code Snippets
curl -X POST -u "$AUTH" "$SITE/wp-json/wp/v2/wpcode-snippets" \
  -d '{"title": "My Snippet", "content": "js_code_here", "status": "publish", "wpcode_type": "js"}'
```

---

## EP-006: wpautop Paragraph Corruption in Mixed Content
**Frequency:** 20+ occurrences | **Severity:** LOW | **Confidence:** 0.85

### Symptoms
- Extra empty paragraphs appearing in content
- Images wrapped in `<p>` tags creating unwanted spacing
- `<br>` tags where newlines should be clean
- Content layout appears "stretched" or has extra whitespace

### Root Cause
When `<!-- wp:html -->` wraps mixed content (text + HTML), wpautop is disabled entirely — including for the text portions. This removes ALL paragraph formatting, not just the problematic wrapping.

### Prevention
```python
# Use <!-- wp:html --> only for self-contained HTML blocks
# For mixed content (text + custom HTML), either:
# 1. Use separate blocks (paragraph block + html block)
# 2. Accept the wpautop wrapping and fix artifacts in <style>/<script> only
# 3. Use gutenberg blocks for text, wp:html only for custom components
```

---

## EP-007: Cache Serving Stale Content
**Frequency:** 15+ occurrences | **Severity:** MEDIUM | **Confidence:** 0.88

### Symptoms
- Content updated in DB but live page shows old version
- REST API returns new content, browser shows old
- Cache-busting query parameter works
- Different results with/without `?v=timestamp`

### Root Cause
Multi-layer caching (PhastPress + Cloudflare + LiteSpeed + browser) can serve stale content. Each layer needs independent purging.

### Prevention
```python
# After ANY content change, purge all cache layers:
# 1. PhastPress: WP Admin → Settings → PhastPress → Purge
# 2. Cloudflare: API purge (single URL or zone)
# 3. LiteSpeed: WP Admin → LiteSpeed → Purge All
# 4. Add verification with cache-bust: curl "?v=$(date +%s)"
```

### Auto-Fix
```bash
# Cloudflare purge (requires API token)
curl -X POST "https://api.cloudflare.com/client/v4/zones/$ZONE/purge_cache" \
  -H "Authorization: Bearer $TOKEN" \
  -d "{\"files\":[\"$URL\"]}"

# Note: PhastPress and LiteSpeed have no REST API — must use WP admin
```

---

## EP-008: Media Upload HTML Corruption
**Frequency:** 3 occurrences | **Severity:** MEDIUM | **Confidence:** 0.90

### Symptoms
- HTML files uploaded via REST API media endpoint have `<p>` tags added
- `.html` files go through text processing despite octet-stream MIME type
- Standalone HTML pages render with broken styling

### Root Cause
WordPress processes ALL content through `wpautop()` on save, regardless of MIME type. REST API media upload triggers the content processing pipeline.

### Prevention
```python
# NEVER upload .html files via REST API
# Use direct filesystem access (SCP/SFTP) for HTML files
# For media uploads, use images/documents only
```

### Auto-Fix
```bash
# Upload HTML files directly to filesystem
scp page.html user@server:/var/www/html/wp-content/uploads/2026/03/
```

---

## EP-009: Application Password vs Dashboard Login Confusion
**Frequency:** 5+ occurrences | **Severity:** LOW | **Confidence:** 0.95

### Symptoms
- App password works for REST API but fails on wp-login.php
- "Invalid credentials" error on dashboard login with app password
- User cannot access WP admin despite correct app password

### Root Cause
Application passwords are for REST API only. They cannot be used for dashboard login via wp-login.php form. These are two separate authentication systems.

### Prevention
```markdown
# Application Passwords = REST API ONLY
# Dashboard Login = regular password (or SSO)
# They are different systems, passwords don't cross over
```

---

## EP-010: GeneratePress CSS Override Conflicts
**Frequency:** 8+ occurrences | **Severity:** MEDIUM | **Confidence:** 0.82

### Symptoms
- Injected CSS not applying correctly
- `background-color` overridden by theme
- `font-family` from theme overriding custom fonts
- Container padding/margin conflicts
- `body{}` declarations appearing multiple times

### Root Cause
GeneratePress has 13+ `body{}` CSS declarations: `background-color:var(--base-2)`, `background-image:url(...)`, `font-family`, `padding`, etc. Theme's container divs (`.entry-content`, `.inside-article`, `#main`) add layout artifacts.

### Prevention
```python
# Don't fight GeneratePress with CSS overrides
# Use document.write() + base64 for full-page replacement:
content = f'<script>var s=atob("{base64_html}");document.open();document.write(s);document.close();<\/script>'
```

### Auto-Fix
```html
<!-- CORRECT: Full-page replacement -->
<!-- wp:html -->
<script>
var s=atob("PCFET0NUWVBFIGh0bWw+PGh0bWw+PGhlYWQ+PC9oZWFkPjxib2R5PjxoMT5IZWxsbyA8L2gxPjwvYm9keT48L2h0bWw+");
document.open();
document.write(s);
document.close();
</script>
<!-- /wp:html -->
```
