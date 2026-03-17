# MEMORY.md — Durable Truths

_See `memory/YYYY-MM-DD.md` for daily context._

## WordPress Credentials
- **AFS**: Papalexios:pP4g kOOR SzO7 u24N eTxG flm6 (admin, User ID 1)
- **PH**: Admin:vshq G2r2 fXOs 2WC3 uHK4 cCYd (admin, User ID 11)
- Always read from `.secrets/*.access.env` files — they're the source of truth

## WordPress REST API — What Works & What Doesn't

### ✅ Works
- Posts/Pages CRUD, Media upload, Categories/Tags, Settings
- Yoast meta via `_yoast_wpseo_metadesc` in meta field
- `<!-- wp:html -->` Gutenberg block prevents wpautop
- Code Snippets REST API (PH) for JS injection
- HTML file upload via `application/octet-stream` MIME type

### ❌ Doesn't Work
- ALL REST API endpoints strip `<script>` tags (wp_filter_post_kses)
- WPCode blocks API creates posts but doesn't activate them
- WPCode Pro stores PHP snippets in custom table, NOT in wpcode-blocks endpoint
- Application passwords can't be used for wp-login.php form login
- `subscribers/do-bulk-action` with `add_to_email_sequence` always fails via REST
- WordPress corrupts HTML files on media upload (even with binary MIME)

## Homepage Deployment — Proven Patterns

### What Works
1. **iframe approach**: JS clears body, creates `position:fixed` iframe → works on ALL themes
2. **Scoped HTML**: `<div class="PREFIX">` + `all:initial` + prefixed CSS → zero conflicts
3. **`<!-- wp:html -->` block**: Prevents wpautop from processing raw HTML

### What NEVER Works
1. Full HTML document in page content → nested DOCTYPE/head/body
2. `document.write()` base64 → trapped in og:description meta tag
3. `wp_redirect()` → changes URL to ugly path
4. Meta refresh → client-side redirect, URL changes
5. HTML upload via WP media → corrupted by wpautop

### Theme-Specific Lessons
- **Twenty Twenty-Four**: `.entry-content` has conflicting CSS
- **Astra**: Puts scripts in og:description meta tag from post content
- **Kadence**: Elementor content in postmeta, not content field
- **GeneratePress**: 13+ `body{}` declarations override injected CSS

## Blank Page Debugging
1. Check body class: `page-id-*` vs `postid-*` (wrong content type?)
2. Check `content.raw` vs `content.rendered` (DB wiped?)
3. Check template: `elementor_header_footer` = no content area
4. Check slug conflicts between pages and posts

## FluentCRM (AFS)
- Sequence email path is reliable: `POST /sequences/{id}/subscribers`
- `subscribers/do-bulk-action` with `add_to_email_sequence` = broken via REST
- Delivery proof ≠ content proof — verify email_subject and email_body

## Brevo Webhook
- Port 8081 (8080 is SearXNG)
- Start: `nohup python3 ops/scripts/brevo-webhook.py 8081 &`

## All Managed WordPress Sites
| Site | Priority |
|------|----------|
| affiliatemarketingforsuccess.com | High |
| efficientgptprompts.com | High |
| gearuptogrow.com | High |
| mysticaldigits.com | Medium |
| plantastichaven.com | Secondary |
| micegoneguide.com | Secondary |
| frenchyfab.com | Low |
| gearuptofit.com | Low |

## Quality System (v5.0)
- Every task scored /25 (Functionality + Quality + Verification + Speed + Learning)
- Target: 22+/25 before claiming completion
- Quality monitor: `ops/self-improvement/quality-monitor.py`
- Quality logger: `ops/self-improvement/log-quality.py`
- Performance patterns: `skills/performance-patterns.md`
- Quality framework: `skills/quality-framework.md`
