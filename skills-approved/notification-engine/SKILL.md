---
name: notification-engine
description: Use when setting up alerts for site issues, sending notifications to teams, creating status monitors, configuring webhooks for events, or building escalation pipelines.
---

# Notification Engine

## Purpose
Send multi-channel notifications and alerts with severity routing and escalation for operational events.

## Use this when
- Alerting on site downtime, errors, or threshold breaches
- Notifying a team when a workflow completes or fails
- Creating status monitors with automatic alerts
- Routing alerts by severity to different channels
- Building escalation pipelines (warn → alert → page)

**Do NOT use this skill for:** Email marketing sequences or drip campaigns (→ `lifecycle-email-sequences`), marketing automation or subscriber lifecycle management (→ `email-marketing-engine`).

## Do this

### 1. Determine severity
| Level | Meaning | Default channel |
|-------|---------|----------------|
| `info` | FYI, completed task | Telegram (quiet) |
| `warn` | Something degraded | Telegram + email |
| `critical` | Service down / data loss | All channels + escalate |

### 2. Route to channels
Configure channel targets in `.secrets/notification.env`:
```
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...
BREVO_API_KEY=...
BREVO_ALERT_EMAIL=alerts@example.com
DISCORD_WEBHOOK_URL=...
```

### 3. Send the alert
```bash
python3 scripts/send-alert.py \
  --severity critical \
  --title "Site Down" \
  --body "https://example.com returned 503" \
  --channel telegram \
  --channel email
```

### 4. Escalation pattern
For critical alerts:
1. **Immediate**: Send to primary channel (Telegram)
2. **+5 min**: If no ack, send to email
3. **+15 min**: If no ack, send to Discord + additional contact
4. Log all attempts in `ops/alerts/<date>.log`

Track acknowledgement by checking for reply or marking in state file.

### 5. Log delivery
Every alert writes a line to `ops/alerts/YYYY-MM-DD.log`:
```
[HH:MM:SS] SEVERITY | title | channels | delivered: telegram=email
```

## Resources
- `scripts/send-alert.py` — Send alerts via Brevo email or Telegram
- `.secrets/notification.env` — Channel credentials (create if missing)

## Checks / common mistakes
- Sending critical alerts only to Telegram (people miss them) — always add email
- Not testing channel config before relying on it — dry-run first
- Forgetting to log alerts — makes debugging impossible
- Noisy alerts (every minor event) — use `info` sparingly, escalate judiciously
- Not handling missing credentials gracefully — script should fail loudly

## Output contract
Alert sent with: title, severity, channels used, delivery confirmation, log entry written.

## Output Contract
**Artifact**: Skill-specific deliverable (report, fix, config, or document)
**Evidence**: Proof that the work was completed correctly
**Decision**: What was decided or recommended
**Next**: Follow-up action or monitoring period
