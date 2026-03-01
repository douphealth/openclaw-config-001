# Enterprise Email Playbook v1 (SOTA)

## 1) Per-site strategy lock
For each site, define before writing any sequence:
- Core audience + pain map
- Offer ladder (free -> low-ticket -> core)
- Lifecycle stages (lead, nurture, buyer, customer, lapsed)
- Brand voice constraints

## 2) Sequence architecture (site-specific)
Mandatory flows:
1. Welcome (AIM)
2. Nurture
3. Sales/launch
4. Post-purchase onboarding
5. Re-engagement
6. Sunset/suppression

## 3) Deliverability SLOs (hard stop)
Pause sends automatically when:
- complaint rate > 0.1%
- hard bounce rate > 2%
- auth checks fail (SPF/DKIM/DMARC)

## 4) Proof standard
- No numeric/social-proof claim without verifiable source.
- If unverified, use non-numeric wording.

## 5) Personalization quality
- Use token defaults (e.g., {{first_name | default:"there"}})
- Validate token rendering before every send.

## 6) Test discipline
- One variable per test.
- Minimum sample threshold before winner declaration.
- Changelog required (hypothesis, variant, result, decision).

## 7) KPI tiers
Track by sequence + segment:
- Open rate
- CTR
- CTOR
- Unsubscribe
- Revenue/email
- Revenue/subscriber
- 12-month LTV contribution

## 8) QA protocol
Pre-send:
- audience/segment check
- link + tracking check
- mobile rendering check
- compliance/footer/unsub check
Post-send (24h):
- deliverability anomalies
- complaint/unsub spikes
- conversion delta

## 9) Exit logic (mandatory)
- Welcome exits on purchase.
- Sales exits on conversion.
- Nurture exits on inactivity threshold.
- Re-engagement exits to either active or sunset list.

## 10) Governance
- Author -> Reviewer -> Approver sequence required.
- Rollback path required before major campaign edits.
