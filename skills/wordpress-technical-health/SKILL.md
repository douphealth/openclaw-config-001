---
name: wordpress-technical-health
description: Site reliability, performance budgets, technical auditing, incident response, regression monitoring, security hardening, and CDN/edge optimization for WordPress. Use when auditing CWV/indexation/schema/canonical, responding to incidents, handling degraded runtime, enforcing performance budgets, resolving plugin conflicts, running recurring health checks, or hardening security posture.
version: 3.0
---

# WordPress Technical Health

## Own
HTTP health, canonical/indexation, robots/sitemap, schema validation, CWV enforcement, plugin/theme integrity, incident response, reliability under degraded conditions, multi-site regression monitoring, security hardening, CDN/edge optimization, performance budgets.

## Do NOT Own
Content quality (wordpress-content-engine), keyword/entity optimization (wordpress-seo-intelligence), monetization (wordpress-monetization), data analysis (analytics-intelligence).

## Decision Matrix: Which Workflow to Run
| Signal | Workflow | Priority |
| :--- | :--- | :--- |
| Site down / 5xx / homepage broken | Incident Mode | P0 |
| Canonical corruption / robots blocking crawlers | Incident Mode | P0 |
| CWV regression on key templates | Performance Mode | P1 |
| New site onboarding / quarterly review | Full Audit Mode | P1 |
| Timeouts / cache variance / API flakiness | Reliability Mode | P1 |
| Recurring health check (daily/weekly) | Multi-site Health Check | P2 |
| CDN/cache misconfiguration | Edge Optimization | P2 |
| Security concern / suspicious behavior | Security Hardening | P0/P1 |

## Workflow 1: Full Audit Mode
### Phase 1: Inventory
Build per-site profile:
- Domain, stack (theme, builders), SEO plugin, cache/CDN, image pipeline.
- Post types, taxonomies, template hierarchy, top 50 URLs by traffic.
- Current sitemap structure, robots.txt rules, canonical strategy.

### Phase 2: Systematic Audit
Run `scripts/wp_management_audit.py` against top URLs.

#### Layer 1: Crawl & Indexation (Most Critical)
- `robots.txt` accessible, no unintended disallows, no conflicting directives.
- XML sitemap loads, valid, includes all intended URL types, excludes thin/utility.
- Canonical tags present, self-referential unless intentional consolidation.
- No contradictory "noindex + canonical" combinations.
- No orphan money pages (in sitemap but zero internal links).
- No duplicate URL variants indexed (www/non-www, trailing slash, HTTP/HTTPS).

#### Layer 2: Head Integrity
- Single canonical per page (no duplicates from plugin conflicts).
- Title present, unique per URL, intent-aligned, 50-65 chars.
- Meta description present, unique, 145-160 chars.
- No conflicting OG/Twitter tags vs canonical.
- `hreflang` correct if multilingual.

#### Layer 3: Schema & Structured Data
Run `scripts/schema_validator.py` per template type:
- Homepage: `Organization`, `WebSite` (+ `SearchAction` if valid).
- Blog posts: `Article`, `BreadcrumbList`.
- Review/comparison: `Review`, `Product` (only when real product entity).
- FAQ pages: `FAQPage` (only when visible FAQ exists).
- Local: `LocalBusiness`, `Geo`.
- Validate: no duplicate schema, no hidden/invisible FAQ schema, no spam.

#### Layer 4: Performance (CWV)
Per key template (homepage, blog post, category, money page):
- LCP < 2.5s (target 1.8s)
- INP < 200ms (target 150ms)
- CLS < 0.1 (target 0.05)
- TTFB < 800ms
- No render-blocking resources in critical path.
- Image optimization (next-gen formats, proper sizing, lazy-load below fold).

#### Layer 5: Security
- HTTPS enforced with valid certificate.
- Security headers: HSTS, X-Content-Type-Options, X-Frame-Options, CSP.
- WordPress admin: strong passwords, 2FA, limited admin accounts.
- Plugin audit: no abandoned plugins (>2yr no update), no known vulnerabilities.
- File permissions: `wp-config.php` not publicly readable.
- XML-RPC disabled if not needed.
- Login URL obscured or rate-limited.

#### Layer 6: Architecture
- Internal link "dead zones" (pages with < 2 inbound internal links).
- Redirect chains (max 1 hop).
- Thin pages (template-generated pages with < 200 words).
- Pagination: `rel=next/prev` or load-more, crawlable.
- Breadcrumbs present, accurate hierarchy.

### Phase 3: Severity Classification & ICE Scoring
For each finding:
```yaml
finding: "description"
severity: "critical|high|medium|low"
affected: "template|specific URLs|sitewide"
blast_radius: "high (homepage/money)|medium (category/template)|low (individual post)"
ice_score: 0 # Impact(1-10) * Confidence(1-10) * Ease(1-10)
fix: "rollback verification dependencies"
```

### Phase 4: Execution
Execute in ICE-score order within severity bands (critical first regardless of ICE). For each fix: backup → atomic change → dual verify → log.

## Workflow 2: Incident Mode
**Trigger:** Site down, source code leakage, broken templates, mass canonical corruption, plugin conflict causing render failure, security breach.

### Containment (First 5 Minutes)
1. **Freeze ALL non-essential writes** across the portfolio.
2. **Snapshot affected state** (database, files, CDN config).
3. **Map blast radius:**
   - Homepage: HTTP status, render, canonical, schema.
   - Top 5 money pages: same checks.
   - Top 3 templates: sample 1 URL each.
4. **Classify:** total outage, partial degradation, data corruption, security breach.

### Diagnosis
| Symptom | Check First | Check Second |
| :--- | :--- | :--- |
| White screen / 500 | `wp-config.php` integrity | Active plugins / PHP error log |
| Source code visible | Theme file corruption | `functions.php` |
| Canonical corruption | SEO plugin settings | Recent bulk edit / Theme injection |
| Layout broken | Theme update / page builder | CSS/JS minification / CDN cache |
| Login broken | `.htaccess` / plugin conflict | Security plugin lockout / file perms |
| Malware/redirect | File integrity scan | Database injection / user audit |

### Recovery
1. **Revert** latest risky change (`git revert` / file restore / plugin rollback).
2. **Purge ALL cache layers** (plugin cache, CDN, browser hints).
3. **Validate** homepage + 3-5 critical URLs.
4. **Verify** head output (canonical, schema).
5. **Reopen writes ONLY** after stable verification (3 consecutive checks, 5 min apart).

### Closure
- Before/after evidence for every affected URL.
- Root cause confirmed (not hypothesized).
- Prevention step implemented (not just documented).
- Residual risk assessment with monitoring plan.
- Timeline: detection → containment → diagnosis → recovery → closure.

## Workflow 3: Reliability Mode
**Trigger:** Timeouts, cache/render mismatch, slug-to-ID mismatch, flaky APIs.

### Failure Classification
| Class | Symptoms | Resolution |
| :--- | :--- | :--- |
| Network | Intermittent timeouts, resets | Retry with backoff, reduce batch size |
| Cache | Source correct, live stale | Purge specific URL cache, verify after TTL |
| Mapping | Slug resolves to wrong ID | Query REST by slug, cross-ref frontend postid |
| Payload | REST returns unexpected shape | Validate response schema, check plugin interference |
| Auth | 401/403 on REST endpoints | Verify app password, check role, test nonce |
| Plugin | Intermittent failures | Isolate by disabling suspect plugin, test, re-enable |

### Execution Protocol
1. **Classify** failure type BEFORE attempting fixes.
2. **Resolve Identity** before writes (slug → REST ID → frontend postid alignment).
3. **Two-layer verification:**
   - Source truth: REST context/edit raw content.
   - Live truth: frontend render markers (title, canonical, schema).
4. **Parallel reads, sequential atomic writes.**
5. If live is flaky but raw is correct (degraded), retry failed URLs only.

### Retry Policy
| Context | Max Retries | Backoff | Escalation |
| :--- | :--- | :--- | :--- |
| Standard URL | 3 | Exponential (2s, 4s, 8s) | Mark degraded |
| Critical URL | 5 | Exponential (2s, 4s, 8s, 16s, 32s) | Alert Alex |
| Batch failure | 30% URLs fail | 60s cooldown | Stop batch, diagnose |
| Auth failure | 2 | 5s | Stop all writes, check credentials |

### Cache Variance Protocol
- NEVER claim breakage from a single-signal canonical miss.
- Require DUAL confirmation: head parse + alternate fetch (different user-agent or cache-bust).
- If signals conflict: label `monitor-only`, recheck in 30 min.
- Three consecutive matching failures required before declaring regression.

## Workflow 4: Performance Mode
**Trigger:** CWV regression on key templates, new plugin adding render-blocking resources.

### Performance Budget (per template)
| Metric | Budget | Action if Exceeded |
| :--- | :--- | :--- |
| LCP | < 2.5s (target 1.8s) | Optimize image/font/server response |
| INP | < 200ms (target 150ms) | Audit JS execution, reduce main thread blocking |
| CLS | < 0.1 (target 0.05) | Add dimensions to images/embeds, fix shifts |
| Total JS | < 300KB (compressed) | Audit plugins, defer non-critical scripts |
| Total CSS | < 100KB (compressed) | Remove unused CSS, inline critical CSS |
| Hero image | < 200KB | Compress, resize, use next-gen format |
| TTFB | < 800ms | Server optimization, edge caching, reduce queries |

### Regression Detection
- After any plugin install, theme change, or template modification:
- Run PageSpeed Insights API against 3 URLs per affected template.
- Compare against stored baseline (analytics-intelligence).
- If any metric exceeds budget: rollback change immediately.
- If metric degraded but within budget: flag for monitoring.

## Workflow 5: Multi-site Health Check
For EACH site in portfolio, check in order:
1. **Tier 1: Existence (stop if fail):** Homepage HTTP 200, renders, no PHP leak, title present, `robots.txt` accessible, sitemap loads.
2. **Tier 2: Integrity:** Homepage canonical self-referential, top 3 money pages canonical match, schema present.
3. **Tier 3: Performance:** Homepage LCP within budget, no new render-blocking resources.
4. **Tier 4: Compliance:** Affiliate disclosure present, no clickbait/fearbait titles.

Severity: `critical` (Tier 1/2 fail), `degraded` (Tier 3 fail), `monitor` (Tier 4 fail).

## Workflow 6: Security Hardening
Run quarterly or after any concern:
- All core/plugins current (no abandoned plugins).
- Admin accounts minimum necessary, strong passwords, 2FA enabled.
- File permissions: `wp-config.php` (440), uploads (755).
- HTTPS valid cert, HSTS header, no mixed content.
- Login protection (rate limiting, obscure URL).
- XML-RPC disabled, REST API auth required for writes.
- Automated backup system tested (restore within 4 hours).

## Failure Modes & Recovery
| Failure Mode | Detection | Recovery | Prevention |
| :--- | :--- | :--- | :--- |
| Plugin conflict | Visual diff / 500 error | Deactivate plugin, verify | Staging tests |
| Stale cache | Live truth mismatch | Purge specific URL cache | Post-save hook |
| Canonical corruption | Audit script (selfmatch=false) | Rollback SEO plugin | Pin versions, test |
| Performance regression | Budget exceeded | Remove/defer script | Performance gate |
| robots.txt block | Audit shows disallow | Restore from version control | Review changes |
| Schema failure | Validator reports errors | Revert template change | Schema test |

## Integration Hooks
| This Skill Outputs | Feeds Into |
| :--- | :--- |
| Audit findings with severity/ICE | `portfolio-growth-ops` (priority queue) |
| CWV baselines per template | `analytics-intelligence` (tracking) |
| Schema validation results | `wordpress-seo-intelligence` (optimization) |
| Broken internal links | `wordpress-content-engine` (repair queue) |
| Security findings | `portfolio-growth-ops` (P0 escalation) |
| Incident post-mortems | `quality-assurance` (lesson extraction) |

## Measurement Protocol
- **Health Gate Pass Rate:** % of URLs passing all health gates (target > 95%).
- **MTTD:** Mean time to detect incidents (target < 15 min).
- **MTTR:** Mean time to recover from incidents (target < 60 min).
- **CWV Pass Rate:** % across portfolio (target > 90%).
- **Critical findings resolved within 24h.**

## Anti-Patterns
- Running full-site audit when only one template is affected (waste).
- Claiming site is healthy after checking only homepage (insufficient).
- Upgrading all plugins simultaneously (impossible to isolate regressions).
- Purging all caches as first troubleshooting step (masks real problem).
- Ignoring CWV on mobile (most traffic is mobile).
- Adding security plugins without measuring performance impact.


