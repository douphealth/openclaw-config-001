# Priority Model

Scoring framework for ranking content opportunities by business value.
Use this to turn a long topic list into a prioritized publishing order.

## Scoring Dimensions (1-5 Scale)

### 1. Business Value (Weight: ×3)
How directly does this topic support revenue, leads, or strategic goals?

| Score | Criteria |
|-------|----------|
| 5 | Directly drives revenue (bottom-funnel, product comparison, pricing) |
| 4 | Strongly supports revenue (middle-funnel, solution-aware content) |
| 3 | Indirectly supports revenue (top-funnel, builds authority, drives traffic) |
| 2 | Weak business connection (nice-to-know, tangential) |
| 1 | No clear business path (pure entertainment, off-brand) |

### 2. Search Demand (Weight: ×2)
Is there meaningful search volume or distribution potential?

| Score | Criteria |
|-------|----------|
| 5 | High volume (>1,000/mo) OR strong social/share potential |
| 4 | Moderate volume (500-1,000/mo) with growing trend |
| 3 | Decent volume (200-500/mo) or clear long-tail cluster |
| 2 | Low volume (50-200/mo) but relevant niche |
| 1 | Very low/no volume (<50/mo) and no alternative distribution |

### 3. Competition / Achievability (Weight: ×2)
Can we realistically rank or compete for this topic?

| Score | Criteria |
|-------|----------|
| 5 | Low competition (KD < 20) OR competitors have thin/outdated content |
| 4 | Moderate competition (KD 20-35) but we have topical authority |
| 3 | Moderate competition (KD 20-35), neutral authority |
| 2 | High competition (KD 35-50) with strong incumbents |
| 1 | Very high competition (KD > 50) with major authority sites dominating |

### 4. Intent-to-Conversion Alignment (Weight: ×2)
Does the search intent match our conversion path?

| Score | Criteria |
|-------|----------|
| 5 | Transactional intent → direct product/service page |
| 4 | Commercial investigation → comparison/review that leads to our offer |
| 3 | Informational → builds trust, captures email, retargeting pixel |
| 2 | Informational → very top of funnel, long path to conversion |
| 1 | Navigational or off-intent for our goals |

### 5. Effort / Production Cost (Weight: ×1, Inverse)
How much work to create this content well? (Lower effort = higher score)

| Score | Criteria |
|-------|----------|
| 5 | Template/listicle format, existing research, <4 hours |
| 4 | Standard article format, some research needed, 4-8 hours |
| 3 | Long-form guide, original research or screenshots, 8-16 hours |
| 2 | Original data study, interviews, custom graphics, 16-40 hours |
| 1 | Major production: video, interactive tool, full redesign, 40+ hours |

## Priority Score Calculation

```
Priority = (Business × 3) + (Demand × 2) + (Competition × 2) + (Intent × 2) + ((6 - Effort) × 1)
```

**Maximum score:** (5×3) + (5×2) + (5×2) + (5×2) + (5×1) = 15 + 10 + 10 + 10 + 5 = **50**
**Minimum score:** (1×3) + (1×2) + (1×2) + (1×2) + (1×1) = 3 + 2 + 2 + 2 + 1 = **10**

## Priority Tiers

| Tier | Score Range | Action | Cadence |
|------|-----------|--------|---------|
| **P0 — Publish Now** | 40-50 | Create immediately | This week |
| **P1 — Next Sprint** | 30-39 | Schedule for next publishing cycle | Next 2 weeks |
| **P2 — Planned** | 20-29 | Add to backlog, schedule when capacity allows | Next 1-2 months |
| **P3 — Nice to Have** | 10-19 | Keep in backlog but deprioritize | When everything else is done |

## Weight Calibration

The default weights (3/2/2/2/1) assume a revenue-focused content strategy. Adjust for different goals:

**Lead generation focus:** Increase Business Value to ×4, reduce Demand to ×1
**Authority building:** Increase Demand to ×3, reduce Business to ×2
**New site (no authority):** Increase Competition to ×3 (prioritize low-KD wins)
**Limited resources:** Increase Effort weight to ×2 (favor quick wins)

## Quick Priority Calculator (Manual)

For each topic, fill out this table:

| Topic | Biz | Demand | Comp | Intent | Effort | **Score** |
|-------|-----|--------|------|--------|--------|-----------|
| "How to fix [problem]" | 3 | 4 | 4 | 3 | 4 | **36** |
| "Best [tool] for [use case]" | 5 | 5 | 3 | 5 | 3 | **44** |
| "[Tool] review" | 4 | 4 | 3 | 4 | 3 | **40** |
| "What is [concept]" | 2 | 5 | 4 | 2 | 4 | **32** |

## Cross-Check Questions (After Scoring)

Before finalizing priority order:
1. **Does the P0 list have variety?** (Mix of intent types, not all transactional)
2. **Are there quick wins in P1?** (High-demand, low-effort topics that can fill gaps)
3. **Are there authority builders in P2?** (Pillar content that takes time but strengthens everything)
4. **Is the publishing cadence realistic?** (Can we actually produce P0 content at the planned rate?)
5. **Are dependencies accounted for?** (Does topic B need topic A published first for internal linking?)

## Learning Loop

After each publishing cycle, revisit scores:
- Did the P0 topics perform as predicted? (Traffic, conversions, rankings)
- Which dimension's predictions were most accurate? Least accurate?
- Adjust weights and scoring criteria based on real performance data.
- Document learnings in this file for future calibration.
