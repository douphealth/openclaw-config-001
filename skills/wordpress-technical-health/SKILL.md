---
name: wordpress-technical-health
description: Monitor and maintain WordPress core, plugin, and server-side health.
---

# WordPress Technical Health

## Scope
- Plugin/Theme updates and compatibility audits.
- Error log monitoring (PHP, MySQL).
- Performance benchmarking (LCP, FID, CLS).
- Security hardening (WAF, login protection).

## Legacy Mapping
- wp-reliability-ops.md, multisite-watchdog.md.

## Execution Protocols
1. **Health Check:** Run weekly site audits for broken links and 404s.
2. **Resource Audit:** Verify hosting resources (CPU/RAM) are sufficient for traffic spikes.
3. **Backup Verification:** Ensure daily automated backups are valid.
