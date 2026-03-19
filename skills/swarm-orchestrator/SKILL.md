---
name: swarm-orchestrator
description: Use when work should be decomposed across multiple OpenClaw workers, specialist sessions, or verification passes. Triggers on parallel execution, multi-site operations, director-worker-verifier setups, autonomous execution systems, high-throughput batches, or tasks with independent deliverables that benefit from orchestration.
---

# Swarm Orchestrator

## Purpose
Coordinate complex work through a director/worker/verifier model so throughput increases without collapsing quality control.

Enterprise orchestration system for coordinating complex work through a director/worker/verifier pattern so execution scales without losing QA.

## Decision Tree: Swarm or Single Thread?

```
Task received
│
├── Can a single focused session finish in <10 minutes?
│   └── YES → Do it directly, don't decompose
│
├── Does the task have multiple independent deliverables?
│   ├── YES → Swarm (this skill)
│   └── NO → Single thread
│
├── Would parallel execution save meaningful time?
│   ├── YES → Swarm
│   └── NO → Single thread
│
├── Does the task touch multiple sites or systems?
│   └── YES → Swarm (one worker per site/system)
│
├── Should verification be separated from implementation?
│   └── YES → Swarm with dedicated verifier
│
└── Is the task high-throughput (batch of similar items)?
    └── YES → Swarm (one worker per item or batch chunk)
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

- Task has multiple independent deliverables
- Parallel execution would save meaningful time
- Specialist roles would improve output quality
- Verification should be separated from implementation
- Multi-site or high-throughput workflow would overload a single thread

## Do NOT Use For
- Simple single-threaded tasks (do them directly)
- Tasks needing tight interactive back-and-forth with little decomposability
- Decomposition that adds more overhead than value
- ACP/session spawning when a first-class single-skill execution path is clearly enough

## Operating Model

| Role | Responsibility | Characteristics |
|------|---------------|-----------------|
| **Director** (main session) | Prioritization, blockers, synthesis, proof | Single thread, strategic |
| **Workers** (subagent sessions) | Execution of assigned deliverables | Parallel, focused, one deliverable each |
| **Verifier** (separate session) | QA, validation, evidence checking | Independent from workers |

## Operational Procedures

### 1. Decomposition Protocol

**Step 1 — Assess decomposability:**
```
Is this task decomposable?
├── Yes, deliverables are independent → Full swarm
├── Partially, some steps depend on others → Sequential swarm (chain workers)
└── No, tight coupling required → Single thread
```

**Step 2 — Define deliverables:**
- Each deliverable must be self-contained (no shared mutable state)
- Each deliverable has a clear "done" definition
- Each deliverable produces a verifiable artifact

**Step 3 — Assign roles:**
- One worker = one deliverable (never combine)
- Prefer parallel workers when tasks are independent
- Choose verifier coverage based on risk:
  - Low-risk tasks (research, writing): spot-check verifier
  - High-risk tasks (deployments, data changes): full verification
  - Critical tasks (production changes): mandatory independent verifier

### 2. Worker Prompt Structure

Each worker receives:
```
TASK: [specific deliverable]
CONTEXT: [minimal necessary context — don't overload]
CONSTRAINTS: [what not to do, boundaries]
OUTPUT FORMAT: [expected artifact structure]
VERIFICATION: [how completion will be verified]
```

**Rules for worker prompts:**
- Include only the context the worker needs (token efficiency)
- Be explicit about output format
- Define "done" concretely
- Specify what evidence is required

### 3. Execution Patterns

**Pattern A: Parallel Dispatch (independent tasks)**
```
Director → Worker 1 (task A)
         → Worker 2 (task B)    [simultaneous]
         → Worker 3 (task C)
         
Verifier ← collects all outputs
Director ← synthesizes verified results
```

**Pattern B: Sequential Chain (dependent tasks)**
```
Director → Worker 1 (foundation)
         → Worker 2 (builds on Worker 1 output)
         → Worker 3 (builds on Worker 2 output)
         
Verifier ← checks final output
Director ← delivers result
```

**Pattern C: Fan-Out / Fan-In (batch processing)**
```
Director splits batch into chunks
         → Worker 1 (chunk 1)
         → Worker 2 (chunk 2)   [parallel]
         → Worker 3 (chunk 3)
         
Verifier ← spot-checks sample from each chunk
Director ← merges results, checks for consistency
```

### 4. Quality Gates (Set Before Execution)

Define these BEFORE launching workers:

| Gate | Definition |
|------|-----------|
| **Completion criteria** | What "done" looks like — be specific |
| **Evidence requirements** | What proof each worker must provide |
| **Failure threshold** | How many failed workers = abort |
| **Timeout** | Max wait time before escalating |
| **Verification method** | How the verifier will check work |

### 5. Director Output Format

Always return this structure:

```
## Orchestration Report

### Plan
- Task: [what was being done]
- Decomposition: [how it was split]
- Workers: [count and assignments]

### Workers Launched
| Worker | Task | Status | Duration |
|--------|------|--------|----------|
| W1 | [task] | ✅ Complete | 2m |
| W2 | [task] | ✅ Complete | 3m |
| W3 | [task] | ❌ Failed | 1m |

### Blockers
- [Any blockers encountered and how resolved]

### Verified Outcomes
- [What was verified and by whom]
- [Evidence links/files]

### Next Best Actions
1. [Immediate next step]
2. [Follow-up if needed]
```

## Method Selection Guide

| Task Type | Method | Rationale |
|-----------|--------|-----------|
| Research, writing, audits | Normal subagents | I/O-bound, no iterative debugging |
| Multi-file code changes | ACP | Iterative debugging, multi-file coordination |
| Publishing, QA, testing | Normal subagents | Verification-heavy |
| Data migration, transformations | ACP or subagents (depends on complexity) | Error handling needs |

## Anti-Noise Rules

| Rule | Rationale |
|------|-----------|
| Don't spawn workers for vague, overlapping tasks | Creates confusion, not efficiency |
| Don't skip verification because execution succeeded | Execution success ≠ correct output |
| Don't let main thread become a duplicate worker | Director stays strategic, not tactical |
| Don't decompose tiny tasks | Overhead exceeds value |
| Don't set quality gates after execution | Define upfront, not retroactively |
| Don't use retry loops aggressively | After repeated failure, escalate or change method |

## Performance Optimizations

### Speed Multipliers
- **Pre-fetch context**: Gather all credentials, IDs, and reference data before spawning workers
- **Batch by site**: Never context-switch between sites within a worker
- **Parallel verification**: Run verification checks concurrently, not sequentially
- **Smart timeouts**: Set worker timeouts based on task complexity (5min simple, 15min complex)
- **Cache warm-up**: Share cached data with workers via task context instead of re-fetching

### Worker Efficiency Rules
- Each worker gets ONLY the context it needs (token efficiency)
- Workers should not read MEMORY.md (save tokens)
- Workers should output structured results, not prose
- Worker prompts should be < 500 tokens when possible

## Auto-Verification Protocol

Every swarm must include verification. The verifier checks:
1. **Artifact completeness** — Did each worker deliver what was specified?
2. **Evidence quality** — Is the proof concrete (not just "done" claims)?
3. **Consistency** — Do outputs align across workers?
4. **Quality gates** — Were pre-defined quality gates met?
5. **Rollback safety** — Can changes be undone if issues found?

### Verification Report Format
```
## Verification Report
### Workers Checked
| Worker | Task | Artifact | Evidence | Score |
|--------|------|----------|----------|-------|
| W1 | [task] | ✅ Complete | [link/file] | 5/5 |
| W2 | [task] | ⚠️ Partial | [link/file] | 3/5 |

### Issues Found
- [Issue 1 with severity and fix]

### Quality Score: X/25
- Functionality: X/5
- Quality: X/5
- Verification: X/5
- Speed: X/5
- Learning: X/5
```

## Self-Improvement Loop

After every swarm execution:
1. Note what worked well and what didn't
2. Update worker prompt templates based on results
3. Track error patterns per site/operation
4. Promote successful patterns to `memory/YYYY-MM-DD.md`
5. Update skill references if new patterns emerged

## Anti-Patterns
- ❌ Workers producing inconsistent outputs because tasks overlap
- ❌ Skipping verification when "it looked done"
- ❌ Main thread doing worker tasks instead of coordinating
- ❌ Decomposing 5-minute tasks (overhead exceeds value)
- ❌ No quality gates defined before launch
- ❌ Aggressive retry loops after failure (thrashing, wasted tokens)
- ❌ Workers reporting optimism as fact without evidence

## Verification Steps

1. Confirm each worker delivered the specified artifact
2. Verify evidence is concrete (not just "done" claims)
3. Check for consistency across worker outputs
4. Confirm quality gates were met
5. Validate synthesis is complete and accurate

## Output Contract

| Field | Description |
|-------|-------------|
| **Artifact** | Orchestration plan with worker assignments and results |
| **Evidence** | Worker outputs, verification results, artifacts produced |
| **Decision** | All workers completed and verified (or failure state with root cause) |
| **Next** | Synthesis of results + recommended next actions |

## Resources

- `references/worker-selection.md` — Worker choice and spawn patterns
- `references/parallel-dispatch-patterns.md` — Independence checks and prompt structure
- `references/site-routing.md` — Task routing for workspace websites
- `references/output-contracts.md` — Consistent output format for workers

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

## Mandatory Enterprise Protocols

Before ANY operation, follow:
- `skills/shared/enterprise-protocol.md`
- `skills/shared/openclaw-superpowers.md`

Required:
- Pre-flight health check (site accessibility + auth)
- Mandatory backup before modifications
- Retry logic with exponential backoff (max 3 attempts)
- Progress reporting every 10 items
- Health checks every 50 items during long operations
- Verification after each modification
- Rollback plan identified before starting
- For complex work: Spec-first, then plan, then worker dispatch, then two-stage review

### Parallel Dispatch Decision Matrix

| Items | Approach | Max Workers |
|-------|----------|-------------|
| 1-5 | Single thread | 1 |
| 6-20 | Parallel subagents | 3-5 |
| 21-50 | Parallel subagents | 5-7 |
| 51+ | concurrent.futures + subagents | 8-10 |

### Worker Reliability Rules
- Each worker gets a 120s timeout (not 60s)
- Workers must report `SUCCESS` or `FAILED: [reason]`
- If >20% workers fail, abort batch and diagnose
- Never retry failed workers more than once
- After 3 consecutive worker failures, escalate to user

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
