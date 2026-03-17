---
name: notification-engine
description: Use when configuring alert routing, escalation policies, webhook notification delivery, severity-based channel selection, or operational notifications for downtime, threshold breaches, workflow failures, or status change events that need provable delivery.
---

# Notification Engine

## Purpose
Design and operate operational notifications with severity routing, escalation chains, delivery proof, and noise control.

## Use this when
- alerting on site downtime, HTTP error spikes, or resource threshold breaches
- notifying an operator when a deployment, backup, or workflow completes or fails
- configuring webhook or event-driven alert delivery via Slack, Telegram, email, or PagerDuty
- routing alerts by severity to different channels
- building escalation policies (warn → alert → page → fallback)
- debugging why an alert was not delivered or was missed

## Do NOT use this for
- lifecycle email or drip sequences (→ `lifecycle-email-sequences`)
- subscriber marketing or campaign email operations (→ `email-marketing-engine`)
- monitoring design, uptime checks, or threshold definition without delivery design as the primary task (→ `monitoring-ops`)
- chat moderation or broadcast announcements

## Severity model
| Level | Meaning | Default behavior |
|---|---|---|
| info | FYI, completion, low-risk change | quiet delivery (log file, daily digest channel), no escalation |
| warn | degraded state or recoverable issue | primary channel with visible notice, 30 min escalation timer |
| critical | service down, data loss, serious breakage | immediate multi-channel delivery + escalation within 5 min |

## Do this
1. **Define the trigger event** — what condition fires this alert? Be specific (e.g., "HTTP 5xx > 5% for 3 min" not "server issues"). Write the trigger as a boolean expression.
2. **Assign severity** — use the model above. Do not default everything to critical. Ask: "Does this need a human right now, or can it wait until morning?"
3. **Select channels** — pick 1–3 delivery surfaces per severity level. Never put a critical alert on only one channel. Use `references/alert-patterns.md` for standard configs.
4. **Define escalation** — if the alert is `warn` or `critical`, specify: primary channel, escalation delay, escalation channel, fallback, and how acknowledgement is detected. Write this as a numbered timeline (T+0, T+5min, etc.).
5. **Write the notification payload** — include: severity emoji/label, affected system/site, error description, timestamp, and acknowledgement instruction. See webhook payload examples in `references/alert-patterns.md`.
6. **Prove delivery** — fire a test alert through the full path using `scripts/send-alert.py` or a direct curl. Confirm receipt on every channel in the chain. For escalation, simulate an ack timeout and confirm the escalation fires.
7. **Log configuration** — write down what was configured: event, severity, channels, escalation timers, test result. Store in project ops log or `memory/` daily file.
8. **Review noise** — estimate alert frequency. If a rule will fire more than 3×/day on average, add deduplication or throttling before deploying.

## Routing rules
- `info` → single low-noise channel (log, digest, or quiet Slack channel). Never notify operators directly.
- `warn` → primary operator channel (Slack, Telegram). Escalate to email or second channel after 30 min if unacknowledged.
- `critical` → primary channel + secondary channel simultaneously. Escalate to on-call page after 5 min if unacknowledged. Final fallback: direct message to team lead.

## Escalation pattern
For `warn` and `critical` alerts, define this chain:
1. **T+0** — deliver to primary channel (e.g., Slack #ops-alerts)
2. **T+5min (critical) / T+30min (warn)** — escalate to secondary channel (e.g., Telegram operator group) if unacknowledged
3. **T+15min (critical) / T+60min (warn)** — escalate to fallback (e.g., direct message to team lead)
4. Acknowledgement = explicit reaction (e.g., Slack ✅ emoji) or `ack` command in channel

## Example 1: Site downtime alert (critical)
**Trigger:** uptime check returns HTTP 5xx or timeout for 2 consecutive checks (1 min interval).
**Severity:** critical
**Channels:** Slack `#ops-alerts` + Telegram `@ops-oncall` (simultaneous)
**Escalation:** If no ✅ reaction in Slack within 5 min → send SMS via Twilio to on-call number
**Acknowledgement:** Slack ✅ reaction on the alert message
**Test:** Run `python scripts/send-alert.py --severity critical --channel slack,telegram --message "TEST: site down alert dry run"` and confirm message appears in both channels within 30 seconds.

## Example 2: Deployment success notification (info)
**Trigger:** CI/CD pipeline completes `deploy-production` job with exit code 0.
**Severity:** info
**Channels:** Slack `#deploys` (quiet, no push notification)
**Escalation:** none
**Test:** Trigger a dry-run deployment notification and verify message appears in `#deploys` without triggering mobile push.

## Resources
- OpenClaw `message` tool — supports Telegram, Discord, Slack delivery
- `scripts/send-alert.py` — local helper for firing test alerts and real alerts via multiple channels
- `.secrets/notification.env` — credential store for webhook URLs and API keys (Slack incoming webhook, Telegram bot token, Twilio SID)
- Webhook provider docs: Slack (api.slack.com/messaging/webhooks), Telegram (core.telegram.org/bots/api)

## Checks and common mistakes
- **Single-channel critical alerts** — if that channel is down, you are blind. Always use 2+ channels for critical.
- **No test before relying on it** — always fire a test alert. Check actual delivery, not just "config looks right."
- **Alert fatigue** — more than 3 alerts/day to the same channel trains humans to ignore them. Throttle or deduplicate.
- **Silent credential failure** — if a webhook URL is expired or a bot token is revoked, the alert fails silently. Add a health check that verifies channel connectivity weekly.
- **Vague triggers** — "server issues" is not a trigger. "HTTP 5xx rate exceeds 5% for 3 minutes" is.
- **No acknowledgement mechanism** — without it, you cannot escalate. Define how ack works before deploying.
- **Missing log evidence** — log every alert send attempt with timestamp, channel, severity, success/failure. You need this to debug delivery failures.

## Output contract
**Artifact:** notification configuration document or script, including trigger definition, severity, channels, escalation timers, and acknowledgement method
**Evidence:**
- Test alert fired and confirmed received on every channel in the escalation chain (screenshot, log entry, or confirmation message)
- For webhook-based delivery: curl or HTTP response showing 200 OK from the webhook endpoint
- For escalation paths: simulate ack timeout and confirm escalation message fires to the secondary channel
**Decision:** routing policy approved and delivery path proved end-to-end, or blocked with reason (e.g., "Telegram bot token missing from .secrets/")
**Next:** connect alert to live monitoring source, tune thresholds, or add noise controls
**Line count target:** 100–130 lines for this file. Move payload examples, escalation configs, and channel setup to `references/`.
