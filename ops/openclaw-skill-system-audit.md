# OpenClaw Skill System Audit

_Date: 2026-03-19_

## Executive Summary

The workspace skill system has grown into a powerful stack, but it now contains three kinds of complexity:

1. **Healthy specialization** — distinct skills with clear roles
2. **Soft overlap** — multiple skills in the same domain with fuzzy boundaries
3. **Control-layer fragmentation** — new meta/orchestration skills exist, but the hierarchy between them was not yet fully explained in one place

This audit groups the skills into operating systems, identifies overlap/redundancy, and proposes a cleaner hierarchy.

## System Map

### 1. Control / Meta Layer
These decide *how* work should run.
- `skill-router`
- `skill-trigger-engine`
- `using-superpowers`
- `task-intake-spec-writer`
- `parallel-execution-director`
- `swarm-orchestrator`
- `execution-state-ledger`
- `job-bootstrapper`

**Observation:** This is now a strong system, but there is overlap between `parallel-execution-director` and `swarm-orchestrator`.

### 2. Recovery / Stability Layer
These handle breakage, cleanup, rollback, and unstable systems.
- `failure-recovery-director`
- `content-integrity-cleanup`
- `repair-wave-runner`
- `site-cleanup-operator`
- `wp-error-recovery`
- `auto-verification`
- `verification-runner`

**Observation:** This is now one of the strongest parts of the stack. Main overlap is between `auto-verification` and `verification-runner`.

### 3. Audit / Intelligence Layer
These diagnose systems and generate prioritized actions.
- `site-audit-director`
- `seo-command-center`
- `seo-audit-playbook`
- `seo-intelligence`
- `keyword-research-mastery`
- `seo-competitor-analysis`
- `seo-intent-mapper`
- `ai-visibility`
- `tracking-measurement`
- `analytics-reporting`
- `tool-evaluation`

**Observation:** This is rich, but `site-audit-director` should become the preferred entrypoint for serious audits, with the others acting as specialists.

### 4. Mutation / Implementation Layer
These actually change content, sites, funnels, tracking, etc.
- `batch-mutation-controller`
- `wp-rest-api-mastery`
- `wordpress-growth-ops`
- `revenue-site-execution`
- `editorial-post-enhancement`
- `copy-editing-sweeps`
- `conversion-copywriting`
- `offer-positioning`
- `schema-ops`
- `service-funnel-architecture`
- `lead-magnet-delivery-ops`
- `lifecycle-email-sequences`
- `email-automation-debugging`
- `email-marketing-engine`

**Observation:** Strong domain specialization. Main issue is entrypoint ambiguity between WordPress/content/revenue skills.

### 5. Site / Business Strategy Layer
These shape portfolio and growth decisions.
- `content-strategy-planning`
- `programmatic-seo-blueprints`
- `launch-readiness-audit`
- `money-path-verification`
- `experiment-tracking`
- `paid-media-audit`
- `technical-writing`
- `memory-operations`

## Main Overlaps / Redundancies

### A. `swarm-orchestrator` vs `parallel-execution-director`
- **Current state:** both deal with multi-worker execution
- **Refactor direction:**
  - `using-superpowers` = should we slow down / spec / control?
  - `parallel-execution-director` = how to decompose and dispatch workers?
  - `swarm-orchestrator` = lower-level worker mechanics and templates

**Decision:** Keep both, but define `parallel-execution-director` as the strategic entrypoint and `swarm-orchestrator` as the execution substrate.

### B. `auto-verification` vs `verification-runner`
- **Current state:** both cover verification
- **Refactor direction:**
  - `verification-runner` = reusable verification controller
  - `auto-verification` = specialist for operational verification workflows / templates

**Decision:** Keep both, but `verification-runner` becomes the general verification entrypoint.

### C. `wordpress-growth-ops` vs `revenue-site-execution` vs `wp-rest-api-mastery`
- **Current state:** three ways into WordPress work
- **Refactor direction:**
  - `wp-rest-api-mastery` = data-plane / API specialist
  - `wordpress-growth-ops` = WordPress implementation specialist
  - `revenue-site-execution` = business/prioritization layer for monetization work

**Decision:** Hierarchical, not redundant. Route broad business tasks to `revenue-site-execution`, implementation to `wordpress-growth-ops`, low-level REST work to `wp-rest-api-mastery`.

### D. `seo-command-center` vs `site-audit-director`
- **Current state:** both can orchestrate audit-like work
- **Refactor direction:**
  - `site-audit-director` = full-site audit synthesis entrypoint
  - `seo-command-center` = ongoing SEO operating system / command hub

**Decision:** `site-audit-director` for audits, `seo-command-center` for operating the SEO program after audit.

## Refactor Principles

1. **One strategic entrypoint per system**
2. **Subordinate specialists stay specialized**
3. **Avoid deleting useful specialization unless truly duplicative**
4. **Clarify hierarchy rather than flattening everything**

## Proposed Grouped Systems

### OpenClaw OS Core
- `skill-router`
- `skill-trigger-engine`
- `using-superpowers`
- `task-intake-spec-writer`
- `job-bootstrapper`
- `execution-state-ledger`

### OpenClaw Parallel Execution System
- `parallel-execution-director`
- `swarm-orchestrator`
- `batch-mutation-controller`
- `repair-wave-runner`
- `verification-runner`

### OpenClaw Recovery System
- `failure-recovery-director`
- `content-integrity-cleanup`
- `site-cleanup-operator`
- `wp-error-recovery`
- `auto-verification`

### OpenClaw Audit / Intelligence System
- `site-audit-director`
- `seo-command-center`
- `seo-audit-playbook`
- `seo-intelligence`
- `keyword-research-mastery`
- `ai-visibility`
- `analytics-reporting`
- `tracking-measurement`

### OpenClaw WordPress / Revenue System
- `revenue-site-execution`
- `wordpress-growth-ops`
- `wp-rest-api-mastery`
- `editorial-post-enhancement`
- `offer-positioning`
- `service-funnel-architecture`
- `lead-magnet-delivery-ops`
- `money-path-verification`

## Recommended Immediate Refactors

1. Add explicit “Strategic Entry Point” sections to:
   - `parallel-execution-director`
   - `verification-runner`
   - `site-audit-director`
   - `revenue-site-execution`

2. Add “Use this before/after” cross-links between overlapping skills.

3. Create one master document that explains the full stack coherently.

## Final Verdict

The system is no longer weak — it is becoming layered. The main need is no longer “more skills,” but **clear hierarchy, entrypoints, and operating doctrine**.
