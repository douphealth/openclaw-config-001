---
name: wordpress-email-mastery-orchestrator
description: Orchestrate end-to-end WordPress email marketing execution by chaining infrastructure, list setup, welcome automation, copy quality, performance optimization, and continuous improvement. Use when deploying a complete email growth system on a WordPress site with enterprise safety and KPI verification.
---

# WordPress Email Mastery Orchestrator

## Scope Ownership
### Own
- Execute Orchestrate end-to-end WordPress email marketing execution by chaining infrastructure, list setup, welcome automation, copy quality, performance optimization, and continuous improvement. Use when deploying a complete email growth system on a WordPress site with enterprise safety and KPI verification.
- Apply workflows, gates, and outputs defined in this file and its references/scripts.

### Do Not Own
- Do not override responsibilities of more specific domain skills when one clearly matches.
- Do not claim completion for adjacent systems without their direct verification gates.

## Mission
Deploy a full email revenue system fast, safely, and measurably.

## Mandatory chain order
1. `wordpress-email-infrastructure-setup`
2. `wordpress-newsletter-list-setup`
3. `email-welcome-sequence-automation`
4. `email-human-copywriting-framework`
5. `email-ctr-openrate-optimization`
6. `email-sequence-improvement-engine`

References:
- orchestration map: `references/orchestration-map.md`
- premium QA: `references/premium-rollout-checklist.md`
- operating standard: `references/enterprise-email-playbook-v1.md`

## Execution profiles
- **Safe (default):** staged rollout with gate validation at each stage.
- **Aggressive (Alex-approved):** parallelize only non-destructive setup tasks.
- **Degraded:** timeout-safe narrow retries; no over-claims.

## Enterprise gates (all must pass)
A. Infrastructure: SMTP primary+fallback, SPF/DKIM/DMARC, inbox sanity  
B. List/compliance: double opt-in, consent logs, segmentation, suppression hygiene  
C. Sequence readiness: 5-email AIM, trigger/delay/exit logic, tracking  
D. **Cadence proof**: run UI-independent timing verification (`scripts/amfs_timing_proof.py`) and store report  
E. **KPI hygiene**: run test-contact suppression (`scripts/amfs_test_contact_suppression.py`) before KPI interpretation  
F. Copy quality: human readability, low-jargon, one-idea-per-email  
G. Performance loop: A/B subjects, send-time logic, KPI baseline + cadence  
H. UX/trust: safe placement, mobile validation, legal/consent clarity, no dark patterns  
I. Observability: evidence artifacts, exact IDs/settings, rollback path

## Operating rules
- Never send to unconfirmed contacts.
- Never use purchased lists.
- Never use deceptive urgency or fabricated outcomes.
- Keep transactional and marketing streams separated.
- Require explicit placement approval before intrusive capture inserts.
- Use staged rollout: one placement → verify → scale.
- Enforce stop rules for complaints/bounces/auth failures.
- Never mark done without verifiable proof.

## Required outputs
1. infrastructure verification report
2. list/consent/segmentation report
3. welcome automation map (trigger→exit)
4. copy package (subjects/preheaders/CTA variants)
5. KPI baseline + 30-day optimization plan
6. blockers + shortest unblock path

## Recovery protocol
If any gate fails:
1. stop next stage
2. log exact failing control
3. apply minimal rollback/fix
4. re-verify failed gate before continuing