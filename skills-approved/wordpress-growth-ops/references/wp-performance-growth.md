# WordPress Performance for Growth

Performance optimizations ranked by conversion impact. Not a general performance guide — focused on changes that directly affect conversion rate.

## Performance → Conversion Link

Research consensus:
- **1s delay** → 7% conversion loss
- **3s load** → 40%+ bounce rate
- **TTFB > 800ms** → measurable ranking impact
- **Core Web Vitals failing** → Google ranking penalty

For growth ops, performance is Layer 1 because visitors leave before seeing the offer.

## Quick Wins (High Impact, Low Risk)

### 1. Autoloaded Options Bloat
The #1 WordPress performance killer for database-heavy sites.

```bash
# Diagnose
wp db query "SELECT option_name, ROUND(LENGTH(option_value)/1024, 1) as size_kb FROM wp_options WHERE autoload='yes' ORDER BY LENGTH(option_value) DESC LIMIT 15"

# Fix: disable autoload for large transient/expired options
wp option update <option_name> <value> --autoload=no

# Check total autoload size
wp db query "SELECT ROUND(SUM(LENGTH(option_value))/1024, 1) as total_autoload_kb FROM wp_options WHERE autoload='yes'"
```

**Target:** Total autoload < 500KB. Anything over 1MB is actively hurting.

### 2. Object Cache
Missing object cache = every page load hits the database.

```bash
# Check if object cache is present
wp cache flush  # If this errors, no object cache drop-in

# Check for object-cache.php
ls wp-content/object-cache.php 2>/dev/null && echo "Present" || echo "MISSING"
```

**Fix:** Install Redis or Memcached + object cache drop-in. High-traffic sites without this are leaving performance on the table.

### 3. Image Optimization
Unoptimized images are the most common cause of slow money pages.

```bash
# Check for huge images in uploads
wp media list --field=guid | head -20

# Check upload directory size
du -sh wp-content/uploads/
```

**Fix:** WebP conversion, proper srcset, lazy loading for below-fold images. Many plugins handle this (ShortPixel, Imagify, EWWW).

### 4. Plugin Audit
Every active plugin adds PHP overhead on every request.

```bash
# List all active plugins
wp plugin list --status=active --fields=name,version

# Check for known heavy plugins
wp plugin list --status=active --field=name | grep -i 'elementor\|divi\|wpbakery\|rev.slider\|visual.composer'
```

**Growth-specific:** If a page builder plugin is used on money pages, profile its impact:
```bash
# Compare page load with and without page builder content
wp profile stage --path=<path> --url=<money-page-url>
```

## WordPress 6.9+ Performance Features

### On-Demand CSS (Classic Themes)
Classic themes now get automatic on-demand CSS loading.
- Only loads CSS for blocks actually used on each page
- 30-65% CSS payload reduction
- If using a classic theme, verify this is working:
```bash
curl -s <page-url> | grep -c 'wp-block-library-css'  # Should be minimal/bundled
```

### Zero Render-Blocking Block Themes
Block themes without custom stylesheets can load with zero render-blocking CSS.
- Styles come from global styles (theme.json) + separate block styles, all inlined
- Significantly improves LCP (Largest Contentful Paint)
- If using a block theme, check if custom stylesheet is adding render-blocking CSS

### Inline CSS Threshold
Raised threshold for inlining small stylesheets — fewer render-blocking resources.

## Caching Strategy for Money Pages

### Page Cache
- Money pages MUST be cached (unless personalized/dynamic)
- Cache TTL: 1-24 hours for content pages, 15-60 min for time-sensitive offers
- Exclude: cart, checkout, account pages, form submission pages
- Purge on: content update, plugin update, theme change

### Fragment Caching
For dynamic elements within cached pages:
- Shopping cart widget (update via AJAX)
- Personalized greetings
- "Recently viewed" sections
- Stock availability

### Browser Cache
```nginx
# nginx config for static assets
location ~* \.(css|js|jpg|jpeg|png|gif|ico|woff2)$ {
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```

## Cron Performance

WP-Cron running on every page load is a hidden performance killer.

```bash
# Check cron status
wp cron event list --fields=hook,next_run

# Disable pseudo-cron (use system cron instead)
# wp-config.php: define('DISABLE_WP_CRON', true);

# System cron (runs every 5 minutes)
# */5 * * * * cd /path/to/wordpress && wp cron event run --due-now > /dev/null 2>&1
```

## Measurement Protocol

### Before/After Comparison
Always measure with the same tool and conditions:

```bash
# Consistent measurement
curl -s -o /dev/null -w "TTFB: %{time_starttransfer}s\nTotal: %{time_total}s\nSize: %{size_download}bytes\n" <url>

# Multiple samples (average out noise)
for i in {1..5}; do
  curl -s -o /dev/null -w "%{time_total}\n" <url>
done | awk '{sum+=$1} END {print "Average:", sum/NR, "seconds"}'
```

### Core Web Vitals Check
- LCP (Largest Contentful Paint): < 2.5s
- FID (First Input Delay): < 100ms
- CLS (Cumulative Layout Shift): < 0.1

Use PageSpeed Insights API for programmatic checks:
```bash
curl -s "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=<url>&strategy=mobile&key=<key>" | jq '.lighthouseResult.categories.performance.score'
```
