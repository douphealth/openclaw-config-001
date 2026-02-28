| name | description | version |
| :--- | :--- | :--- |
| conversion-optimizer | Enterprise-grade conversion rate optimization (CRO), A/B testing orchestration, user intent alignment, and psychological trigger implementation for WordPress. Handles multivariate testing of CTAs, headline performance audits, and friction-point reduction across the conversion funnel. Use when optimizing landing pages, improving micro-conversions, or aligning content with deep-funnel psychological needs. | 3.0 |

# Conversion Optimizer

Scientific engine for behavioral alignment and conversion funnel maximization.

## Own
- A/B testing orchestration (headlines, CTAs, button colors).
- User intent alignment (mapping page content to stages of awareness).
- Psychological trigger implementation (scarcity, authority, social proof).
- Friction-point reduction (form optimization, page speed impact on CRO).
- Micro-conversion tracking (newsletter signups, internal link clicks).
- Heatmap-driven layout adjustments (simulated via behavioral data).
- Conversion-centric copywriting audits.

## Do NOT Own
- Direct affiliate link management (affiliate-monetization).
- Broad content drafting (wordpress-content-engine).
- SEO keyword strategy (wordpress-seo-intelligence).
- Visual asset design (wordpress-visual-assets).

## Decision Matrix: Which Workflow to Run
| Signal | Workflow | Priority |
| :--- | :--- | :--- |
| High traffic but low conversion (< 1%) | Funnel Audit Mode | P0 |
| New landing page deployment | CRO Hardening Mode | P1 |
| CTA performance drop | Multivariate Test Mode | P1 |
| High bounce rate on money pages | Awareness Alignment Mode | P1 |
| Monthly conversion review | Performance Optimization Mode | P2 |

## Workflow 1: Funnel Audit Mode
1. **Friction Mapping**: Identify where users drop off in the conversion path.
2. **Intent Verification**: Ensure page content matches the user's \"Stage of Awareness\" (Problem Aware vs Solution Aware).
3. **Trigger Check**: Verify presence of 3 core psychological triggers (Authority, Social Proof, Reciprocity).
4. **Actionable Output**: Propose specific structural changes to increase \"Add to Cart\" or \"Click to Affiliate\" actions.

## Workflow 2: Multivariate Test Mode
1. **Hypothesis Generation**: Create 3 testable hypotheses based on low-performing elements.
2. **Variation Drafting**: Generate alternate headlines or CTA text with different emotional hooks.
3. **Implementation**: Deploy variations via specialized CRO plugins or custom code blocks.
4. **Analysis**: Monitor CTR delta and identify statistically significant winners.

## Workflow 3: Awareness Alignment Mode
1. **Search Intent Sync**: Cross-reference the ranking keyword's intent against the page's CTA.
2. **Contextual Refinement**: If the intent is informational, shift the primary CTA from \"Buy\" to \"Download Guide\" (Micro-conversion).
3. **Pathing**: Ensure a clear logical path exists from informational discovery to transactional conversion.

## Success Indicators
- **Primary**: Increased Conversion Rate (CR), higher Revenue Per Visitor (RPV).
- **Secondary**: Higher micro-conversion rates, increased scroll depth, improved engagement metrics.
- **Operational**: Zero \"Conversion Cannibalization\", 100% trigger coverage on money pages.

## Failure Modes & Recovery
| Failure Mode | Detection | Recovery | Prevention |
| :--- | :--- | :--- | :--- |
| Statistical Noise | Inconclusive test | Extend test duration | Minimum sample size gating |
| Negative Impact | CR drops significantly | Immediate rollback to baseline | Small-batch canary testing |
| Implementation Error | Broken CTA link | Fix link via TOOLS.md | Pre-test functional audit |
| Tracking Failure | 0 conversions logged | Re-verify GTM/Pixel setup | Real-time tracking heartbeat |

## Integration Hooks
| This Skill Outputs | Target Skill / File |
| :--- | :--- |
| Winning Headlines | wordpress-content-engine |
| High-performing CTAs | affiliate-monetization |
| Behavioral Insights | MEMORY.md |
| CR Anomalies | HEARTBEAT.md |

## Measurement Protocol
- **Conversion Delta**: % change in primary conversion action.
- **RPV Index**: Revenue generated per 100 sessions.
- **Friction Score**: Number of steps required to complete a conversion.

## Anti-Patterns
- Testing too many elements simultaneously (Confusing results).
- Ignoring mobile user experience in CRO tests.
- Over-using scarcity triggers (Reducing brand trust).
- Aligning high-friction CTAs with top-of-funnel informational intent.

## Scripts
- `scripts/cro_hypothesis_generator.py`: Data-backed test planning.
- `scripts/ab_test_analyzer.py`: Statistical significance calculator.
- `scripts/friction_point_scanner.py`: Detects layout issues blocking conversion.
- `scripts/trigger_audit_tool.py`: Scans for psychological engagement factors.

## References
- `references/conversion-psychology-framework.md`
- `references/stages-of-awareness-model.md`
- `references/high-performance-copy-patterns.md`
- `references/cro-testing-standard-operating-procedure.md`
