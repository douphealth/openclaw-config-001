| name | description | version |
| :--- | :--- | :--- |
| wordpress-content-engine | High-velocity, enterprise-grade content orchestration for WordPress. Handles full-article generation (SOTA quality), multi-step editorial workflows, programmatic cluster expansion, semantic refresh logic, and automated media/asset integration. Use when drafting new pillars, scaling spokes, or performing bulk content refreshes based on SEO intelligence. | 3.0 |

# WordPress Content Engine

Advanced orchestration engine for high-signal, semantically-rich content generation and optimization.

## Own
- High-fidelity article drafting (H1-H6 hierarchy).
- Programmatic content expansion (topic cluster spokes).
- Semantic refresh logic (updating existing posts with new entities).
- Multi-step editorial \"Quality Gates\" (accuracy, tone, structure).
- Automated internal link injection (based on link graph intelligence).
- Metadata generation (Title, Meta, Excerpt, OpenGraph).
- Programmatic page generation and schema-ready formatting.

## Do NOT Own
- Keyword research / strategy (wordpress-seo-intelligence).
- Technical site maintenance (wordpress-technical-health).
- Monetization logic (affiliate-monetization).
- Direct social media distribution (automation-ops).

## Decision Matrix: Which Workflow to Run
| Signal | Workflow | Priority |
| :--- | :--- | :--- |
| SEO brief received from seo-intelligence | Full-Article Draft Mode | P1 |
| Content score below threshold (85+) | Semantic Refresh Mode | P0 |
| Cluster spoke missing from pillar | Spoke Generation Mode | P2 |
| Bulk post-update requested | High-Velocity Batch Mode | P1 |
| Content contains outdated statistics | Evidence Audit Mode | P1 |

## Workflow 1: Full-Article Draft Mode
1. **Brief Intake**: Parse SEO brief for entities, intent, and structure.
2. **First Pass (Structure)**: Generate H1-H4 hierarchy and section objectives.
3. **Second Pass (Depth)**: Expand sections with high-signal content, data-backed claims, and expert tone.
4. **Third Pass (Optimization)**: Inject semantic entities from NeuronWriter mapping.
5. **Quality Gate**: Run automated audit for citation accuracy and readability.

## Workflow 2: Semantic Refresh Mode
1. **Delta Mapping**: Identify entities missing from existing post vs current SEO intelligence.
2. **Contextual Injection**: Add missing entities naturally into existing paragraphs.
3. **Structural Upgrade**: Update headers or add new \"FAQ\" or \"Key Takeaways\" sections to match current intent.
4. **Score Verification**: Confirm new semantic score meets v3.0 standards (85+).

## Workflow 3: Spoke Generation Mode (Cluster Expansion)
1. **Pivot Analysis**: Identify sub-topic \"pivot\" from the Pillar page.
2. **Spoke Drafting**: Create short-form, highly focused \"spoke\" articles targeting long-tail intent.
3. **Cross-Linking**: Automatically include a contextual link back to the Pillar page.

## Success Indicators
- **Primary**: Post published with 85+ semantic score, 100% header alignment.
- **Secondary**: Reader engagement (dwell time), reduction in bounce rate, internal link density.
- **Operational**: < 5 min per full-article generation, zero hallucination incidents.

## Failure Modes & Recovery
| Failure Mode | Detection | Recovery | Prevention |
| :--- | :--- | :--- | :--- |
| Hallucination / Fact Error | Quality Gate audit | Manual review + fact-check script | Grounding via \"Reference\" files |
| Tone Drift (Too \"AI\") | Readability check | Re-draft with specific style constraints | Identity-level tone enforcement |
| Missing SEO Entities | Score check | Iterative injection | Brief-level entity requirements |
| Format Corruption (HTML) | Visual diff | Re-sanitize output | Strict Markdown-to-HTML pipeline |

## Integration Hooks
| This Skill Outputs | Target Skill / File |
| :--- | :--- |
| Published Post IDs | MEMORY.md (Daily log) |
| Optimization Metrics | STATUS.md |
| New Internal Links | wordpress-seo-intelligence |
| Media Requirements | wordpress-visual-assets |

## Measurement Protocol
- **Editorial Quality**: Pass/Fail on 10-point quality checklist.
- **Semantic Depth**: Number of secondary/tertiary entities included.
- **Speed to Market**: Total time from brief intake to publish-ready state.

## Anti-Patterns
- Drafting without an SEO brief.
- Over-using boilerplate intros/outros.
- Ignoring existing post context during a \"refresh\".
- Publishing without automated link/entity validation.


