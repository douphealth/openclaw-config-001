| name | description | version |
| :--- | :--- | :--- |
| affiliate-monetization | High-conversion affiliate orchestration, product comparison logic, automated link health monitoring, and transactional intent optimization for WordPress. Handles product review structures, comparison table generation, and multi-network affiliate link management with zero dead-link tolerance. Use when building money pages, optimizing CTAs, or managing product-centric content clusters. | 3.0 |

# Affiliate Monetization

Strategic engine for high-yield affiliate conversion and product-centric revenue orchestration.

## Own
- Product review orchestration (data-driven comparison).
- Automated comparison table generation (pros, cons, specs).
- Affiliate link management (health checks, cloaking logic).
- Transactional intent optimization (CTA placement, button text).
- Amazon Product Advertising API integration (pricing, availability).
- Multi-network revenue tracking (mapping clicks to content).
- Compliance auditing (disclosure enforcement, no-follow attributes).

## Do NOT Own
- Informational content generation (wordpress-content-engine).
- SEO keyword research (wordpress-seo-intelligence).
- General site automation (automation-ops).
- Brand asset creation (wordpress-visual-assets).

## Decision Matrix: Which Workflow to Run
| Signal | Workflow | Priority |
| :--- | :--- | :--- |
| High-intent keyword identified | Money Page Mode | P1 |
| Affiliate link returns 404/OOS | Link Rescue Mode | P0 |
| Low CTR on existing comparison tables | Conversion Optimization Mode | P1 |
| New product launch in target niche | Product Review Mode | P1 |
| Quarterly monetization audit | Compliance Audit Mode | P2 |

## Workflow 1: Money Page Mode
1. **Product Selection**: Identify top 3-5 high-margin affiliate products for the target intent.
2. **Data Harvesting**: Pull specs, pricing, and unique selling points (USPs) for each product.
3. **Table Generation**: Build responsive comparison tables with \"Winner\" badges and clear CTAs.
4. **Link Injection**: Place cloaked/no-follow affiliate links in high-visibility zones.
5. **Validation**: Confirm FTC disclosure is present and links are functional.

## Workflow 2: Link Rescue Mode
1. **Health Check**: Periodically scan all outbound affiliate links for 404s or \"Out of Stock\" (OOS) indicators.
2. **Fallback Selection**: If a product is unavailable, find the closest high-converting alternative.
3. **Automated Replacement**: Update link and product name across all affected posts.
4. **Logging**: Record the change in MEMORY.md for future audit.

## Workflow 3: Conversion Optimization Mode
1. **Heatmap Analysis**: (Simulated) Identify low-performing CTA zones.
2. **A/B Variation**: Generate 3 variations of CTA button text (e.g., \"Check Price\" vs \"Buy Now\" vs \"View Deal\").
3. **Implementation**: Deploy winning variation based on historical click data.

## Success Indicators
- **Primary**: Increased Click-Through Rate (CTR) on affiliate links, zero dead affiliate links.
- **Secondary**: High conversion on comparison tables, 100% compliance score.
- **Operational**: < 2 min for link rescue operations, automated pricing accuracy.

## Failure Modes & Recovery
| Failure Mode | Detection | Recovery | Prevention |
| :--- | :--- | :--- | :--- |
| API Token Expiry | 401 Error | Re-auth via TOOLS.md | Token expiry heartbeat |
| Product Discontinued | 404 / Scraper alert | Swap with alternative | Proactive stock monitoring |
| Disclosure Missing | Compliance script | Auto-insert disclosure | Pre-publish quality gate |
| Link Tracking Break | 0 clicks reported | Verify tracking pixel/ID | Daily click-sanity check |

## Integration Hooks
| This Skill Outputs | Target Skill / File |
| :--- | :--- |
| Monetized Post IDs | MEMORY.md |
| Revenue Opportunities | wordpress-seo-intelligence |
| Link Health Reports | HEARTBEAT.md |
| Product Data Sheets | wordpress-content-engine |

## Measurement Protocol
- **Conversion Efficiency**: Clicks per 1000 visitors.
- **Link Availability**: % of affiliate links returning 200 OK.
- **Compliance Rate**: % of money pages with correct disclosures.

## Anti-Patterns
- Using direct affiliate links without no-follow/sponsored attributes.
- Promoting low-quality products solely for high commission.
- Ignoring \"Out of Stock\" alerts on top-performing pages.
- Placing CTAs too far below the fold.


