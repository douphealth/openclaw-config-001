---
name: Email Marketing Engine
description: Complete email marketing system for deliverability, list growth, sequences, outreach, automation, analytics, and revenue optimization. Use when building or fixing end-to-end email performance operations.
---

# Email Marketing Engine (Execution Spec)

Run in strict order:
1) Deliverability baseline
2) List quality + segmentation
3) Sequence architecture
4) Campaign production
5) Automation wiring
6) Measurement + iteration

## 1) Deliverability baseline
- Validate SPF, DKIM, DMARC alignment.
- Verify domain and sending identity health.
- Check bounce/complaint thresholds before scaling sends.

## 2) List quality + segmentation
- Enforce consent-first capture + hygiene.
- Segment by lifecycle stage and intent.
- Suppress invalid, inactive, and test contacts.

## 3) Sequence architecture
- Maintain at minimum: welcome, nurture, promo, re-engagement.
- Define trigger, delay, branch, and exit criteria per sequence.
- Keep one clear conversion objective per sequence.

## 4) Campaign production
- Draft subject/preheader/body/CTA variants.
- Apply readability, scannability, and conversion clarity gates.
- Run seed/test send before production rollout.

## 5) Automation wiring
- Confirm triggers fire and event payloads are valid.
- Verify retry/fallback behavior for provider/API errors.
- Use reversible changes and preserve rollback path.

## 6) Measurement + iteration
- Track opens, CTR, CTOR, unsubscribes, complaints, bounce mix.
- Diagnose underperforming stages and propose one focused fix per cycle.
- Keep evidence-linked change log.

## Required output
- risk_status: green|yellow|red
- wins
- blockers
- KPI movement
- top 3 next actions
- evidence paths

## Hard constraints
- No fabricated KPI claims.
- No high-blast sending changes without approval.
- No compliance shortcuts.
