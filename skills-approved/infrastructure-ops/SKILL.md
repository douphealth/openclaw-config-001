---
name: infrastructure-ops
description: Use when managing server infrastructure, deployments, DNS/SSL, backups, container/runtime operations, cron or scheduled automation, or other changes to infrastructure state that require rollback thinking and post-change verification.
---

# Infrastructure Ops

## Purpose
Handle infrastructure changes, deployment operations, and runtime/platform configuration with rollback discipline, verification, and documentation.

## Use this when
- configuring servers, DNS, SSL certificates, or runtime networking
- setting up Docker containers, compose stacks, or service processes
- automating deployments or scheduled tasks
- managing backups and disaster recovery operations
- changing infrastructure state or operational configuration
- repairing OpenClaw runtime, gateway, auth, provider, or channel plumbing

## Do NOT use this for
- WordPress plugin/content growth work (→ `wordpress-growth-ops`)
- email automation and lifecycle delivery (→ `email-marketing-engine`)
- monitoring or alerting as the primary task (→ `monitoring-ops` / `notification-engine`)
- pure verification work after a claimed fix (→ `auto-verification`)

## Do this

### 1. Assess current state
Before changing anything:
- What is running? (process list, container status, service health)
- What is the current configuration? (read the actual config, don't assume)
- What changed recently? (check logs, deployment history)

### 2. Define the change, risk, and rollback
- **Intended outcome:** what should be true after the change?
- **Risk level:** low (config tweak), medium (service restart), high (deployment, migration)
- **Rollback plan:** how to undo if it goes wrong? (config revert, container rollback, restore from snapshot)

### 3. Snapshot or back up state
For medium/high risk changes:
- Back up the config file before editing
- Snapshot the database before migration
- Tag the current container image before deploying

### 4. Apply the smallest viable change
- One change at a time. Don't bundle unrelated changes.
- Prefer config changes over code changes when both would work.
- Prefer rolling updates over big-bang deployments.

### 5. Verify the changed behavior
Don't trust command exit codes. Verify:
- The service is running (process health, container status)
- The service is reachable (HTTP check, port check, health endpoint)
- The expected behavior is present (the thing you changed actually works)
- No regressions (other services/features still work)

### 6. Document what changed
Record in `memory/YYYY-MM-DD.md` when the change matters:
- What was changed and why
- What proof confirmed success
- Rollback path if needed later

## Change categories and proof

| Category | What to verify after change |
|---|---|
| DNS / SSL | Real DNS lookup + certificate check + reachable endpoint |
| Deployment | Live service behavior (not just deploy logs) |
| Runtime / process | Process alive + health endpoint + expected output |
| Backup / recovery | Successful restore test or backup integrity check |
| Scheduled automation | Job exists + runs on schedule + produces expected effect |
| Container / compose | Container status (`docker ps`) + service reachability |

## Example: OpenClaw gateway scheduled task repair

**Context:** `openclaw status` reports gateway scheduled task is missing/stopped.

**Current state assessment:**
```powershell
# Check if scheduled task exists
Get-ScheduledTask -TaskName "OpenClaw*" -ErrorAction SilentlyContinue
# Check if gateway process is running
Get-Process | Where-Object { $_.ProcessName -match "node|openclaw" }
# Check gateway health
openclaw gateway status
```

**Change plan:**
- Intended: Gateway auto-starts on boot and restarts on crash
- Risk: Low (creates scheduled task, no config change)
- Rollback: `Unregister-ScheduledTask -TaskName "OpenClaw-Gateway" -Confirm:$false`

**Verification:**
1. Task exists: `Get-ScheduledTask -TaskName "OpenClaw-Gateway"` → returns task
2. Task runs: trigger it manually → `Start-ScheduledTask -TaskName "OpenClaw-Gateway"`
3. Gateway healthy: `openclaw gateway status` → reports running
4. Message flow: send a test message → received in Telegram

**Documentation:** Record fix in daily memory file with timestamp.

## Core rules
- Prefer the smallest safe change.
- Document intended change and rollback path before execution when risk is non-trivial.
- Verify the changed behavior, not just the command exit code.
- Treat restart success text as unproven until runtime behavior is confirmed.
- Pair important infrastructure changes with `auto-verification`.

## Resources
- Workspace `TOOLS.md` — local infrastructure notes, service inventory, and operational patterns
- OpenClaw docs at `C:\Users\<user>\AppData\Roaming\npm\node_modules\openclaw\docs`
- WordPress sites via WP REST API (credentials in `.secrets/wordpress-sites.json`)
- Cloud/provider tooling as available

## Checks and common mistakes
- Changing infra without defining rollback
- Trusting CLI success text without runtime proof ("command said restarted" ≠ restarted)
- Restarting services without checking real health after restart
- Applying multiple changes at once and losing causality (can't tell which change caused the issue)
- Forgetting to document important infra changes in memory files
- Not checking process list after "stop" commands (process might still be running)

## Output contract
**Artifact:** Infrastructure change summary with before/after state
**Evidence:** Verification proof — process status, health endpoint response, test message received, or equivalent concrete proof
**Decision:** Applied successfully, rolled back, blocked, or needs follow-up verification
**Next:** Monitoring period (watch for regressions), additional hardening, or document in memory
