# FluentCRM REST API Cookbook

## Authentication
```python
import base64
encoded = base64.b64encode(b'username:app_password').decode()
headers = {
    'Authorization': f'Basic {encoded}',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
    'Content-Type': 'application/json',
}
```

**CRITICAL: User-Agent header required.** Python urllib gets 403 without it. curl works fine.

## Subscribers

### List subscribers
```
GET /wp-json/fluent-crm/v2/subscribers?page=1&per_page=50
```

### Get subscriber by email
```
GET /wp-json/fluent-crm/v2/subscribers?search=email@example.com
```

### Get subscriber's emails
```
GET /wp-json/fluent-crm/v2/subscribers/{id}/emails
```

## Tags

### List tags
```
GET /wp-json/fluent-crm/v2/tags
```

### Apply tag to subscriber (bulk action)
```
POST /wp-json/fluent-crm/v2/subscribers/do-bulk-action
{"action_name":"add_to_tags","action_options":[TAG_ID],"subscriber_ids":[SUB_ID]}
```

### Remove tag
```
POST /wp-json/fluent-crm/v2/subscribers/do-bulk-action
{"action_name":"remove_from_tags","action_options":[TAG_ID],"subscriber_ids":[SUB_ID]}
```

## Sequences

### List sequences
```
GET /wp-json/fluent-crm/v2/sequences
```

### Get sequence with emails
```
GET /wp-json/fluent-crm/v2/sequences/{id}?with[]=sequence_emails
```

### Create/update sequence email
```
POST /wp-json/fluent-crm/v2/sequences/{id}
Body: email object with subject, body, settings
```

### Enroll subscriber in sequence (RELIABLE)
```
POST /wp-json/fluent-crm/v2/sequences/{id}/subscribers
{"subscriber_ids": [SUB_ID]}
```
Returns: sequence tracker + scheduled emails with hydrated content.

### Check subscriber's sequences
```
GET /wp-json/fluent-crm/v2/sequences/subscriber/{id}/sequences
```

### Bulk add to sequence (BROKEN)
```
POST /wp-json/fluent-crm/v2/subscribers/do-bulk-action
{"action_name":"add_to_email_sequence","action_options":[SEQ_ID],"subscriber_ids":[...]}
→ Returns "Invalid Email Sequence ID" always
→ Requires FLUENTCAMPAIGN constant (Pro)
→ Don't use this
```

## Funnels

### Get funnel
```
GET /wp-json/fluent-crm/v2/funnels/{id}
```

### Save funnel sequences
```
POST /wp-json/fluent-crm/v2/funnels/funnel/save-funnel-sequences
(form-urlencoded, not JSON)
```

### Funnel email reports (check for sent emails)
```
GET /wp-json/fluent-crm/v2/funnels/{id}/email_reports
```

### Funnel report (stats)
```
GET /wp-json/fluent-crm/v2/funnels/{id}/report
```

## Common Issues

### "send_custom_email" with reference_campaign is broken
The campaign object exists as a shell with no content. The funnel writer doesn't always hydrate it via API. The sent email shows `subject: "0"`, `body: ""`.

### Tags not applied via form submission
WordPress REST API form submission (`admin-ajax.php`) may not trigger tag automation that depends on PHP hooks or WPCode snippets. Check if tags are applied via PHP filter — they won't fire through API submission.

### wp/v2/settings doesn't expose CRM options
Only whitelisted WordPress core options are exposed. FluentCRM settings (mailer, etc.) are in wp_options but not accessible via REST API.

### Setting endpoint returns empty
```
GET /wp-json/fluent-crm/v2/setting → {"__bench":...}
(Empty unless you have the right role/capabilities)
```

## Cron Status
```
GET /wp-json/fluent-crm/v2/setting/cron_status
→ Returns scheduled hooks and next run times
```

## System Logs
```
GET /wp-json/fluent-crm/v2/setting/system-logs
→ Returns debug logs (often empty)
```
