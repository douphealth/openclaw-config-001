---
name: infrastructure-ops
description: Use when managing server infrastructure, configuring deployments, setting up monitoring, handling backups, managing DNS/SSL, containerizing services, or automating DevOps workflows.
---

# Infrastructure Ops

## Purpose
Server infrastructure, deployment automation, and DevOps workflows.

## Use this when
- Configuring servers, DNS, SSL certificates
- Setting up Docker containers or compose stacks
- Automating deployments
- Managing backups and disaster recovery
- Monitoring server health and performance
- Setting up cron jobs and scheduled tasks

**Do NOT use this skill for:** WordPress plugin management or site-level growth work (→ `wordpress-growth-ops`), email automation setup and delivery pipelines (→ `email-marketing-engine`), or application-level monitoring and alerting (→ `monitoring-ops`).

## Do this
1. Assess current infrastructure state
2. Document changes before applying
3. Test in staging when possible
4. Apply changes with rollback plan
5. Verify after changes
6. Document what was done

## Resources
- Server access via SSH (check TOOLS.md for details)
- WordPress sites managed via WP REST API
- Cloudflare for DNS management
- Brevo for email infrastructure


## Output Contract
**Artifact**: Infrastructure change documentation
**Evidence**: Before/after state, verification steps
**Decision**: Changes applied successfully
**Next**: Monitoring period
## Checks
- Always backup before changes
- Verify DNS/SSL after modifications
- Test deployments before declaring success
- Document all infrastructure changes in memory/YYYY-MM-DD.md
