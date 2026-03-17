---
name: monitoring-ops
description: Enterprise monitoring and alerting for search rankings, uptime, Core Web Vitals, brand mentions, competitor intelligence, multisite health, social listening, AI visibility, and technical health. Use when tracking keyword movements, watching site availability, monitoring brands or competitors, aggregating health across multiple sites, detecting technical risk signals, defining alert thresholds, or building monitoring dashboards.
---

# Monitoring Ops — Enterprise Site & Search Monitoring

## Purpose
Proactive monitoring and alerting across all managed properties: rankings, uptime, performance, mentions, competitors, and AI visibility.

## When to Use
- Rank tracking and keyword movement alerts
- Uptime monitoring and availability checks
- Brand mention tracking and social listening
- Competitor intelligence and change detection
- Multisite health aggregation
- Core Web Vitals and performance monitoring
- AI search visibility tracking (GEO/AEO)
- Technical health signals (SSL, DNS, CDN, error rates)
- Alert threshold definition and escalation

**Do NOT use for:** SEO auditing (→ `seo-audit-playbook`), tracking implementation (→ `tracking-measurement`), schema markup (→ `schema-ops`).

## Monitoring Dimensions

### 1. Search Rankings
- Track target keywords by domain → position → daily delta
- Alert on: rank drop ≥3 positions, new competitor entering top 5, featured snippet loss
- Tools: SERP API, Google Search Console API, manual checks

### 2. Uptime & Performance
- Monitor HTTP status, response time, SSL expiry
- Alert on: uptime <99.5%, response time >3s, SSL expiry <14 days
- Core Web Vitals: LCP >2.5s, CLS >0.1, INP >200ms → flag

### 3. Brand & Competitor Intelligence
- Brand mentions across web, social, news
- Competitor content changes (new pages, price changes, new features)
- Alert on: mention volume spike >2σ, competitor launches new product/page

### 4. Multisite Health (Portfolio Mode)
- Iterate all managed sites → health check each → aggregate → alert on issues
- Check: HTTP status, response time, WordPress health, plugin errors, disk space

### 5. AI Visibility (New)
- Track brand/product mentions in AI search results (Perplexity, ChatGPT, Gemini)
- Monitor GEO/AEO signals: FAQ schema presence, Speakable markup, content freshness
- Alert on: brand disappearing from AI answers for key queries

## Alert Configuration

| Signal | Threshold | Severity | Action |
|--------|-----------|----------|--------|
| Rank drop | ≥3 positions | High | Check competitors, audit page |
| Uptime | <99.5% over 24h | Critical | Check hosting, CDN, DNS |
| Response time | >3s average | Medium | Check caching, optimize |
| SSL expiry | <14 days | Critical | Renew certificate |
| Core Web Vitals | 2+ metrics failing | Medium | Optimize assets, defer scripts |
| Brand mention spike | >2σ volume | Low | Review sentiment, engage |
| Competitor new page | Top-10 competitor | Low | Evaluate threat, respond |
| AI visibility loss | Brand missing from AI answers | Medium | Update content, add schema |

## Performance Optimizations

### Speed Multipliers
- Parallel data fetching from multiple sources
- Pre-compute common metrics for the session
- Template-based reports and dashboards
- Batch API calls for platform operations
- Automated threshold alerts for significant changes

### Self-Critique Scorecard (/25)
1. **Functionality** (1-5): Does it work perfectly?
2. **Quality** (1-5): Enterprise-grade analysis?
3. **Verification** (1-5): Data validated from multiple sources?
4. **Speed** (1-5): Optimal execution?
5. **Learning** (1-5): Patterns documented?

**Target: 22+/25**

### Auto-Check
- [ ] Data quality validated before conclusions
- [ ] Comparison periods consistent
- [ ] Confidence levels stated
- [ ] Actionable recommendations provided
- [ ] Score logged to memory

## Output Contract
**Artifact**: Monitoring configuration, alert setup, or health dashboard
**Evidence**: Alert firing test, escalation path verified, data source confirmed
**Decision**: Monitoring active with appropriate thresholds
**Next**: Review alert quality after 1 week, tune thresholds

## Compatibility
- Targets current WordPress 6.9+ where applicable
- REST API + WP-CLI preferred over browser automation
- Batch operations via `_fields` + `per_page=100` + `concurrent.futures`
- Browser automation only when API/CLI insufficient

## Inputs Required (Pre-Flight)
Before executing any task in this skill:
1. **Target identification** — What site, page, post, or system is being operated on?
2. **Auth verification** — Confirm credentials work (test API call or CLI command)
3. **Current state** — Understand what exists before making changes (GET before POST)
4. **Environment** — Production vs staging (assume production unless stated)
5. **Constraints** — No downtime? Preserve SEO? Preserve data? Budget limits?

## Triage Protocol
Before ANY operation:
1. **Identify** — What type of content/system/problem is this?
2. **Check state** — Query current state via API/CLI before modifying
3. **Verify creds** — Confirm authentication works
4. **Plan rollback** — How to undo if something breaks?
5. **Scope check** — Is this a single item or batch? Scale determines approach.

## Speed Optimizations
- **API calls**: Always use `_fields` parameter (80%+ payload reduction)
- **Pagination**: Use `per_page=100` for list endpoints
- **Parallelism**: Use `concurrent.futures` for independent operations (max 10/site)
- **Caching**: Store results in session — never re-fetch same data
- **Batching**: Group similar operations into single API calls where possible
- **Direct CLI**: Use WP-CLI `wp db query` for complex operations

## Error Recovery (Auto-Learning)
- Track error patterns — after 2 failures, try alternative approach
- Log recurring fixes to `memory/YYYY-MM-DD.md`
- Update references when new patterns discovered
- Rollback plan: Know how to undo before making changes

## Self-Critique Scorecard (/25)
Before claiming complete, score yourself:
1. **Triage** (1-5): Was current state fully understood before changes?
2. **Execution** (1-5): Was the operation clean, efficient, correct?
3. **Verification** (1-5): Was the result verified via API/live check?
4. **Rollback** (1-5): Can changes be undone if issues found?
5. **Learning** (1-5): Were new patterns documented for future use?

**Target: 22+/25**

## Output Contract
- **Artifact**: What was created/changed/deleted
- **Evidence**: API response proof + live verification
- **Decision**: Success/failure with reasoning
- **Next**: What follow-up is needed (if any)
