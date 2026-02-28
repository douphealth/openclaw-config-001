| name | description | version |
| :--- | :--- | :--- |
| competitor-intelligence | Strategic competitor entity auditing, SERP landscape analysis, and visibility gap detection. Monitors competitor content shifts, entity-coverage deltas, and ranking volatility to inform defensive and offensive content strategies. Use when auditing niche leaders, identifying new SERP features, or mapping competitor internal linking patterns. | 3.0 |

# Competitor Intelligence

Offensive engine for SERP landscape dominance and competitor entity deconstruction.

## Own
- Competitor entity auditing (identifying what they cover that we don't).
- SERP landscape analysis (monitoring AIO, People Also Ask, and Knowledge Panels).
- Content shift detection (noticing when competitors update key pillars).
- Ranking volatility monitoring within target clusters.
- Competitor backlink/internal link pattern mapping.
- Identifying \"Low-Hanging Fruit\" based on competitor weakness.

## Do NOT Own
- Direct SEO optimization for our site (wordpress-seo-intelligence).
- Content generation (wordpress-content-engine).
- Technical health (wordpress-technical-health).
- Backlink acquisition/outreach (automation-ops).

## Decision Matrix: Which Workflow to Run
| Signal | Workflow | Priority |
| :--- | :--- | :--- |
| Competitor launches new topical hub | Niche Penetration Mode | P1 |
| Drop in share of voice for brand terms | Defensive Audit Mode | P0 |
| New SERP feature (AIO) appears | SERP Evolution Mode | P1 |
| Monthly niche overview requested | Landscape Report Mode | P2 |
| Competitor ranking for high-intent entity | Entity Gap Mode | P1 |

## Workflow 1: Entity Gap Mode
1. **Target Selection**: Identify the top 3 ranking competitors for a primary keyword.
2. **Entity Extraction**: Use NeuronWriter or SERP-scraping to extract all entities covered by competitors.
3. **Delta Analysis**: Compare competitor entity list against our own Pillar/Spoke content.
4. **Actionable Output**: List specific sub-topics or entities we must add to regain topical authority.

## Workflow 2: SERP Evolution Mode
1. **Feature Scan**: Map the current SERP features (AIO, Video, Image, Local Pack) for a keyword set.
2. **Citation Mapping**: Identify which URLs are being cited in the AI Overview (AIO).
3. **Alignment Strategy**: Suggest content formatting changes (e.g., bulleted lists, direct answers) to secure citations.

## Workflow 3: Defensive Audit Mode
1. **Volatility Check**: Run ranking check for our top 20 money pages.
2. **Competitor Cross-Ref**: If we dropped, identify who moved up.
3. **Change Detection**: Analyze the content of the competitor who gained rank (recent updates, link velocity).
4. **Counter-Strategy**: Propose immediate content refresh or link injection.

## Success Indicators
- **Primary**: Increased \"Share of Voice\" in target niche, capture of new SERP features.
- **Secondary**: Higher entity-overlap scores with niche leaders, reduction in ranking gaps.
- **Operational**: Early detection of competitor content pivots (< 48 hours).

## Failure Modes & Recovery
| Failure Mode | Detection | Recovery | Prevention |
| :--- | :--- | :--- | :--- |
| Scraper Blocked | 403 / Captcha | Rotate proxy / use SERP API | Header randomization |
| Outdated SERP Data | Cache mismatch | Clear cache / force fresh crawl | Real-time API calls |
| Entity Misclassification | Low relevance score | Adjust NLP parameters | Better reference grounding |
| Competitor Obfuscation | Content hidden from bots | Use headless browser | Browser-mimicry scripts |

## Integration Hooks
| This Skill Outputs | Target Skill / File |
| :--- | :--- |
| Missing Entities | wordpress-seo-intelligence |
| Formatting Suggestions | wordpress-content-engine |
| Niche Volatility Alerts | HEARTBEAT.md |
| Competitive Benchmarks | MEMORY.md |

## Measurement Protocol
- **Entity Coverage Index**: % overlap with niche leaders.
- **SERP Feature Capture**: Number of non-standard features owned (AIO, PAA).
- **Competitor Response Time**: Time from competitor update to our detection.

## Anti-Patterns
- Copying competitor content exactly.
- Ignoring competitors outside the top 3.
- Relying on 3rd party tool metrics (DR/DA) over actual entity coverage.
- Failing to notice SERP feature shifts (e.g., from Text to Video).

## Scripts
- `scripts/competitor_entity_audit.py`: Multi-domain entity comparison.
- `scripts/serp_feature_tracker.py`: Automated AIO/PAA monitoring.
- `scripts/content_change_detector.py`: Notifies on competitor page updates.
- `scripts/sov_calculator.py`: Calculates Share of Voice for keyword clusters.

## References
- `references/niche-competitor-matrix.md`
- `references/serp-feature-optimization-guide.md`
- `references/entity-mapping-templates.md`
- `references/defensive-content-playbook.md`
