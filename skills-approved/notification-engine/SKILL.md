---
name: notification-engine
description: Enterprise notification and alerting system for agent-driven communication. Use when setting up push notifications, email alerts, Telegram/Discord messages, Slack pings, SMS alerts, or any automated notification pipeline for business events. Triggers on notification setup, alert configuration, channel routing, escalation logic, or notification quality improvement.
---

# Notification Engine — Enterprise Alerting & Communication

## Purpose
Build reliable notification pipelines that deliver the right message to the right channel at the right time without noise.

## When to Use
- Setting up push notifications or email alerts
- Configuring channel routing (Telegram, Discord, Slack, Email, SMS)
- Building escalation logic for critical alerts
- Reducing notification noise or improving alert relevance
- Connecting business events to agent notifications

**Do NOT use for:** Email marketing campaigns (→ `email-marketing-engine`), monitoring setup (→ `monitoring-ops`), workflow automation (→ `workflow-macros`).

## Notification Framework

### Channel Selection Matrix
| Channel | Speed | Attention | Best For |
|---------|-------|-----------|----------|
| Telegram/Discord | Instant | High | Critical alerts, urgent actions |
| Slack/Teams | Instant | Medium | Team notifications, updates |
| Email | Delayed | Low-Medium | Summaries, digests, non-urgent |
| SMS | Instant | Very High | Security alerts, time-sensitive |
| In-app | On-demand | Low | Status updates, historical logs |

### Severity Routing
| Severity | Channel | Format | Response Time |
|----------|---------|--------|--------------|
| Critical | Telegram + SMS | Title + Impact + Action | Immediate |
| High | Telegram/Discord | Title + Impact | Within 1 hour |
| Medium | Discord/Slack | Brief summary | Batch in digest |
| Low | Email/Digest | Daily summary | Review at next check |

### Message Format Template
Every notification should include:
1. **Title**: One-line summary (what happened?)
2. **Severity**: Critical / High / Medium / Low
3. **Impact**: Business consequence
4. **Evidence**: Key data points
5. **Action**: What should the recipient do?
6. **Link**: Deep link to dashboard/details if available

### Notification Rules
1. **Batching**: Group related notifications (don't send 10 separate alerts)
2. **Quiet hours**: Respect time zones (no alerts 22:00-07:00 local)
3. **Escalation**: If no response in X time, escalate to higher channel
4. **Dedup**: Don't send the same alert twice within 1 hour
5. **Feedback loop**: Track notification open/response rates
6. **Test mode**: Always test new alerts with one recipient before broad rollout

### Escalation Flow
```
Alert fires → Send to primary channel
  ↓
No response in 15 min → Escalate to secondary channel
  ↓
No response in 30 min → Escalate to SMS/phone
  ↓
No response in 1h → Log incident, notify backup contact
```


## Self-Critique Scorecard (/25)
After every operation, score yourself:

| Dimension | Score | Notes |
|-----------|-------|-------|
| **Functionality** (1-5) | ? | Does it work perfectly and meet all requirements? |
| **Quality** (1-5) | ? | Is it enterprise-grade and production-ready? |
| **Verification** (1-5) | ? | Was it verified via multiple methods? |
| **Speed** (1-5) | ? | Was execution optimal with parallel operations? |
| **Learning** (1-5) | ? | Were new patterns documented and memory updated? |

**Target: 22+/25 before claiming completion**

### Pre-Flight Checklist
- [ ] Credentials verified and target exists
- [ ] Rollback plan identified
- [ ] Success criteria defined
- [ ] Anti-patterns reviewed

### Post-Flight Checklist
- [ ] Verified via API response + live check
- [ ] Quality score logged to memory/YYYY-MM-DD.md
- [ ] Skill references updated if new patterns discovered
- [ ] No common mistakes made

## Output Contract
**Artifact**: Notification configuration, message template, or alert pipeline
**Evidence**: Test notification received on correct channel with correct content
**Decision**: Notification pipeline active
**Next**: Monitor delivery and response rates for 1 week, tune thresholds

## Anti-Patterns
- ❌ Alert storms: 50+ notifications per hour (fatigue)
- ❌ Channel mismatch: critical alerts buried in email
- ❌ No severity routing (everything treated as "urgent")
- ❌ Missing context: "something went wrong" without details
- ❌ No escalation path for unacknowledged alerts
- ❌ Sending test alerts to entire team

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
