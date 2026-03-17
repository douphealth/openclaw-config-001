---
name: email-marketing-engine
description: Build and operate enterprise-grade email marketing automation systems. Use when implementing multi-sequence drip campaigns, Brevo/Sendinblue API integration, subscriber lifecycle engines, email delivery pipelines, or self-hosted email automation. Triggers on requests to build email systems, set up Brevo API, create email engines, implement drip campaigns, build subscriber automation, or scale email marketing infrastructure.
---

# Email Marketing Engine

## Purpose
Build production-grade email marketing automation systems that run independently of WordPress/CRM mailer limitations. This skill covers the full stack: sequence architecture, API integration, subscriber lifecycle management, delivery verification, and operational monitoring.

## When to use
- Building a multi-sequence drip campaign from scratch
- Integrating Brevo (Sendinblue) REST API for email delivery
- Bypassing broken CRM mailer settings (FluentCRM, MailPoet, etc.)
- Implementing subscriber lifecycle tracking and auto-advancement
- Setting up instant delivery on signup + scheduled progression
- Building analytics dashboards for email performance

**Do NOT use for:** single one-off emails (use the CRM directly), debugging existing automations (use `email-automation-debugging`), or writing email copy (use `lifecycle-email-sequences`).

## Architecture Pattern

The proven architecture for reliable email automation:

```
┌─────────────────────────────────────────────────────┐
│  SUBSCRIBER LIFECYCLE ENGINE                        │
│                                                     │
│  Signup ──→ Contact Created ──→ Tag/List Applied    │
│      │                              │               │
│      ▼                              ▼               │
│  Fast Lane (5min)           Sequence Engine (hourly) │
│  - New signup detect        - Check pending emails  │
│  - Instant welcome email    - Auto-advance sequences│
│  - Auto-tag subscriber      - A/B subject testing   │
│  - Enroll in CRM sequence   - Retry failed sends    │
│      │                              │               │
│      ▼                              ▼               │
│  Brevo API ──→ Email Delivered ──→ Engagement Track │
│                                                     │
│  Sequences: Welcome (7) → Nurture (8) → Winback (3)│
└─────────────────────────────────────────────────────┘
```

## Implementation Steps

### 1. Sequence Design
Map all sequences with exact timing:
```json
{
  "welcome": {"emails": 7, "span_days": 14, "trigger": "on_signup"},
  "nurture": {"emails": 8, "span_days": 65, "trigger": "post_welcome"},
  "winback": {"emails": 3, "span_days": 14, "trigger": "inactive_30d"}
}
```
- Welcome: 0h, 24h, 72h, 120h, 168h, 240h, 336h
- Nurture: every 168h (weekly) after welcome completes
- Winback: 0h, 72h, 336h after 30 days inactive

### 2. Brevo API Integration
Use Brevo REST API v3, NOT SMTP (avoids auth issues):
```python
# Send endpoint
POST https://api.brevo.com/v3/smtp/email
Headers: api-key: YOUR_KEY, Content-Type: application/json

# Payload structure
{
  "sender": {"email": "verified@domain.com", "name": "Brand Name"},
  "to": [{"email": "user@example.com", "name": "User"}],
  "subject": "Subject line",
  "htmlContent": "<html>...</html>",
  "headers": {"List-Unsubscribe": "<unsubscribe_url>"}
}

# Critical: Only include "name" in "to" if non-empty
# Brevo returns 400 "name is missing in to" if name is empty string
```

### 3. Engine State Management
Track subscriber lifecycle in JSON state file:
```json
{
  "subscribers": {
    "1": {
      "email": "user@example.com",
      "enrolled_at": "2026-03-13T08:00:00+00:00",
      "current_sequence": "welcome",
      "sequence_started_at": "2026-03-13T08:00:00+00:00",
      "emails_sent": [
        {"sequence": "welcome", "index": 0, "subject": "...", "sent_at": "...", "messageId": "..."}
      ],
      "next_email_index": 1,
      "first_name": "User",
      "segment": "new_subscriber",
      "engagement": {"opens": 0, "clicks": 0, "bounced": false, "unsubscribed": false}
    }
  }
}
```

### 4. Cron Architecture
Three-tier cron for optimal performance:
```
*/5 * * * *  Fast lane (new signups only, instant welcome)
0 * * * *    Main engine (sequence progression, smart scan)
*/30 * * * * Engagement tracker (pull opens/clicks from API)
```

**Smart scan optimization:** Only check subscribers with pending emails, not all subscribers. Compare `send_at` time vs now. Skip completed sequences. This scales to 10K+ subscribers.

### 5. Auto-Retry with Backoff
```python
# On send failure:
# Retry 1: 5 minutes
# Retry 2: 30 minutes  
# Retry 3: 2 hours
# After 3 failures: skip email, advance to next
```

### 6. A/B Subject Testing
Deterministic per subscriber (not random):
```python
import hashlib
def select_subject(email, subscriber_id):
    variants = email.get('subject_variants', [])
    if not variants:
        return email['subject']
    hash_val = int(hashlib.md5(f"{subscriber_id}-{email['subject']}".encode()).hexdigest(), 16)
    return variants[hash_val % len(variants)]
```

### 7. Email Template
- Mobile-responsive HTML email template
- Inline CSS only (email client compatibility)
- Max 600px width
- Placeholder system: `{{email_body}}`, `{{first_name}}`, `{{subject}}`, `{{unsubscribe_url}}`, `{{site_url}}`
- UTM tracking on all internal links
- Brevo-compatible rendering

### 8. Link Verification
ALWAYS verify all links return HTTP 200 before deploying emails:
```python
from urllib.request import Request, urlopen
for link in extract_links(email_html):
    req = Request(link, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
    resp = urlopen(req, timeout=10)
    assert resp.code == 200, f"Broken link: {link}"
```

### 9. Deliverability Checklist
- SPF record: include provider's SPF (e.g., `include:spf.brevo.com`)
- DKIM: set up domain authentication in provider dashboard
- DMARC: configure at `p=quarantine` minimum
- List-Unsubscribe header in all emails
- Verified sender domain (not freemail)
- HTML + plain text versions

### 10. Analytics
Track per sequence:
- Send count per email position
- Open rate (via provider API)
- Click rate (via provider API)
- Bounce/unsubscribe rate
- Sequence completion rate

## Core Rules
- Never rely on CRM's built-in mailer for critical delivery — use provider API directly
- Always separate delivery proof (API messageId) from content proof (subject/body verification)
- State file is the source of truth, not the CRM
- Smart scan > full scan for scalability
- Auto-retry everything before declaring failure
- Verify ALL links in ALL emails before first send

## Output
When building an email engine, deliver:
- Engine script with state management
- Fast lane script for instant delivery
- Sequence JSON files with verified links
- HTML email template
- Config file with sequence definitions
- Analytics script
- Cron schedule
- Deliverability status report

## Common Mistakes
- Using CRM's SMTP settings (often broken, can't fix via API)
- Scanning all subscribers every run (doesn't scale)
- Not auto-retrying failed sends
- Not verifying links before sending
- Skipping List-Unsubscribe header (hurts deliverability)
- Using random A/B testing (inconsistent experience)
- Not tracking engagement (can't identify inactive subscribers)


## Performance Optimizations

### Speed Multipliers
- Use proven email templates as starting point (subject lines, CTAs, structure)
- Batch API calls for email platform operations
- Pre-fetch subscriber data and sequence info in parallel
- Template-based email generation (don't start from blank)
- A/B test subject lines and CTAs

### Self-Critique Scorecard (/25)
1. **Functionality** (1-5): Does the email/sequence work perfectly?
2. **Quality** (1-5): Is the copy enterprise-grade?
3. **Verification** (1-5): Verified via API + test email + automation check?
4. **Speed** (1-5): Optimal execution?
5. **Learning** (1-5): Patterns documented?

**Target: 22+/25**

### Auto-Check
- [ ] Pre-flight checks (credentials, list/sequence exists)
- [ ] Verified via API + test send
- [ ] Subject line and CTA optimized
- [ ] Score logged to memory

## Output Contract
**Artifact**: Email marketing system (forms, sequences, tracking)
**Evidence**: List health metrics, delivery rates
**Decision**: System operational
**Next**: Ongoing optimization

## Compatibility
- Targets current WordPress 6.9+ where applicable
- REST API + WP-CLI preferred over browser automation
- Batch operations via `_fields` + `per_page=100` + `concurrent.futures`
- Browser automation only when API/CLI insufficient

## Inputs Required (Pre-Flight)
Before executing any task in this skill:
1. **Target identification** — What site, page, post, or system is being operated on?
2. **Auth verification** — Confirm credentials work (test API call or CLI command)
3. **Current state** — Understand what exists before making changes (GET before POST)
4. **Environment** — Production vs staging (assume production unless stated)
5. **Constraints** — No downtime? Preserve SEO? Preserve data? Budget limits?

## Triage Protocol
Before ANY operation:
1. **Identify** — What type of content/system/problem is this?
2. **Check state** — Query current state via API/CLI before modifying
3. **Verify creds** — Confirm authentication works
4. **Plan rollback** — How to undo if something breaks?
5. **Scope check** — Is this a single item or batch? Scale determines approach.

## Speed Optimizations
- **API calls**: Always use `_fields` parameter (80%+ payload reduction)
- **Pagination**: Use `per_page=100` for list endpoints
- **Parallelism**: Use `concurrent.futures` for independent operations (max 10/site)
- **Caching**: Store results in session — never re-fetch same data
- **Batching**: Group similar operations into single API calls where possible
- **Direct CLI**: Use WP-CLI `wp db query` for complex operations

## Error Recovery (Auto-Learning)
- Track error patterns — after 2 failures, try alternative approach
- Log recurring fixes to `memory/YYYY-MM-DD.md`
- Update references when new patterns discovered
- Rollback plan: Know how to undo before making changes

## Self-Critique Scorecard (/25)
Before claiming complete, score yourself:
1. **Triage** (1-5): Was current state fully understood before changes?
2. **Execution** (1-5): Was the operation clean, efficient, correct?
3. **Verification** (1-5): Was the result verified via API/live check?
4. **Rollback** (1-5): Can changes be undone if issues found?
5. **Learning** (1-5): Were new patterns documented for future use?

**Target: 22+/25**

## Output Contract
- **Artifact**: What was created/changed/deleted
- **Evidence**: API response proof + live verification
- **Decision**: Success/failure with reasoning
- **Next**: What follow-up is needed (if any)
