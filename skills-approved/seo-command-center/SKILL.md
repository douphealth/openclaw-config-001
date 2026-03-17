---
name: seo-command-center
description: Use when a request requires cross-cutting SEO work spanning multiple specialized skills — audits, content planning, editorial optimization, schema, programmatic SEO, or monitoring. Routes to the smallest SEO workflow that fits. Triggers on site-wide SEO plans, multi-domain SEO strategy, "do our SEO" requests, or when the right next SEO skill is unclear.
---

# SEO Command Center

## Purpose
Coordinate cross-cutting SEO work by routing to the smallest effective combination of specialized SEO skills instead of treating SEO as one vague bucket.

## Use this when
- the request spans multiple SEO domains (technical + content + schema, etc.)
- a site-wide or cross-cutting SEO plan is needed
- keyword strategy, audits, editorial optimization, schema, and monitoring may all be relevant
- the right next SEO skill is not obvious from the request alone
- someone says "do our SEO" or "SEO audit" without specifying scope

## Do NOT use this for
- single-page SEO tasks that clearly fit one specialized skill (route directly)
- direct content writing (→ `editorial-post-enhancement` or `conversion-copywriting`)
- routine monitoring-only work (→ `monitoring-ops`)

## Routing rules

| Request type | Route to |
|---|---|
| Technical/site audit, crawl issues, cannibalization, internal linking | `seo-audit-playbook` |
| Keyword research, clustering, content gaps, editorial roadmap | `content-strategy-planning` |
| Article/page optimization and publish-quality upgrades | `editorial-post-enhancement` |
| Structured data, rich snippets, JSON-LD markup | `schema-ops` |
| Scaled template/page-system design, programmatic page generation | `programmatic-seo-blueprints` |
| Rank tracking, movement alerts, SERP monitoring | `monitoring-ops` |
| Revenue site funnel or monetization path fixes | `revenue-site-execution` |

## Do this

### 1. Define the SEO goal and scope
- What site(s)? What pages? What's the business goal (traffic, leads, revenue)?
- Is this a diagnosis (find problems) or execution (fix/improve) request?

### 2. Route to one skill if possible
If the request clearly fits one skill above, route directly and stop. Don't over-engineer.

### 3. Build an ordered workflow if multi-skill
If multiple skills are needed, define the minimum sequence:

**Common workflow patterns:**

Pattern A — Site audit + content plan:
1. `seo-audit-playbook` → find technical issues and cannibalization
2. `content-strategy-planning` → build keyword/content roadmap based on audit findings
3. `editorial-post-enhancement` → execute top-priority content items

Pattern B — New site launch SEO:
1. `content-strategy-planning` → keyword strategy and page structure
2. `schema-ops` → structured data for all page types
3. `monitoring-ops` → set up rank tracking from day one

Pattern C — Ranking recovery:
1. `seo-audit-playbook` → diagnose the drop (technical? content? algorithm?)
2. Based on findings, route to the specific fix skill
3. `monitoring-ops` → track recovery

### 4. Require evidence at each step
Each routed skill must return actionable findings with proof — not vague recommendations.

### 5. Stop routing when scope narrows
Once the task is specific enough for one skill, route and stop orchestrating.

## Example: "Our traffic dropped 40%, fix our SEO"

**Scope analysis:** Unknown cause — could be technical, content, or algorithmic. Multi-skill workflow needed.

**Workflow:**
1. **`seo-audit-playbook`** — Full technical + content audit. Check: crawl errors, indexation drops, Core Web Vitals, cannibalization, recent content changes, backlink profile. Return: diagnosed cause(s) with evidence.
2. **Based on findings:**
   - If technical issues → `infrastructure-ops` for fixes, then `auto-verification`
   - If content/cannibalization → `content-strategy-planning` for consolidation plan
   - If thin content → `editorial-post-enhancement` for priority pages
   - If schema issues → `schema-ops`
3. **`monitoring-ops`** — Set up recovery tracking on affected keywords.

**Routing decision:** Start with `seo-audit-playbook`. Do NOT jump to content creation before diagnosing the cause.

## Core rules
- Always check cannibalization before content expansion recommendations.
- Do not call SEO work complete without real evidence (rankings, crawl data, indexation status).
- Do not keep routing after the correct specialized skill is clear.
- Keep orchestration lightweight — don't create SEO bureaucracy with unnecessary handoffs.

## Resources
- `references/seo-orchestration-rules.md` — detailed routing decision tree and workflow templates
- `references/output-templates.md` — standardized output formats for cross-skill SEO workflows
- `references/search-visibility-data-pack.md` — required GSC/Bing data slices before SEO diagnosis or prioritization
- `skill-router` — use when the request may cross into non-SEO domains (e.g., SEO + paid media + email)

## Checks and common mistakes
- Routing broad SEO requests into too many skills up front (scope creep)
- Treating one page task like a site-wide program
- Mixing diagnosis with implementation without clear handoff
- Giving content recommendations before cannibalization review
- Saying "SEO complete" when only one layer was checked
- Not checking Google Search Console data before making indexation claims

## Output contract
**Artifact:** SEO routing decision or ordered SEO workflow with skill sequence and rationale
**Evidence:** Scope assessment tied to site state and request type; routing justified by the routing rules table
**Decision:** Exact SEO skill(s) to run, in order, with clear handoff points
**Next:** Execute the selected skill(s) in sequence; verify outcomes where applicable; loop back if findings change the scope
