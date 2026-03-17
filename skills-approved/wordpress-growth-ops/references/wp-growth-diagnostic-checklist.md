# WordPress Growth Diagnostic Checklist

Step-by-step diagnostic flowchart for WordPress conversion problems.

## Quick Triage (< 2 minutes)

1. **Is the site up?** → `curl -s -o /dev/null -w "%{http_code}" <url>`
   - If not 200 → infrastructure problem (→ `infrastructure-ops`)
2. **Is the money page published?** → `wp post list --post_type=page --s=<slug> --field=post_status`
   - If draft/trash → publish it
3. **Is there a PHP fatal?** → `wp eval 'echo "ok";' --path=<path>`
   - If error → check `wp-content/debug.log` or `wp plugin list --status=active`

## Full Diagnostic Flow

### Step 1: Performance Gate
```
┌─ Page load > 3s? ──── YES ─→ Check: wp doctor check
│                               Check: autoload options bloat
│                               Check: object cache presence
│                               Fix performance BEFORE other layers
└─ NO ─→ Continue ↓
```

Key WP-CLI checks:
```bash
wp doctor check --path=<path>
wp profile stage --path=<path>
wp db query "SELECT option_name, LENGTH(option_value) FROM wp_options WHERE autoload='yes' ORDER BY 2 DESC LIMIT 10"
```

### Step 2: Rendering Gate
```
┌─ Page shows expected content? ──── NO ─→ Check: block errors
│                                          Check: shortcode failures
│                                          Check: theme template override
│                                          Check: cache showing stale content
└─ YES ─→ Continue ↓
```

Key checks:
```bash
curl -s <page-url> | grep -c 'Invalid block\|shortcode-error\|error'
wp post get <page-id> --field=post_content | head -50
```

### Step 3: Form/Checkout Gate
```
┌─ Form appears on page? ──── NO ─→ Check: form shortcode/block present
│                                    Check: form plugin active
│                                    Check: form ID correct in shortcode
└─ YES ─→ Continue ↓

┌─ Form submits without error? ──── NO ─→ Check: AJAX endpoint (wp-admin/admin-ajax.php)
│                                          Check: nonce validity
│                                          Check: JS console errors
│                                          Check: REST API form submission endpoint
└─ YES ─→ Continue ↓

┌─ Submission creates record? ──── NO ─→ Check: form plugin entry storage
│                                        Check: database table exists
│                                        Check: PHP errors during save
└─ YES ─→ Continue ↓
```

### Step 4: CRM/Email Gate
```
┌─ CRM receives contact? ──── NO ─→ Check: API key valid
│                                    Check: integration enabled in form plugin
│                                    Check: CRM list/segment exists
│                                    Check: tag mapping correct
└─ YES ─→ Continue ↓

┌─ Automation fires? ──── NO ─→ Check: trigger conditions met
│                                Check: automation is active (not paused)
│                                Check: contact not already in sequence
│                                Check: email deliverability (spam folder)
└─ YES ─→ Continue ↓
```

### Step 5: Delivery Gate
```
┌─ User gets promised asset? ──── NO ─→ Check: file exists and is accessible
│                                        Check: download link not expired
│                                        Check: email with link sent
│                                        Check: thank-you page redirects work
└─ YES ─→ PATH VERIFIED ✓
```

## WP-CLI Quick Reference for Growth Diagnostics

| What | Command |
|---|---|
| Site URL | `wp option get siteurl` |
| Home URL | `wp option get home` |
| Active plugins | `wp plugin list --status=active` |
| Active theme | `wp theme list --status=active` |
| Recent posts | `wp post list --post_type=post --posts_per_page=5 --field=post_title` |
| Published pages | `wp post list --post_type=page --post_status=publish --field=post_title` |
| Form plugin entries | Varies by plugin (Gravity: `wp gf entry list`, CF7: check DB) |
| Check cron | `wp cron event list --fields=hook,next_run` |
| Debug status | `wp config get WP_DEBUG` |
| Object cache | `wp cache flush` (test) or check drop-ins |
| Rewrite rules | `wp rewrite list` |
| Recent errors | Check `wp-content/debug.log` or server error log |

## Red Flags (Instant Escalation)

- **`wp doctor check` reports autoload > 1MB** → likely performance impact
- **Multiple plugins with pending updates** → security + compatibility risk
- **`WP_DEBUG` is true in production** → may expose errors to users
- **Permalinks set to "Plain"** → likely rewrite rule issues
- **Object cache drop-in missing on high-traffic site** → every page hit hits DB
- **WooCommerce: abandoned cart rate > 70%** → checkout friction issue
- **Form: >50% drop-off between view and submit** → form UX or trust issue
