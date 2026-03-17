---
name: wordpress-performance
description: WordPress performance optimization, cache management, Core Web Vitals monitoring, database optimization, image optimization, and CDN configuration. Use when WordPress sites need speed improvements, cache troubleshooting, performance audits, database cleanup, or Core Web Vitals fixes. NOT for: content optimization (→editorial-post-enhancement), SEO auditing (→seo-audit-playbook), server infrastructure (→infrastructure-ops).
---

# WordPress Performance — Speed & Core Web Vitals Optimization

## Purpose
Optimize WordPress site performance across all layers: server response, caching, database, assets, images, and CDN. Detect and fix performance regressions. Manage cache across multiple platforms.

## When to Use
- Page load time exceeds 3 seconds
- Core Web Vitals failing (LCP, FID, CLS)
- Cache not reflecting content updates
- Database bloat affecting performance
- Image optimization needed
- CDN configuration issues
- Performance regression detection
- Multi-cache management (PhastPress + Cloudflare + LiteSpeed)

**Do NOT use for:** Content SEO (→`seo-audit-playbook`), site growth strategy (→`wordpress-growth-ops`), server setup (→`infrastructure-ops`).

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

## Cache Architecture — Complete Guide

### Cache Layer Stack (Typical WordPress)
```
Browser Cache → CDN (Cloudflare) → Server Cache (LiteSpeed) → 
Application Cache (PhastPress/WP Rocket) → Object Cache (Redis) → 
Database → WordPress → wpautop → HTML Output
```

Each layer must be purged independently for changes to reflect.

### Cloudflare Cache
```bash
# Purge single URL via API
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache" \
  -H "Authorization: Bearer {cf_token}" \
  -H "Content-Type: application/json" \
  '{"files":["https://site.com/page-url/"]}'

# Purge everything
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache" \
  -H "Authorization: Bearer {cf_token}" \
  -H "Content-Type: application/json" \
  '{"purge_everything":true}'

# Cache verification (bypass cache)
curl -s -H "Cache-Control: no-cache" -H "Pragma: no-cache" "https://site.com/page/"
# Or add query param: ?v=$(date +%s)
```

### LiteSpeed Cache
```
# Via WP Admin: LiteSpeed Cache → Toolbox → Purge All
# Via REST API: Not available — requires WP admin access
# Via CLI: wp litespeed-purge all (if WP-CLI installed)
```

### PhastPress
```
# Via WP Admin: Settings → PhastPress → Purge Cache
# No REST API or CLI method available
# Cache stored as static HTML files on server
```

### WP Rocket (if installed)
```bash
# Via REST API (if enabled)
POST /wp-json/wp-rocket/v1/purge?url=https://site.com/page/
```

## Performance Measurement

### Quick Performance Check
```bash
# Time to first byte
curl -o /dev/null -w "TTFB: %{time_starttransfer}s\n" -s "https://site.com/"

# Total load time
curl -o /dev/null -w "Total: %{time_total}s\n" -s "https://site.com/"

# Page size
curl -s "https://site.com/" | wc -c
```

### Core Web Vitals Targets
| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | < 2.5s | 2.5-4.0s | > 4.0s |
| FID (First Input Delay) | < 100ms | 100-300ms | > 300ms |
| CLS (Cumulative Layout Shift) | < 0.1 | 0.1-0.25 | > 0.25 |
| TTFB (Time to First Byte) | < 800ms | 800-1800ms | > 1800ms |
| INP (Interaction to Next Paint) | < 200ms | 200-500ms | > 500ms |

## Database Optimization

### Identify Bloat
```bash
# Check database size via WP-CLI or direct DB access
wp db size --tables --human-readable

# Common bloat sources:
# - wp_postmeta (revision meta, transient meta)
# - wp_options (autoloaded options)
# - wp_commentmeta (spam metadata)
# - wp_posts (post revisions, auto-drafts)
```

### Cleanup Operations
```sql
-- Delete post revisions older than 30 days
DELETE FROM wp_posts WHERE post_type = 'revision' 
AND post_date < DATE_SUB(NOW(), INTERVAL 30 DAY);

-- Delete expired transients
DELETE FROM wp_options WHERE option_name LIKE '%_transient_%' 
AND option_name NOT LIKE '%_transient_timeout_%';

-- Delete spam comments metadata
DELETE FROM wp_commentmeta WHERE comment_id IN (
    SELECT comment_id FROM wp_comments WHERE comment_approved = 'spam'
);

-- Optimize tables
OPTIMIZE TABLE wp_posts, wp_postmeta, wp_options, wp_commentmeta;
```

### Autoloaded Options Check
```sql
-- Find large autoloaded options (slow down every page load)
SELECT option_name, LENGTH(option_value) as size 
FROM wp_options WHERE autoload = 'yes' 
ORDER BY LENGTH(option_value) DESC LIMIT 20;
```

## Image Optimization

### Via REST API
```bash
# Check image sizes in media library
GET /wp-json/wp/v2/media?per_page=100&mime_type=image

# Look for: file size, dimensions, srcset availability
```

### Best Practices
1. **Serve WebP/AVIF** — Use ShortPixel, Imagify, or EWWW plugin
2. **Lazy loading** — Native `loading="lazy"` on all below-fold images
3. **Responsive images** — Ensure `srcset` and `sizes` attributes
4. **Preload LCP image** — `<link rel="preload" as="image" href="...">` for hero images
5. **Dimensions** — Always specify width/height to prevent CLS

## CSS/JS Optimization

### Render-Blocking Resources
```
1. Identify render-blocking CSS/JS
2. Inline critical CSS in <head>
3. Defer non-critical CSS with media="print" onload="media='all'"
4. Defer JS with async or defer attributes
5. Remove unused CSS/JS (coverage analysis)
```

### Font Optimization
```
1. Use font-display: swap
2. Preload critical fonts: <link rel="preload" as="font" crossorigin>
3. Subset fonts to used characters only
4. Self-host fonts instead of Google Fonts (privacy + speed)
```

## Common Performance Issues

### Slow TTFB
```
Cause: Server response time > 800ms
Diagnosis: curl -o /dev/null -w "%{time_starttransfer}s" site.com
Fix: Enable page caching, optimize database, check hosting
```

### Layout Shift (CLS)
```
Cause: Images/ads without dimensions, dynamic content injection
Diagnosis: Check for width/height attributes, font loading
Fix: Set dimensions, use font-display: swap, reserve space for ads
```

### Large Page Size
```
Cause: Unoptimized images, inline assets, excessive HTML
Diagnosis: curl -s site.com | wc -c (compare to baseline)
Fix: Compress images, minify CSS/JS, remove unused code
```

### Slow Database Queries
```
Cause: Unoptimized queries, missing indexes, autoload bloat
Diagnosis: Query monitor plugin, slow query log
Fix: Add indexes, clean autoloaded options, optimize tables
```

## Performance Optimizations

### Speed Multipliers
- Use `_fields` parameter to fetch only needed data
- Parallel API calls (max 10/site)
- Batch by site, never context-switch
- Pre-fetch auth before starting
- Cache category/post maps

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

## Output Contract
**Artifact**: Performance improvement with measured impact
**Evidence**: Before/after metrics (TTFB, page size, CWV scores)
**Decision**: Optimization successful or root cause identified
**Next**: Monitor metrics for 24h, alert on regression

## Scripts
- `scripts/perf-audit.py` — Quick performance audit (TTFB, page size, asset count)
- `scripts/cache-purge.py` — Multi-platform cache purging
- `scripts/db-optimize.py` — Database cleanup and optimization
- `scripts/image-audit.py` — Image optimization audit

## References
- `references/cache-platforms.md` — Cache platform-specific purge methods
- `references/core-web-vitals.md` — CWV measurement and optimization guide
- `references/database-optimization.md` — Database maintenance procedures
- `references/image-optimization.md` — Image optimization strategies
