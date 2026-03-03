| name | description | version |
| :--- | :--- | :--- |
| wordpress-seo-intelligence | Strategic keyword/entity intelligence, Search Console gap analysis, NeuronWriter semantic optimization, internal link graph orchestration, and GEO/AEO alignment for WordPress. Use when analyzing ranking opportunities, optimizing content for semantic depth, performing competitor entity audits, or identifying internal linking deficiencies. | 3.0 |

# WordPress SEO Intelligence

Strategic engine for semantic search dominance, entity orchestration, and visibility intelligence.

## Own
- Keyword research and search intent classification.
- GSC (Google Search Console) gap analysis and traffic opportunity mapping.
- NeuronWriter API integration for semantic entity optimization.
- Internal link graph analysis and deficiency detection.
- GEO (Generative Engine Optimization) and AEO (Answer Engine Optimization) alignment.
- Competitor entity audits and SERP feature landscape analysis.
- Automated SEO brief generation and content cluster planning.

## Do NOT Own
- Technical site health / 5xx errors (wordpress-technical-health).
- Raw content drafting or creative writing (wordpress-content-engine).
- Affiliate link management (affiliate-monetization).
- Visual asset generation (wordpress-visual-assets).

## Decision Matrix: Which Workflow to Run
| Signal | Workflow | Priority |
| :--- | :--- | :--- |
| Organic traffic drop on top 50 pages | Gap Analysis Mode | P0 |
| Low semantic score (< 85) on key money pages | Semantic Optimization Mode | P1 |
| New topical cluster initiation | Cluster Strategy Mode | P1 |
| Unlinked high-authority pages found | Link Graph Mode | P2 |
| AIO/GEO citation loss for brand terms | AEO/GEO Response Mode | P1 |

## Workflow 1: Gap Analysis Mode (GSC Focused)
1. **Data Pull**: Query Search Console API for last 28 days vs previous 28 days.
2. **Prioritization**: Flag pages with > 5% traffic loss or CTR below 3% for high-impression terms.
3. **Intent Check**: Verify if search intent for top queries has shifted (Commercial vs Informational).
4. **Actionable Output**: List specific pages requiring meta-title, meta-description, or content depth updates.

## Workflow 2: Semantic Optimization Mode (NeuronWriter)
1. **Term Fetch**: Initialize NeuronWriter query for target keyword.
2. **Entity Audit**: Cross-reference existing content against NeuronWriter's recommended semantic keywords.
3. **Draft Enhancement**: Inject missing high-frequency entities without increasing spam score.
4. **Validation**: Target a minimum NeuronWriter score of 85+ before publishing.

## Workflow 3: Link Graph Mode
1. **Spider Crawl**: Map internal linking structure for target cluster.
2. **Deficiency Mapping**: Identify \"orphan\" pages or pages with low internal link counts (< 3).
3. **Anchor Selection**: Map exact-match and semantic anchor text from supporting posts to target \"Pillar\" page.
4. **Implementation**: Suggest specific link insertions with contextually relevant surrounding text.

## Success Indicators
- **Primary**: Improved semantic score (85+), increased top-3 keyword rankings.
- **Secondary**: CTR improvement, reduction in internal link \"orphans\", increased GEO/AEO citations.
- **Operational**: Zero over-optimization penalties, 100% semantic coverage for core money terms.

## Failure Modes & Recovery
| Failure Mode | Detection | Recovery | Prevention |
| :--- | :--- | :--- | :--- |
| NeuronWriter API Limit | 429 Error | Switch to Serper.dev/manual entities | Implement query caching |
| GSC Auth Failure | Empty result | Re-authenticate via TOOLS.md | Daily heartbeat check |
| Over-optimization (Spam) | Ranking drop | Revert to previous version via GitHub | Entity frequency capping |
| Internal Link Cannibalization | Multiple pages ranking | Consolidate spokes | Hub-and-spoke enforcement |

## Integration Hooks
| This Skill Outputs | Target Skill / File |
| :--- | :--- |
| SEO Content Briefs | wordpress-content-engine |
| Internal Link Suggestions | automation-ops |
| Top-performing queries | MEMORY.md (Learned facts) |
| Ranking Alerts | HEARTBEAT.md |

## Measurement Protocol
- **Semantic Coverage**: % of targeted posts with NeuronWriter score > 85.
- **CTR Delta**: Change in click-through rate for top-20 queries.
- **Entity Density**: Ratio of target entities to total word count (optimizing for depth, not density).

## Anti-Patterns
- Keyword stuffing without entity relevance.
- Creating clusters without internal linking to a pillar.
- Relying solely on SERP-scraping without GSC performance data.
- Ignoring mobile vs desktop intent differences.


