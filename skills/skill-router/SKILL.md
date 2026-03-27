---
name: skill-router
description: Use FIRST when unsure which skill to use, when a task spans multiple skills, or when optimizing workflow efficiency. Routes work to the optimal skill or skill combination.
---

# Skill Router

## Purpose
Route work to the most specific useful skill, avoid overlap, and minimize token waste from loading the wrong playbook.

Intelligent routing layer that maps tasks to optimal skills, prevents overlap confusion, and enables multi-skill workflows with minimal token waste.

## Decision Tree: How to Route?

```
Task or request received
│
├── Is it obvious which single skill handles this?
│   └── YES → Load that skill directly (skip routing)
│
├── Are you unsure which skill to use?
│   └── YES → Use the routing tables below (Section 1)
│
├── Does the task span multiple skills?
│   └── YES → Check Multi-Skill Workflows (Section 3)
│
├── Could it map to 2+ skills?
│   └── YES → Use Tiebreakers (Section 4)
│
├── Is it a full SEO operation across multiple areas?
│   └── YES → seo-command-center (orchestrates sub-skills)
│
└── Does no skill match?
    └── See "When No Skill Fits" (Section 6)
```

## Superpower Layer

For serious work, also follow:
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`

Default execution mode:
1. clarify/spec first if ambiguous
2. write a short plan before large execution
3. dispatch parallel workers for independent subtasks when safe
4. review output for spec compliance and quality
5. verify in reality before claiming complete

## When to Use

- Unsure which skill handles a task
- Task spans multiple skills
- Optimizing token efficiency across skills
- Building multi-step workflows

## Do NOT Use For
- Actually executing the task itself (route, then load the target skill)
- Tasks with an obvious single-skill match (load it directly)
- Simple questions that do not require a skill

## 1. Route by Task Type

| User Intent | Load This Skill |
|------------|----------------|
| "Write new page/copy" | `conversion-copywriting` |
| "Improve existing article" | `editorial-post-enhancement` |
| "Plan content topics" | `content-strategy-planning` |
| "SEO audit" | `seo-audit-playbook` |
| "Add/improve schema" | `schema-ops` |
| "Debug email automation" | `email-automation-debugging` |
| "Set up email marketing" | `email-marketing-engine` |
| "Design email drip" | `lifecycle-email-sequences` |
| "Verify checkout/funnel" | `money-path-verification` |
| "Pre-launch check" | `launch-readiness-audit` |
| "Build API integration" | `api-integration-builder` |
| "Run site tests" | `test-automation-ops` |
| "Set up alerts" | `notification-engine` |
| "Improve WordPress site" | `wordpress-growth-ops` |
| "Analyze/report data" | `analytics-reporting` |
| "Fix tracking/pixels" | `tracking-measurement` |
| "Audit ad spend" | `paid-media-audit` |
| "Position an offer" | `offer-positioning` |
| "Design a funnel" | `service-funnel-architecture` |
| "Write documentation" | `technical-writing` |
| "Alerts + monitoring" | `notification-engine` + `monitoring-ops` |
| "Compare tools" | `tool-evaluation` |
| "Design A/B test" | `experiment-tracking` |
| "Create lead magnet" | `lead-magnet-delivery-ops` |
| "Build pSEO pages" | `programmatic-seo-blueprints` |
| "Multi-worker coordination" | `swarm-orchestrator` |
| "Ambiguous / high-risk / multi-step task" | `using-superpowers` |
| "Parallel audit / parallel batch execution" | `parallel-execution-director` |
| "Turn vague requests into an execution brief" | `task-intake-spec-writer` |
| "Recover from failures / unstable systems / partial corruption" | `failure-recovery-director` |
| "Fragile custom page / repeated visual regressions / shell rewrite needed" | `browser-visual-ops` + `verification-runner` || "Run a full audit and output a prioritized action queue" | `site-audit-director` |
| "Safely mutate many records in controlled waves" | `batch-mutation-controller` |
| "Clean duplicate/broken content structures" | `content-integrity-cleanup` |
| "Improve automatic skill activation / trigger policy" | `skill-trigger-engine` |
| "Run controlled repair waves with canary + checkpoints" | `repair-wave-runner` |
| "Run standardized verification after work" | `verification-runner` |
| "Bootstrap a serious job with brief + ledger" | `job-bootstrapper` |
| "Run a sitewide cleanup campaign" | `site-cleanup-operator` |
| "Manage memory/notes" | `memory-operations` |
| "Create/edit skills" | `skill-authoring-standard` |
| "Host/publish files" | `here-now` |
| "Edit/improve existing copy" | `copy-editing-sweeps` |
| "Full SEO operations" | `seo-command-center` |
| "Screenshots / visual QA / browser automation / DOM inspect" | `browser-visual-ops` |

## 2. Route by Site (All Managed Sites)

| Site | Stack | Primary Skills | WP Skills |
|------|-------|---------------|-----------|
| affiliatemarketingforsuccess.com | WP + FluentCRM + Cloudflare | `revenue-site-execution`, `email-automation-debugging` | `wp-rest-api-mastery`, `wordpress-growth-ops` |
| mysticaldigits.com | WP + GeneratePress + Seraphinite + Cloudflare | `seo-audit-playbook`, `schema-ops` | `wp-error-recovery`, `wp-rest-api-mastery` |
| gearuptofit.com | WP + Elementor + Cloudflare | `editorial-post-enhancement`, `schema-ops` | `wp-rest-api-mastery`, `wordpress-performance` |
| frenchyfab.com | WP + GeneratePress + Cloudflare | `wordpress-growth-ops`, `content-strategy-planning` | `wp-rest-api-mastery` |
| efficientgptprompts.com | WP | `content-strategy-planning`, `conversion-copywriting` | `wordpress-growth-ops` |
| micegoneguide.com | WP | `wordpress-growth-ops`, `seo-audit-playbook` | `wp-rest-api-mastery` |
| gearuptogrow.com | WP | `wordpress-growth-ops`, `revenue-site-execution` | `wp-rest-api-mastery` |
| plantastichaven.com | WP | `content-strategy-planning`, `seo-audit-playbook` | `wp-rest-api-mastery` |
| profitplaybook.com | WP + Divi | `revenue-site-execution`, `schema-ops` | `wp-rest-api-mastery`, `wp-error-recovery` |
| outdoormisting.com | Static | N/A | N/A |
| openclaw-skillshub.com | GitHub App | N/A | N/A |

**WordPress sites:** Always start with `wp-rest-api-mastery` for CRUD, `wp-error-recovery` for debugging.
**Known site patterns:** Use the site table to load pre-computed skill combos.

## 3. Multi-Skill Workflows (Load in Order)

### New Content End-to-End
```
content-strategy-planning → conversion-copywriting → editorial-post-enhancement → schema-ops → wordpress-growth-ops
```

### SEO Fix
```
seo-audit-playbook → schema-ops → editorial-post-enhancement
```

### Email System Setup
```
email-marketing-engine → lifecycle-email-sequences → tracking-measurement
```

### Site Launch
```
launch-readiness-audit → money-path-verification → tracking-measurement → notification-engine
```

### Content Refresh
```
seo-audit-playbook → editorial-post-enhancement → schema-ops
```

### Paid Media Fix
```
paid-media-audit → tracking-measurement → analytics-reporting
```

### Service Funnel Build
```
offer-positioning → service-funnel-architecture → conversion-copywriting → money-path-verification
```

### Full Site Rebuild
```
seo-audit-playbook → content-strategy-planning → conversion-copywriting → schema-ops → wordpress-growth-ops → launch-readiness-audit
```

## 4. Ambiguous Requests — Tiebreakers

| Situation | Resolution |
|-----------|-----------|
| Copy involved? | New → `conversion-copywriting`; existing → `copy-editing-sweeps` |
| Money/revenue mentioned? | Verification → `money-path-verification`; execution → `revenue-site-execution` |
| SEO + something else? | Split: SEO part → `seo-audit-playbook`, other part → its own skill |
| WordPress mentioned? | Usually `wordpress-growth-ops` (execution step, not planning) |
| "Should I use X?" | `tool-evaluation` |
| "Can I publish/share this?" | `here-now` |
| AI search visibility / GEO? | `ai-visibility` |
| Health check / security? | `healthcheck` |

## API-First Routing Rule

When a routed skill can complete work through APIs or structured file operations, prefer that route over browser/manual flows and apply `skills/api-efficiency-protocol.md`.

## Visual Verification Rule

For any request involving visual layout, styling, screenshots, "looks broken", mobile/desktop QA, or UI flows:
1. route to `browser-visual-ops` first or immediately after the edit skill
2. capture desktop + mobile artifacts before claiming success
3. if screenshots contradict source-level assumptions, trust the screenshots

## 5. Token Optimization

| Strategy | Implementation |
|----------|---------------|
| Load ONE skill at a time | Don't load multiple upfront — load sequentially |
| Small skills (<60 lines) | Load fully |
| Large skills (>150 lines) | Read sections on demand |
| Use scripts over SKILL.md | `scripts/` directories have runnable code |
| Reference files on-demand | `references/` — load only when skill says to |
| Re-check after completion | Before loading next skill, re-check this router |

### Skill Load Order (When Building a Pipeline)

```
1. PLAN      → strategy, positioning, tool evaluation
2. CREATE    → copywriting, email sequences, lead magnets
3. TECHNICAL → schema, tracking, API integrations
4. EXECUTE   → WordPress publishing, deployment, testing
5. VERIFY    → money-path verification, launch-readiness, QA
6. MONITOR   → notifications, monitoring, analytics
```

## 6. When No Skill Fits

```
No skill matches the task
│
├── Is it a sub-task of a broader skill?
│   ├── "Add a form" → likely `wordpress-growth-ops`
│   ├── "Check if checkout works" → `money-path-verification`
│   └── "Something broke" → diagnose first, then route
│
├── Is it a new skill worth creating?
│   └── YES → `skill-authoring-standard`
│
├── Is it a simple file/hosting task?
│   └── YES → `here-now`
│
└── Is it a general question?
    └── Answer directly — no skill needed
```

## 7. Common Mistakes & Anti-Patterns

| Anti-Pattern | Consequence | Prevention |
|-------------|-------------|-----------|
| Wrong SEO skill | Wasted time, wrong diagnosis | `seo-audit-playbook` = diagnose; `schema-ops` = structured data; `seo-command-center` = cross-cutting |
| `wordpress-growth-ops` too early | Execution before planning | Plan first (content-strategy, offer-positioning), then execute |
| Skipping `tracking-measurement` | Conversion data wasted | Always follow email/ads/funnels with tracking |
| Overloading workflows | Token waste on simple tasks | "Fix this email" = just `email-automation-debugging` |
| Missing site context | Suboptimal skill combos | Check "Route by Site" table first |
| Loading multiple skills upfront | Token waste, context confusion | Load sequentially, one at a time |

## Verification Steps

1. Confirm the routed skill's description matches the task
2. Check that no more specific skill exists for the task
3. If multi-skill workflow, confirm the order is logical
4. After skill work completes, update `memory/` if learnings worth keeping


## Self-Critique Scorecard (/25)
After every operation, score yourself:

| Dimension | Score | Notes |
|-----------|-------|-------|
| **Functionality** (1-5) | ? | Does it work perfectly and meet all requirements? |
| **Quality** (1-5) | ? | Is it enterprise-grade and production-ready? |
| **Verification** (1-5) | ? | Was it verified via multiple methods? |
| **Speed** (1-5) | ? | Was execution optimal with parallel operations? |
| **Learning** (1-5) | ? | Were new patterns documented and memory updated? |

**Target: 22+/25 before claiming completion**

### Pre-Flight Checklist
- [ ] Credentials verified and target exists
- [ ] Rollback plan identified
- [ ] Success criteria defined
- [ ] Anti-patterns reviewed

### Post-Flight Checklist
- [ ] Verified via API response + live check
- [ ] Quality score logged to memory/YYYY-MM-DD.md
- [ ] Skill references updated if new patterns discovered
- [ ] No common mistakes made

## Output Contract

| Field | Description |
|-------|-------------|
| **Artifact** | Skill selection or multi-skill workflow plan |
| **Evidence** | Rationale for skill choice (why this skill, why not others) |
| **Decision** | Which skill(s) to load, in what order |
| **Next** | Load the selected skill and execute the task |

## Checks

- Don't load multiple skills upfront — load sequentially
- When uncertain between 2 skills, read both "Use this when" sections
- Track frequently paired skills — suggest creating a workflow macro to `ops/macros/`
- If a request has no skill match, consider creating one (→ `skill-authoring-standard`)
- After skill work completes, update `memory/` if learnings worth keeping

## Enterprise Protocols (MANDATORY)

Before executing any routed task, read:
- `skills/shared/enterprise-protocol.md`
- `skills/shared/openclaw-superpowers.md`

And follow:
- Pre-flight health check (site accessible, creds valid, state captured)
- Mandatory backup before any modification
- Retry with exponential backoff (max 3 attempts per API call)
- Progress reporting every 10 operations
- Verification after each modification
- Health checks every 50 items in long operations
- Rollback plan identified before starting
- Spec → Plan → Dispatch → Review → Verify workflow for complex tasks

## Post-Task Strategy Identification

After completing ANY task, run this analysis to identify the optimal approach:

```
Task completed
│
├── Was this a single skill task?
│   └── Check if adjacent skills should have been loaded (multi-skill workflow)
│
├── Was this a multi-skill workflow?
│   └── Verify all outputs are consistent across skills
│
├── Did the task involve batch operations (>10 items)?
│   └── Were parallel workers used? If not, document for next time.
│
├── Were there errors or retries?
│   └── Log error pattern to memory/YYYY-MM-DD.md
│   └── Update skill references if new patterns found
│
├── Could this task be a macro?
│   └── If repeated pattern, create in ops/macros/
│
└── Was the approach optimal?
    └── Score: Speed (was parallelism used?) + Quality (was it verified?)
    └── If <22/25, document what to improve next time
```

### Velocity Optimization Matrix

| Task Type | Optimal Approach | Speed Multiplier |
|-----------|-----------------|------------------|
| Single post edit | Direct API call | 1x |
| 5-20 posts | Sequential with retry | 2x |
| 20-100 posts | Parallel subagents (3-5 workers) | 5x |
| 100+ posts | concurrent.futures + subagents | 8x |
| Multi-site ops | One worker per site | 10x |
| Research + execute | Subagent for research, main for execution | 3x |

---
*Last updated: 2026-03-18 | 42 skills routed | 10 workflows defined*

### WordPress Skill Routing (Critical)

| WP Task | Load This Skill |
|---------|----------------|
| REST API CRUD (posts/pages/media) | `wp-rest-api-mastery` |
| Debug broken content/routing | `wp-error-recovery` |
| WP-CLI operations | `wordpress-autonomous-ops` |
| Performance/speed issues | `wordpress-performance` |
| Growth/conversion improvements | `wordpress-growth-ops` |
| Plugin/theme development | Official WP skills (wp-plugin-development, wp-block-themes) |
| Site-wide SEO on WP | `wordpress-growth-ops` → `seo-audit-playbook` |
| Content publishing on WP | `editorial-post-enhancement` → `wp-rest-api-mastery` |
| FluentCRM integration | `wp-rest-api-mastery` (has FluentCRM patterns) |
| Homepage deployment | `wp-error-recovery` (has anti-patterns) |
| Cache issues | `wp-error-recovery` (has caching diagnosis) |

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

## Performance Optimizations

### Speed Multipliers
- Apply `skills/api-efficiency-protocol.md` when a routed skill involves API work — surface the tip during routing
- Read only the "When to Use" and "Do NOT Use For" sections first to confirm routing before loading full skill
- Cache routing decisions within a session — don't re-evaluate the same request type twice
- Load skills sequentially (one at a time) — never load multiple skills upfront for a multi-skill workflow
- Use the "Route by Site" table to pre-load known skill combos instead of re-deriving them
- Check the workflow macros (`workflow-macros`) before building custom pipelines — pre-built chains save tokens

## Anti-Patterns
- ❌ Loading multiple skills upfront for a multi-step task — load sequentially to avoid token waste and context confusion
- ❌ Using skill-router for tasks with an obvious single-skill match — go direct, skip routing overhead
- ❌ Ignoring the "Do NOT Use For" boundaries — routing to the wrong skill wastes more time than asking
- ❌ Building custom workflows when a pre-built macro already exists in `workflow-macros`
- ❌ Re-routing after each sub-task instead of using the site table to pre-plan the skill chain
- ❌ Skipping the tiebreaker rules for ambiguous requests — guesswork leads to wrong skill loads
- ❌ Treating skill-router as a skill to execute work — it routes, it doesn't do the work

## Output Contract
- **Artifact**: What was created/changed/deleted
- **Evidence**: API response proof + live verification
- **Decision**: Success/failure with reasoning
- **Next**: What follow-up is needed (if any)
