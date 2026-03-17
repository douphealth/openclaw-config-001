---
name: paid-media-audit
description: Use when auditing Google Ads, Meta Ads, Microsoft Ads, or paid acquisition for wasted spend, tracking problems, structural issues, bidding mistakes, creative gaps, audience problems, or scale readiness. Triggers on ad account audits, CAC problems, wasted spend reviews, campaign diagnostics, account takeovers, or "why is paid underperforming?".
---

# Paid Media Audit

## Purpose
Find the highest-impact paid media problems before more budget gets wasted.

## Use this when
- diagnosing or auditing paid acquisition performance on Google, Meta, Microsoft, or other platforms
- reviewing ad accounts for wasted spend, structural issues, or tracking problems
- investigating CAC inflation, ROAS decline, or scaling plateaus
- taking over an existing ad account
- asked "why is paid underperforming?"

## Do NOT use this for
- setting up tracking (→ `tracking-measurement`)
- general analytics reporting (→ `analytics-reporting`)
- landing page or offer fixes (→ `revenue-site-execution`, `offer-positioning`)

## Do this

### 1. Check measurement quality first
Before judging any performance metric:
- Confirm conversion actions are firing correctly (not double-counting, not missing)
- Check attribution window and model settings
- Verify pixel/CAPI health (Meta) or enhanced conversions (Google)
- If tracking is broken, flag it as a prerequisite — don't audit spend until measurement is reliable

### 2. Audit account structure
- Campaign organization: does it match business goals or is it a historical mess?
- Ad group/asset group granularity: too broad wastes budget, too narrow fragments data
- Budget distribution: where is money actually going vs. where results come from?
- Naming conventions: can you understand the account in 60 seconds?

### 3. Audit bidding and budgets
- Bid strategy vs. objective alignment (e.g., tCPA on a campaign with 3 conversions/month is broken)
- Budget pressure: are campaigns budget-capped and losing impression share?
- Learning phase resets: recent changes that killed accumulated data

### 4. Audit audiences and targeting
- Search term waste (Google): what % of spend goes to irrelevant queries?
- Placement waste (Meta/Display): where are ads actually showing?
- Audience overlap and cannibalization between campaigns
- Exclusion lists: are existing customers/converters excluded?

### 5. Audit creative
- Creative fatigue: are CTR and conversion rate declining over time?
- Coverage: enough variants per ad group to rotate?
- Message-market fit: does the ad promise match the landing page?

### 6. Diagnose efficiency vs. scale
- **Efficiency problem:** CAC too high, ROAS too low → fix waste, targeting, creative
- **Scale problem:** efficient but can't spend more → expand audiences, new channels, raise budgets
- Don't apply efficiency fixes to a scale problem or vice versa

## Example: Google Ads account takeover

**Context:** E-commerce brand, $45k/month spend, ROAS dropped from 4.2x to 1.8x over 3 months.

**Findings:**
| Priority | Issue | Impact | Fix |
|---|---|---|---|
| P1 | 38% of spend on broad match with no negative keyword list | ~$17k/mo waste | Add 200+ negatives, switch top campaigns to phrase match |
| P1 | Conversion tracking double-counting (GA4 + Google tag both firing) | ROAS inflated ~40% | Deduplicate conversion actions, use single source of truth |
| P2 | All campaigns on tROAS with only 12 conversions/mo | Bidding on noise | Switch to manual CPC until 30+ conversions/mo per campaign |
| P2 | No customer exclusion list | Paying for existing customers | Upload customer list, exclude from acquisition campaigns |
| P3 | Only 2 ad variants per group, both 90+ days old | Creative fatigue | Launch 3 new variants with updated hooks |

**Expected impact:** P1+P2 fixes → estimated ROAS recovery to 3.0-3.5x within 4 weeks.

## Core rules
- Do not judge paid performance without checking measurement quality first.
- Separate structural issues from strategy issues from creative issues.
- Flag budget waste, learning resets, and poor optimization signals explicitly.
- Diagnose using recent data (last 30-90 days), but look for trend shifts and change-history clues.
- Avoid fake precision on upside projections ("estimated" not "guaranteed").

## Resources
- `references/audit-priority-stack.md` — priority framework for audit findings
- `references/portfolio-paid-diagnosis.md` — multi-account diagnosis patterns
- Platform-specific: Google Ads Editor, Meta Ads Library, Google Analytics 4

## Checks and common mistakes
- Giving generic "test more creatives" advice without identifying the actual gap
- Ignoring landing page mismatch when diagnosing ad performance
- Confusing lead volume with lead quality (cheap leads ≠ good leads)
- Calling an account healthy just because CTR looks fine
- Not checking for conversion tracking inflation before trusting ROAS/CPA numbers
- Applying brand campaign metrics to performance campaign evaluation

## Output contract
**Artifact:** Ad account audit report with prioritized findings
**Evidence:** Specific data points (spend waste %, conversion counts, impression share loss, ROAS with/without tracking correction), sourced from platform reports
**Decision:** Action plan ranked by projected business impact, with estimated timeline
**Next:** Implement P1 fixes, verify tracking correction, monitor for 2-4 weeks, reassess
