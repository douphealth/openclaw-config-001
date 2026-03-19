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

## Enterprise Protocol (SOTA Standard — Added 2026-03-18)

ALL operations must follow `skills/shared/enterprise-protocol.md`:
- **Pre-flight**: health check + auth verification + current state capture + rollback plan
- **Backup**: always before any modification (even single-post edits)
- **Retry**: exponential backoff, max 3 attempts per API call
- **Verify**: check after each modification (GET after POST)
- **Progress**: report every 10 items in batch operations
- **Health**: check site accessibility every 50 items during long operations

## Plantastic Haven (PH) — Lessons Learned (2026-03-18)

- **URL**: https://plantastichaven.com
- **Origin IP**: 107.173.167.3 (RackNerd VPS, 3 Xeon cores, 2464MB RAM)
- **Stack**: WordPress + LiteSpeed + Cloudflare + CyberPanel
- **Auth**: Admin:vshq G2r2 fXOs 2WC3 uHK4 cCYd
- **Posts**: 140 total
- **Critical lesson**: Site has broken HTTPS (LiteSpeed SSL) — origin HTTP works but HTTPS hangs. Server running 364+ days without restart. CPU 98%, load 9+.
- **Fix**: Cloudflare proxied + Flexible SSL, or disable HTTP→HTTPS redirect in LiteSpeed
- **Backup**: ops/backups/ph-posts/ (140 posts, 44MB)

## Skill Upgrades (2026-03-18)

- Created `skills/shared/enterprise-protocol.md` — mandatory operational rules
- Created `skills/shared/scripts/wp-bulk-ops.py` — reusable Python helper class
- Added enterprise protocol reference to 36/45 workspace skills
- Enhanced swarm-orchestrator with parallel dispatch matrix
- Enhanced skill-router with post-task strategy identification
