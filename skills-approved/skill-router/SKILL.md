---
name: skill-router
description: Use FIRST when unsure which skill to use, when a task spans multiple skills, or when optimizing workflow efficiency. Routes work to the optimal skill or skill combination.
---

# Skill Router

## Purpose
Intelligent routing layer that maps tasks to optimal skills, prevents overlap confusion, and enables multi-skill workflows with minimal token waste.

## How to Use
1. Read the incoming task or request
2. Check the Decision Tree below for the closest match
3. Load that single skill (not multiple)
4. If multi-step, follow the Multi-Skill Workflows section
5. When truly unsure, read the frontmatter of 2-3 candidate skills before committing

## Use this when
- Unsure which skill handles a task
- Task spans multiple skills
- Optimizing token efficiency across skills
- Building multi-step workflows

## Do NOT use this for
- Actually executing the task (route, then load the target skill)
- Tasks with an obvious single skill match (just load it directly)
- Simple questions that don't require a skill

## Do this

### 1. Route by Task Type
| User Intent | Load This Skill |
|------------|----------------|
| "Write new page/copy" | conversion-copywriting |
| "Improve existing article" | editorial-post-enhancement |
| "Plan content topics" | content-strategy-planning |
| "SEO audit" | seo-audit-playbook |
| "Add/improve schema" | schema-ops |
| "Debug email automation" | email-automation-debugging |
| "Set up email marketing" | email-marketing-engine |
| "Design email drip" | lifecycle-email-sequences |
| "Verify checkout/funnel" | money-path-verification |
| "Pre-launch check" | launch-readiness-audit |
| "Build API integration" | api-integration-builder |
| "Run site tests" | test-automation-ops |
| "Set up alerts" | notification-engine |
| "Server/DevOps work" | infrastructure-ops |
| "Improve WordPress site" | wordpress-growth-ops |
| "Analyze/report data" | analytics-reporting |
| "Fix tracking" | tracking-measurement |
| "Audit ad spend" | paid-media-audit |
| "Position an offer" | offer-positioning |
| "Design a funnel" | service-funnel-architecture |
| "Write documentation" | technical-writing |
| "Set up alerts/monitoring" | notification-engine + monitoring-ops |
| "Server/DevOps work" | infrastructure-ops |
| "Analyze/report data" | analytics-reporting |
| "Fix tracking/pixels" | tracking-measurement |
| "Audit ad spend/PPC" | paid-media-audit |
| "Run site tests/QA" | test-automation-ops |
| "Compare tools" | tool-evaluation |
| "Design A/B test" | experiment-tracking |
| "Create lead magnet" | lead-magnet-delivery-ops |
| "Build pSEO pages" | programmatic-seo-blueprints |
| "Multi-worker coordination" | swarm-orchestrator |
| "Manage memory/notes" | memory-operations |
| "Create/edit skills" | skill-authoring-standard |
| "Host/publish files to web" | here-now |
| "Edit/improve existing copy" | copy-editing-sweeps |
| "Full SEO operations" | seo-command-center |

### 2. Route by Site
| Site | Primary Skills | Secondary |
|------|---------------|-----------|
| frenchyfab.com | wordpress-growth-ops, email-marketing-engine | conversion-copywriting, tracking-measurement |
| affiliatemarketingforsuccess.com | revenue-site-execution, email-automation-debugging | analytics-reporting, money-path-verification |
| profitplaybook.com | revenue-site-execution, schema-ops | seo-audit-playbook, tracking-measurement |

### 3. Multi-Skill Workflows (load in order)
- **New content E2E**: content-strategy-planning → conversion-copywriting → editorial-post-enhancement → schema-ops → wordpress-growth-ops
- **SEO fix**: seo-audit-playbook → schema-ops → editorial-post-enhancement
- **Email system**: email-marketing-engine → lifecycle-email-sequences → tracking-measurement
- **Site launch**: launch-readiness-audit → money-path-verification → tracking-measurement → notification-engine
- **Content refresh**: seo-audit-playbook → editorial-post-enhancement → schema-ops
- **Paid media fix**: paid-media-audit → tracking-measurement → analytics-reporting
- **Service funnel build**: offer-positioning → service-funnel-architecture → conversion-copywriting → money-path-verification
- **Full site rebuild**: seo-audit-playbook → content-strategy-planning → conversion-copywriting → schema-ops → wordpress-growth-ops → launch-readiness-audit

### 4. Ambiguous Requests — Tiebreakers
When a request could map to 2+ skills:
- Copy involved? → conversion-copywriting (new) or copy-editing-sweeps (existing)
- Money/revenue mentioned? → money-path-verification or revenue-site-execution
- SEO + something else? → split the work: SEO part to seo-audit-playbook, other part gets its own skill
- WordPress mentioned? → wordpress-growth-ops (usually the execution step, not the planning step)
- "Should I use X?" → tool-evaluation
- "Can I publish/share this?" → here-now

### 5. Token Optimization
- Load only ONE skill at a time
- Small skills (<60 lines): load fully
- Large skills (>150 lines): read sections on demand
- Scripts in `scripts/` directories: use instead of reading SKILL.md when possible
- Reference files in `references/`: load only when skill says to
- After a skill finishes, re-check this file before loading the next one

## Skill Load Order (When Building a Pipeline)
Plan first → Create second → Technical third → Execute fourth → Verify last → Monitor ongoing
1. **Plan** — strategy, positioning, tool evaluation
2. **Create** — copywriting, email sequences, lead magnets
3. **Technical** — schema, tracking, API integrations
4. **Execute** — WordPress publishing, deployment, testing
5. **Verify** — money-path verification, launch-readiness, QA
6. **Monitor** — notifications, monitoring, analytics

## When No Skill Fits
If no skill in this list matches the task:
1. Check if it's a sub-task of a broader skill (e.g., "add a form" → likely part of wordpress-growth-ops)
2. Consider if it's a new skill worth creating (→ skill-authoring-standard)
3. For simple file/hosting tasks, here-now covers publish/share/upload
4. For general questions, answer directly without loading any skill

## Common Mistakes to Avoid
- **Wrong SEO skill:** seo-audit-playbook = diagnosing issues, seo-command-center = cross-cutting SEO, schema-ops = structured data only. Pick the right one.
- **wordpress-growth-ops too early:** This is execution, not planning. Plan first (content-strategy, offer-positioning), then execute.
- **Skipping tracking-measurement:** When setting up email, ads, or funnels, always follow up with tracking. Conversion data without tracking is wasted.
- **Overloading workflows:** Don't load a 4-skill pipeline for a 1-skill problem. "Fix this email" = just email-automation-debugging.
- **Missing site context:** If the task mentions a known site, check the By Site table first for pre-computed combos.

## Output Contract
**Artifact**: Skill selection or workflow plan
**Evidence**: Rationale for skill choice
**Decision**: Which skill(s) to load, in what order
**Next**: Load the selected skill and execute

## Checks
- Don't load multiple skills upfront — load sequentially
- When uncertain between 2 skills, read both "Use this when" sections
- Track frequently paired skills — suggest creating a workflow macro to /ops/macros/
- If a request has no skill match, consider creating one (→ skill-authoring-standard)
- After skill work completes, update memory/ if there are learnings worth keeping

---
*Last updated: 2026-03-14 | 34 skills routed | 8 workflows defined*
