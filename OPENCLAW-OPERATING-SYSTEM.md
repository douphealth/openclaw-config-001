# OpenClaw Operating System

_Date: 2026-03-19_

This document explains the current OpenClaw operating stack as a coherent system.

---

## 1. What OpenClaw is trying to be

Not just a bag of skills.
Not just a chat assistant with tools.

OpenClaw is being shaped into an **execution operating system** with layers for:
- trigger / activation
- specification
- planning
- orchestration
- implementation
- recovery
- verification
- persistence
- site memory

The goal is not maximum activity.
The goal is **maximum useful, verified, recoverable execution**.

---

## 2. Core Operating Principle

For serious work, OpenClaw should follow:

**Spec → Plan → Dispatch → Review → Verify**

That means:
1. understand the real outcome first
2. plan before large execution
3. split independent work safely
4. review for spec compliance and quality
5. verify in reality before completion

This principle is defined in:
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`
- `skills/shared/enterprise-protocol.md`

---

## 3. System Layers

### Layer A — Trigger / Activation
These decide which path to take.
- `skill-router`
- `skill-trigger-engine`
- `skills/shared/skill-trigger-engine-spec.md`
- `skills/shared/auto-dispatch-policy.md`
- `skills/shared/auto-router-config.json`

**Role:** determine whether work should be clarified, audited, parallelized, repaired, or directly executed.

### Layer B — Control / Meta Discipline
These force better thinking before action.
- `using-superpowers`
- `task-intake-spec-writer`
- `job-bootstrapper`

**Role:** stop vague, risky, or large tasks from jumping straight into mutation.

### Layer C — Orchestration / Scale
These coordinate serious execution.
- `parallel-execution-director`
- `swarm-orchestrator`
- `batch-mutation-controller`
- `repair-wave-runner`
- `execution-state-ledger`

**Role:** split work, run waves, track state, and control scale.

### Layer D — Audit / Intelligence
These diagnose and prioritize.
- `site-audit-director`
- `seo-command-center`
- `seo-audit-playbook`
- `seo-intelligence`
- `keyword-research-mastery`
- `ai-visibility`
- `analytics-reporting`
- `tracking-measurement`

**Role:** convert data into ranked action queues.

### Layer E — Domain Implementation
These do actual business work.
- `revenue-site-execution`
- `wordpress-growth-ops`
- `wp-rest-api-mastery`
- `editorial-post-enhancement`
- `offer-positioning`
- `service-funnel-architecture`
- `lead-magnet-delivery-ops`
- `money-path-verification`
- plus copy / email / SEO specialists

**Role:** implement improvements, not just analyze them.

### Layer F — Recovery / Repair
These handle failure, corruption, instability, and cleanup.
- `failure-recovery-director`
- `content-integrity-cleanup`
- `site-cleanup-operator`
- `wp-error-recovery`
- `auto-verification`
- `verification-runner`
- recovery playbooks + scripts

**Role:** stop damage, classify failure, repair safely, prove recovery.

### Layer G — Site Memory / Registry
These preserve operational knowledge.
- `ops/site-ops-registry.md`
- `ops/site-recovery-packs/*`
- `ops/generated-site-dossiers.json`
- `memory/*.md`
- `MEMORY.md`

**Role:** prevent rediscovering the same facts and traps over and over.

---

## 4. Default Execution Path

### Small, clear, low-risk work
`skill-router` → specialist skill → `verification-runner` if needed

### Ambiguous or risky work
`skill-router` → `using-superpowers` → `task-intake-spec-writer` → specialist/director

### Large-scale parallel work
`skill-router` → `parallel-execution-director` → worker outputs → synthesis → verification

### Large-scale writes
`skill-router` → `batch-mutation-controller` → canary → wave → verification

### Unstable or broken systems
`skill-router` → `failure-recovery-director` → `content-integrity-cleanup` / `repair-wave-runner` / rollback path

### Full-site audit
`skill-router` → `site-audit-director` → prioritized action queue → implementation skills

---

## 5. Strategic Entry Points

Use these as primary starting points:

- **Full audit:** `site-audit-director`
- **Ambiguous/high-risk request:** `using-superpowers`
- **Need a spec:** `task-intake-spec-writer`
- **Parallel execution:** `parallel-execution-director`
- **Safe batch writes:** `batch-mutation-controller`
- **Recovery:** `failure-recovery-director`
- **Content corruption/duplication:** `content-integrity-cleanup`
- **Verification:** `verification-runner`
- **Managed-site business execution:** `revenue-site-execution`

---

## 6. Non-Negotiable Operational Rules

For serious work:
- health check first
- backup before mutation
- retry with backoff
- canary before scale writes
- progress reporting during long jobs
- verification before completion
- rollback thinking before damage occurs

These are defined in:
- `skills/shared/enterprise-protocol.md`

---

## 7. Supporting Artifacts

### Templates / policy
- `skills/shared/execution-brief-template.md`
- `skills/shared/worker-result-contract.md`
- `skills/shared/verification-evidence-pack.md`
- `skills/shared/recovery-playbook-pack.md`
- `skills/shared/capability-map.md`
- `skills/shared/skill-capability-graph.json`
- `skills/shared/auto-dispatch-policy.md`
- `skills/shared/auto-router-config.json`

### Scripts
- `skills/shared/scripts/execution_brief.py`
- `skills/shared/scripts/execution_ledger.py`
- `skills/shared/scripts/synthesize_worker_results.py`
- `skills/shared/scripts/recovery_canary.py`
- `skills/shared/scripts/wp-bulk-ops.py`
- `skills/shared/scripts/site_dossier_generator.py`
- `skills/shared/scripts/repair_wave_runner.py`
- `skills/shared/scripts/verification_runner.py`
- `skills/shared/scripts/remove_linkwhisper_duplicates.py`
- `skills/shared/scripts/strip_embedded_full_html.py`
- `skills/shared/scripts/strip_embedded_article_wrapper.py`
- `skills/shared/scripts/normalize_meta_h1_report.py`
- `skills/shared/scripts/job_bootstrapper.py`

---

## 8. What changed from the old model

### Before
- many isolated skills
- uneven safety/verification discipline
- weak orchestration hierarchy
- poor persistence for long jobs
- recovery often improvised

### Now
- layered control system
- stronger routing and trigger policy
- execution briefing + ledgers
- controlled batch mutation model
- formal recovery and cleanup skills
- evidence-based verification standard
- site-specific ops memory

---

## 9. Where the system is still weak

1. trigger policy is documented, but not fully automated in code/runtime
2. site dossiers should expand to all managed properties
3. some old specialist skills still need hierarchy/cross-link cleanup
4. live infrastructure instability can still defeat good orchestration

---

## 10. Final doctrine

The OpenClaw OS should behave like this:

- **Think before mutating**
- **Structure before scaling**
- **Recover before compounding damage**
- **Verify before claiming success**
- **Remember what the site/system taught you**

That is the operating system.
