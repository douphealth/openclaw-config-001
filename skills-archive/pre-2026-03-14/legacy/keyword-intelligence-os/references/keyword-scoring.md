# Keyword Scoring (Enterprise Rubric)

Score each candidate from 1-5 on:
1. Intent fit (weight 2.0)
2. Business value (weight 1.5)
3. Topical authority fit (weight 1.2)
4. SERP attainability (weight 1.0)
5. AI extractability potential (weight 1.0)
6. Cannibalization risk (inverse, weight -1.0)

## Formula
Priority Score =
(2.0*IntentFit) +
(1.5*BusinessValue) +
(1.2*AuthorityFit) +
(1.0*Attainability) +
(1.0*AIExtractability) -
(1.0*CannibalizationRisk)

## Tiers
- 11.0+ => Tier A (execute now)
- 9.0-10.9 => Tier B (next wave)
- 7.0-8.9 => Tier C (supporting terms)
- <7.0 => Park/Discard

## Scoring notes
- Intent fit below 3 is auto-disqualifying for target URL.
- High cannibalization risk requires merge/re-scope before execution.
- Favor terms with clear solve-intent and conversion adjacency.
