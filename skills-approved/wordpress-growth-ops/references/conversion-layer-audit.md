# Conversion Layer Audit

Detailed analysis patterns for each conversion layer in WordPress growth operations.

## Layer 1: Traffic → Page Entry

### What to audit
- Which pages receive organic/search traffic (Google Search Console data)
- Bounce rate by landing page
- Time on page for money pages
- Mobile vs desktop split

### Common issues
- Money pages not indexed or ranking
- Traffic going to wrong pages (blog posts instead of landing pages)
- Slow page load scaring off visitors before content appears
- Mobile layout broken on key conversion pages

### WP-CLI probes
```bash
# Check if money pages exist and are published
wp post list --post_type=page --s=<money-page-slug> --fields=ID,post_title,post_status

# Check SEO metadata exists
wp post meta get <page-id> _yoast_wpseo_title
wp post meta get <page-id> _yoast_wpseo_metadesc

# Check page template
wp post meta get <page-id> _wp_page_template
```

## Layer 2: Page → CTA Visibility

### What to audit
- Is the CTA above the fold?
- Does the CTA stand out visually?
- Is the offer clear in 5 seconds?
- Are there competing CTAs?

### Common issues
- CTA buried below the fold or hidden in a carousel
- Generic CTA text ("Submit", "Click Here")
- Multiple competing CTAs creating decision paralysis
- CTA button color doesn't contrast with background
- Trust signals missing near CTA

### HTML probes
```bash
# Check for CTA elements above the fold
curl -s <page-url> | head -100 | grep -i 'btn\|cta\|buy\|book\|sign\|start\|get'

# Count total CTAs on page
curl -s <page-url> | grep -oi 'btn\|button\|cta' | wc -l
```

## Layer 3: CTA → Form/Checkout Interaction

### What to audit
- Does the CTA link to the correct form/checkout page?
- Does the form load without errors?
- Are all form fields rendering?
- Does the form submit (AJAX and fallback)?
- Is there a progress indicator for multi-step forms?

### Common issues
- CTA link broken (404, wrong URL, missing page)
- Form plugin shortcode has wrong form ID
- JavaScript error prevents form from loading
- AJAX nonce expired (common after caching)
- Required fields confusing or too many
- No validation feedback on errors
- Form doesn't work on mobile (viewport issues)

### WP-CLI + REST probes
```bash
# Verify target page exists
wp post list --post_type=page --s=<form-page-slug> --fields=ID,post_status

# Check form plugin is active
wp plugin list --name=contact-form-7 --field=status
wp plugin list --name=wpforms --field=status
wp plugin list --name=fluentform --field=status

# Test form REST endpoint (Fluent Forms example)
curl -X POST <site>/wp-json/fluentform/v1/forms/<id>/submit \
  -H "Content-Type: application/json" \
  -d '{"fields":{"email":"test@example.com"}}'

# Check for nonce issues in admin-ajax
curl -s <site>/wp-admin/admin-ajax.php?action=<form-action> | head -5
```

## Layer 4: Form Submit → Data Storage

### What to audit
- Does the form create a database record?
- Does the form plugin fire its submission hooks?
- Are required fields being saved?
- Is file upload working (if applicable)?

### Common issues
- Form plugin database table missing/corrupt
- PHP error during save (check debug.log)
- Plugin conflict preventing hooks from firing
- File upload size limits too restrictive
- Nonce validation failing silently

### Probes
```bash
# Check form plugin DB tables exist
wp db tables --scope=<form-plugin>

# Check for recent form entries (plugin-specific)
# Gravity Forms
wp gf entry list --form_id=<id> --limit=5
# Or direct DB
wp db query "SELECT * FROM wp_gf_entry ORDER BY date_created DESC LIMIT 5"

# Check debug.log for form-related errors
tail -50 wp-content/debug.log | grep -i 'form\|submit\|nonce\|ajax'
```

## Layer 5: Data Storage → CRM/ESP Delivery

### What to audit
- Is the CRM/ESP integration configured?
- Are API credentials valid?
- Does the integration fire on form submission?
- Are field mappings correct?
- Is there a rate limit or quota issue?

### Common issues
- API key expired or revoked
- Integration disabled after plugin update
- Field mapping mismatch (email goes to wrong field)
- CRM list/segment/tag doesn't exist
- Rate limiting on CRM API
- Contact already exists and update is skipped

### Probes
```bash
# Check form plugin integration settings
wp option get <form-plugin>_integrations  # varies by plugin

# Check for CRM-specific options
wp option list --search=*mailchimp* --fields=option_name
wp option list --search=*activecampaign* --fields=option_name
wp option list --search=*brevo* --fields=option_name
wp option list --search=*sendinblue* --fields=option_name

# Test CRM API connectivity (Brevo example)
curl -s -H "api-key: <key>" https://api.brevo.com/v3/account | head -5
```

## Layer 6: CRM → Automation/Delivery

### What to audit
- Is the automation sequence active?
- Does the trigger condition match the data being sent?
- Is the first email configured and scheduled?
- Are there suppression rules blocking delivery?

### Common issues
- Automation paused or in draft mode
- Trigger condition doesn't match (e.g., tag not applied)
- Email template missing or broken
- Contact already went through the sequence
- Suppression list includes the test email
- Email landing in spam (SPF/DKIM/DMARC issues)

### Probes
```bash
# Check email deliverability basics
dig TXT <domain> | grep -i 'spf\|dkim\|dmarc'

# Test email delivery to a fresh address
wp eval '
  $to = "test-" . time() . "@mail-tester.com";
  $subject = "WP Growth Ops Test";
  $result = wp_mail($to, $subject, "Test body");
  echo $result ? "Sent to $to" : "FAILED";
' --path=<path>
```

## Self-Critique Questions (After Each Audit)

1. Did I verify the ENTIRE path with fresh data, or just check config?
2. Did I test from the user's perspective (mobile, slow connection)?
3. Did I check for plugin conflicts, not just individual plugin settings?
4. Did I confirm the fix works after cache purge?
5. Did I monitor for 48h to check for delayed issues (cron, batching)?
