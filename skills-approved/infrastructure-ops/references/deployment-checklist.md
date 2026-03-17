# Deployment Checklist

Use before any deployment, migration, or significant infrastructure change.

## Pre-Deployment

- [ ] Define the intended outcome (what should be true after?)
- [ ] Identify risk level: low / medium / high
- [ ] Write rollback plan (how to undo in <5 minutes)
- [ ] Back up current config files
- [ ] Back up database if schema changes involved
- [ ] Tag current container/image version (if containerized)
- [ ] Check dependency compatibility (OS, runtime, library versions)
- [ ] Notify affected users if downtime expected

## Deployment

- [ ] Apply one change at a time (don't bundle unrelated changes)
- [ ] Use rolling update if possible (zero-downtime)
- [ ] Watch deployment logs for errors in real-time
- [ ] Stop immediately if unexpected errors appear (don't "push through")

## Post-Deployment Verification

- [ ] Process/service is running (`Get-Process`, `docker ps`, `systemctl status`)
- [ ] Health endpoint returns expected response
- [ ] HTTP check from external perspective (curl from another machine/network)
- [ ] Core user-facing functionality works (send a test request/message)
- [ ] No error spike in logs (check last 5 minutes of logs)
- [ ] Related services still healthy (database, cache, queue, external APIs)
- [ ] Monitoring alerts are active and firing correctly

## Rollback Triggers

Initiate rollback if ANY of these occur within 30 minutes:
- Error rate >5% above pre-deployment baseline
- Health check failures
- Core functionality broken
- Performance degradation >50%

## Rollback Procedure

1. Stop the new version
2. Restore previous config/image from backup/tag
3. Restart the service
4. Verify health and functionality
5. Document what happened and why rollback was needed

## Post-Mortem Documentation

Record in `memory/YYYY-MM-DD.md`:
- What was deployed
- What went right
- What went wrong (if anything)
- Rollback trigger hit (if applicable)
- Follow-up action items
