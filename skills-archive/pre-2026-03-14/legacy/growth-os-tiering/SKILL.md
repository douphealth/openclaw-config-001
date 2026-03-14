---
name: growth-os-tiering
description: Strategic content tiering, multi-channel distribution orchestration, and ROI-based resource allocation.
---

| name | description | version |
| --- | --- | --- |
| growth-os-tiering | Advanced tiering logic for content distribution and ROI-focused growth. Handles Tier 1-3 content prioritization, distribution channel mapping, and performance-based resource scaling. Use when planning content calendars, mapping distribution hooks, or auditing resource allocation across the funnel. | 3.0 |

# Growth OS Tiering

Scientific engine for content prioritization and distribution efficiency.

## Own

*   Content tiering (Tier 1: Pillars, Tier 2: Clusters, Tier 3: Support).
*   Multi-channel distribution strategy (Social, Email, Community).
*   Resource allocation based on ROI and conversion potential.
*   Funnel architecture mapping (TOFU/MOFU/BOFU alignment).
*   Growth-centric content scheduling and sequencing.
*   Performance tracking across distribution tiers.

## Do NOT Own

*   Affiliate link management (affiliate-monetization).
*   Direct SEO optimization (wordpress-seo-intelligence).
*   Content drafting or creative writing (wordpress-content-engine).
*   Visual asset generation (wordpress-visual-assets).

## Decision Matrix: Which Workflow to Run

| Signal | Workflow | Priority |
| :--- | :--- | :--- |
| New topical cluster initiation | Tiering Strategy Mode | P0 |
| Low ROI on Tier 2 content | Resource Re-allocation Mode | P1 |
| Monthly growth review | Performance Audit Mode | P1 |
| High-performing Tier 3 detected | Tier Elevation Mode | P2 |
| Distribution channel saturation | Channel Diversification Mode | P2 |

## Workflow 1: Tiering Strategy Mode

1. **Analysis**: Audit the topical authority gap for the proposed niche.
2. **Classification**: Assign every new topic to a Tier (1=Pillar, 2=Cluster, 3=Support).
3. **Resource Check**: Verify availability of internal links from supporting tiers to pillars.
4. **Actionable Output**: Propose a 30-day \"Growth Map\" with tiered prioritization.

## Success Indicators
* **Primary**: Increased ROI per content piece (Total Revenue / Content Cost).
* **Secondary**: Higher internal link density for Tier 1 pages.
* **Operational**: Zero Tier 3 content without a direct \"parent\" Tier 1/2.

## Failure Modes & Redundancy
| Failure Mode | Detection | Mitigation |
| :--- | :--- | :--- |
| Resource Drain | Tier 3 taking >20% manual time | Forced automation for support tiers |
| Orphaned Content | No parent pillar found | Immediate mapping or deletion |
| Channel Fatigue | Decreasing CTR on distribution | Rotate hooks or channels |

## Integration Hooks
| This Skill Outputs | Consumer Skill |
| :--- | :--- |
| Priority Tiers | wordpress-content-engine |
| Distribution Hooks | automation-ops |
| ROI Metrics | conversion-optimizer |

## Measurement Protocol
* **ROI Index**: Revenue generated per $100 spent on content.
* **Pillar Health**: Average ranking of Tier 1 pages.
* **Support Efficiency**: Volume of Tier 3 content published per week.

## Anti-Patterns
*   Treating all content as Tier 1 (Resource exhaustion).
*   Ignoring Tier 3 automation (Scalability bottleneck).
*   Distributing BOFU content to TOFU audiences.

## Scripts
*   `scripts/tiering_logic_audit.py`: Audits current content against tiering rules.
*   `scripts/roi_tracker.py`: Calculates revenue per content tier.
*   `scripts/distribution_mapper.py`: Automates hook generation for social/email.

## References
*   `references/tiering-framework.md`
*   `references/distribution-playbooks.md`
*   `references/growth-funnel-model.md`
