---
name: email-marketing-engine
description: Use when building or operating multi-sequence email automation systems, provider API delivery pipelines, subscriber lifecycle engines, or scalable email infrastructure that must be reliable beyond fragile CRM mailer defaults.
---

# Email Marketing Engine

## Purpose
Build reliable email automation systems with clear sequence architecture, provider-backed delivery, lifecycle state handling, and proof that the system actually sends what it is supposed to send.

## Use this when
- building a multi-sequence drip system from scratch
- integrating a provider API such as Brevo for delivery
- bypassing unreliable CRM mailer behavior for critical automation
- implementing subscriber lifecycle tracking and progression
- setting up instant signup delivery plus scheduled follow-up
- operating a scalable email engine beyond simple plugin defaults

## Do NOT use this for
- debugging an already-broken automation path as the main task (→ `email-automation-debugging`)
- writing lifecycle email copy (→ `lifecycle-email-sequences`)
- setting up the lead-capture front end itself (→ `lead-magnet-delivery-ops`)
- tracking/attribution implementation as the main task (→ `tracking-measurement`)

## Do this
1. Define the lifecycle model: trigger, sequences, progression logic, and success conditions.
2. Define the delivery layer: provider API, sender identity, templates, and unsubscribe handling.
3. Define system state: subscriber status, sequence progress, retries, and engagement fields.
4. Build the smallest end-to-end delivery path first.
5. Add scheduling, retries, and progression logic.
6. Verify delivery with fresh test subscribers and real provider proof.
7. Document the operating model so it can be maintained safely.

## Core rules
- Do not rely on fragile CRM mailer defaults for critical delivery when a provider API is the reliable path.
- Delivery proof and content proof are separate; verify both when relevant.
- State handling must be explicit; do not let sequence progress live only in assumptions.
- Verify links, sender state, and unsubscribe behavior before broad rollout.
- Prefer smart scanning or targeted progression over wasteful full-system scans when scale matters.

## Strong system components
A robust engine usually needs:
- sequence definitions and timing
- provider API integration
- subscriber lifecycle/state tracking
- retry/backoff logic
- template system
- link verification
- engagement tracking
- cron/scheduling model
- deliverability safeguards

## Resources
Read when needed:
- `references/brevo-api-guide.md`
- `references/email-template-standards.md`
- `references/sequence-architecture.md`
- `scripts/validate-email-links.py`

## Checks and common mistakes
- building the full system before proving one real working send path
- using broken SMTP/plugin defaults as if they are trustworthy
- skipping unsubscribe/list-unsubscribe handling
- not separating send failure from content/template failure
- not validating links before rollout
- not verifying with fresh subscribers

## Output contract
**Artifact:** email automation system design, implementation plan, or working engine components
**Evidence:** sequence model, delivery proof, link/template validation, and operating assumptions/limits
**Decision:** system design chosen, working, blocked, or needs staged rollout
**Next:** deploy, monitor deliverability, debug failures, or extend sequence coverage
