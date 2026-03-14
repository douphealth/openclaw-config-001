---
name: wordpress-email-infrastructure-setup
description: Set up production-grade WordPress email infrastructure with SMTP routing, SPF/DKIM/DMARC authentication, fallback providers, and deliverability verification. Use when initializing or fixing email delivery for WordPress sites.
---

# WordPress Email Infrastructure Setup

## Scope Ownership
### Own
- Execute Set up production-grade WordPress email infrastructure with SMTP routing, SPF/DKIM/DMARC authentication, fallback providers, and deliverability verification. Use when initializing or fixing email delivery for WordPress sites.
- Apply workflows, gates, and outputs defined in this file and its references/scripts.

### Do Not Own
- Do not override responsibilities of more specific domain skills when one clearly matches.
- Do not claim completion for adjacent systems without their direct verification gates.

## Objective
Deploy reliable, authenticated, encrypted WordPress email delivery.

## Mandatory order
1. install SMTP layer (FluentSMTP preferred)
2. configure primary + fallback providers
3. configure routing (transactional vs bulk)
4. apply DNS auth in order: SPF → DKIM → DMARC
5. verify deliverability + monitoring

## Setup standards
- prefer API/OAuth over password auth
- enforce TLS transport
- route transactional mail to high-reliability provider
- keep campaign/newsletter stream separate

## DNS gate
- do not enforce strict DMARC before SPF+DKIM are passing

## Verification gate
- plugin test send passes
- SPF/DKIM/DMARC validate
- inbox/mail-tester checks acceptable
- bounce/complaint monitoring enabled

## Output
- provider/routing map
- DNS records applied
- verification evidence
- residual risks + next actions