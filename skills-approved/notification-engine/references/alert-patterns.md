# Alert Patterns Reference

## Common escalation configurations

### Standard 3-tier escalation (most teams)
```
critical → Slack #ops (T+0) → Telegram oncall (T+5min) → SMS team lead (T+15min)
warn     → Slack #ops (T+0) → Email operator (T+30min)
info     → Slack #deploys (T+0, quiet)
```

### Two-person on-call rotation
```
critical → Slack #ops (T+0) → Telegram primary (T+5min) → Telegram secondary (T+15min) → Slack manager DM (T+30min)
warn     → Slack #ops (T+0)
info     → Log file only
```

### Solo operator setup
```
critical → Telegram DM + Email (T+0, simultaneous) → repeat every 10 min until ack
warn     → Telegram DM (T+0)
info     → Daily digest email
```

## Webhook payloads

### Slack incoming webhook
```json
{
  "text": "🔴 CRITICAL: Site gearuptofit.com returning 503",
  "channel": "#ops-alerts",
  "username": "AlertBot",
  "icon_emoji": ":rotating_light:",
  "attachments": [
    {
      "color": "danger",
      "fields": [
        { "title": "Severity", "value": "critical", "short": true },
        { "title": "Site", "value": "gearuptofit.com", "short": true },
        { "title": "Error", "value": "HTTP 503 - Service Unavailable", "short": false },
        { "title": "Time", "value": "2026-03-17T04:12:00Z", "short": true }
      ]
    }
  ]
}
```

### Telegram Bot API (sendMessage)
```
POST https://api.telegram.org/bot{BOT_TOKEN}/sendMessage
{
  "chat_id": "-100XXXXXXXXXX",
  "text": "🔴 CRITICAL: Site gearuptofit.com returning 503\n\nError: HTTP 503\nTime: 2026-03-17T04:12:00Z\nAck: reply with /ack",
  "parse_mode": "Markdown"
}
```

### Generic webhook (PagerDuty-style)
```json
{
  "event_action": "trigger",
  "dedup_key": "gearuptofit-503-20260317",
  "payload": {
    "summary": "gearuptofit.com: HTTP 503 for 3 min",
    "severity": "critical",
    "source": "uptime-monitor",
    "timestamp": "2026-03-17T04:12:00Z"
  }
}
```

## Notification channel setup checklist

### Slack
1. Create incoming webhook at https://api.slack.com/apps → Incoming Webhooks
2. Copy webhook URL to `.secrets/notification.env` as `SLACK_WEBHOOK_URL`
3. Test: `curl -X POST -H 'Content-Type: application/json' -d '{"text":"test alert"}' $SLACK_WEBHOOK_URL`
4. Verify: message appears in the target channel within 5 seconds

### Telegram
1. Create bot via @BotFather → `/newbot`, save token
2. Add bot to target group, send a message to the group
3. Get chat ID: `curl https://api.telegram.org/bot{TOKEN}/getUpdates`
4. Store as `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` in `.secrets/notification.env`
5. Test: `curl -X POST https://api.telegram.org/bot{TOKEN}/sendMessage -d 'chat_id={CHAT_ID}&text=test alert'`
6. Verify: message appears in the group

### Email (SMTP)
1. Configure SMTP credentials in `.secrets/notification.env`
2. Test with a script or `sendmail` command
3. Verify: email arrives in inbox (not spam) within 2 minutes

## Acknowledgement patterns

| Method | How it works | Reliability |
|---|---|---|
| Slack emoji reaction | Operator reacts with ✅ on alert message | High — visible, timestamped |
| Telegram /ack command | Bot listens for `/ack` reply in group | Medium — requires bot listening |
| Reply to alert | Any reply counts as ack | Medium — may false-positive on discussion |
| External dashboard | Operator marks resolved in UI | Low — requires context switch |

## Throttling / deduplication rules
- Suppress duplicate alerts for the same trigger within 15 minutes
- After 3 identical critical alerts in 1 hour, auto-escalate to manager regardless of ack
- Daily info digest: batch all info-level events, send once at 09:00 local time
