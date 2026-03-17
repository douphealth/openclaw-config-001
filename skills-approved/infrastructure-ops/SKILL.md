---
name: infrastructure-ops
description: Enterprise infrastructure management: server configuration, deployment automation, DNS/SSL management, Docker containers, backup strategy, disaster recovery, performance optimization, and DevOps workflows. Use when managing servers, configuring deployments, setting up monitoring, handling backups, managing DNS/SSL, containerizing services, or automating DevOps workflows.
---

# Infrastructure Ops — Enterprise DevOps

## Purpose
Server infrastructure, deployment automation, and DevOps workflows for managed WordPress and web properties.

## When to Use
- Server configuration and optimization
- DNS/SSL certificate management
- Docker container setup and management
- Deployment automation and CI/CD
- Backup strategy and disaster recovery
- Performance optimization (server-level)
- Cron job scheduling and automation
- Cloudflare configuration
- WordPress hosting optimization

**Do NOT use for:** WordPress plugin/content management (→ `wordpress-growth-ops`), email automation (→ `email-marketing-engine`), application monitoring (→ `monitoring-ops`).

## Infrastructure Checklist

### Server Health
- CPU/Memory/Disk usage
- PHP version and configuration
- MySQL/MariaDB optimization
- Nginx/Apache configuration
- Object caching (Redis/Memcached)

### DNS & SSL
- DNS propagation verification
- SSL certificate validity and auto-renewal
- HSTS, CAA, and security headers
- CDN configuration (Cloudflare)

### Deployment
- Git-based deployment workflows
- Staging → production pipeline
- Database migration handling
- Rollback procedures

### Backup Strategy
- Automated daily backups (files + database)
- Off-site backup storage
- Backup restoration testing (quarterly)
- Disaster recovery documentation

### Performance
- Server response time optimization
- PHP-FPM tuning
- Database query optimization
- Static asset caching headers
- CDN cache configuration

## Operational Protocol
1. Assess current infrastructure state
2. Document planned changes
3. Backup before any changes
4. Apply with rollback plan ready
5. Verify post-change state
6. Document in memory/YYYY-MM-DD.md

## Performance Optimizations

### Speed Multipliers
- Parallel data fetching from multiple sources
- Pre-compute common metrics for the session
- Template-based reports and dashboards
- Batch API calls for platform operations
- Automated threshold alerts for significant changes

### Self-Critique Scorecard (/25)
1. **Functionality** (1-5): Does it work perfectly?
2. **Quality** (1-5): Enterprise-grade analysis?
3. **Verification** (1-5): Data validated from multiple sources?
4. **Speed** (1-5): Optimal execution?
5. **Learning** (1-5): Patterns documented?

**Target: 22+/25**

### Auto-Check
- [ ] Data quality validated before conclusions
- [ ] Comparison periods consistent
- [ ] Confidence levels stated
- [ ] Actionable recommendations provided
- [ ] Score logged to memory

## Output Contract
**Artifact**: Infrastructure change documentation, configuration files
**Evidence**: Before/after state, verification commands, health check results
**Decision**: Changes applied and verified
**Next**: Monitor for 24-48 hours post-change

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
