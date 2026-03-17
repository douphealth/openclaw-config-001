# WordPress Caching — Platform Guide

## Cache Layer Stack
```
Browser Cache → Cloudflare (CDN/Edge) → Server Cache (LiteSpeed) →
App Cache (PhastPress) → Object Cache (Redis) → Database
```

Every layer must be purged independently.

## Cloudflare Cache

### Purge Single URL
```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  '{"files":["https://site.com/page-url/"]}'
```

### Purge Everything
```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  '{"purge_everything":true}'
```

### Verification (Bypass Cache)
```bash
curl -s -H "Cache-Control: no-cache" -H "Pragma: no-cache" "https://site.com/page/"
curl -s "https://site.com/page/?v=$(date +%s)"  # Query param bypass
```

### Cache-Status Headers to Check
```
cf-cache-status: HIT/MISS/EXPIRED/DYNAMIC
cf-ray: <request-id>
cf-cache-datetime: <cache-time>
```

## LiteSpeed Cache

### Via WP Admin
```
LiteSpeed Cache → Toolbox → Purge All
```

### Via WP-CLI (if available)
```bash
wp litespeed-purge all
wp litespeed-purge post {id}
wp litespeed-purge category {id}
```

### No REST API method — requires admin access

## PhastPress

### Via WP Admin
```
Settings → PhastPress → Purge Cache
```

### Cache Location
- Static HTML files in `wp-content/cache/phastpress/`
- Each URL has a corresponding cached file
- Auto-purged when content updates (usually)

### No REST API or CLI method

## Browser Cache

### Via Headers (Set by Server)
```
Cache-Control: max-age=31536000 (1 year for static assets)
Cache-Control: no-cache, must-revalidate (for HTML)
ETag: <hash> (conditional requests)
Last-Modified: <date> (conditional requests)
```

### Force Browser Cache Clear (User-Side)
```
Add query parameter: ?v=timestamp
Or hard refresh: Ctrl+Shift+R / Cmd+Shift+R
```

## Multi-Layer Cache Purge Protocol

### After Content Update (Single Page)
```bash
# 1. Purge Cloudflare for that URL
curl -X POST "$CF_PURGE_URL" -d "{\"files\":[\"$PAGE_URL\"]}"

# 2. PhastPress — no API, must use WP admin
echo "⚠️ Manual: Settings → PhastPress → Purge"

# 3. LiteSpeed — no API, must use WP admin  
echo "⚠️ Manual: LiteSpeed → Toolbox → Purge All"

# 4. Verify with cache-bust
curl -s "$PAGE_URL/?v=$(date +%s)" | grep -o "ExpectedContent"
```

### After Bulk Update (Entire Site)
```bash
# Purge everything from Cloudflare
curl -X POST "$CF_PURGE_URL" -d '{"purge_everything":true}'

# PhastPress + LiteSpeed — must use WP admin
echo "⚠️ Manual: Purge all caches in WP admin"
```
