# Cache Platform Reference

## Quick Purge Commands

### Cloudflare
```bash
# Single URL
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone}/purge_cache" \
  -H "Authorization: Bearer {token}" \
  -d '{"files":["{url}"]}'
```

### LiteSpeed
- WP Admin → LiteSpeed Cache → Toolbox → Purge All
- CLI: `wp litespeed-purge all`
- No REST API

### PhastPress
- WP Admin → Settings → PhastPress → Purge
- No REST API or CLI

## Verification
```bash
curl -s "{url}/?v=$(date +%s)" | grep -c "expected"
curl -s -H "Cache-Control: no-cache" "{url}"
```
