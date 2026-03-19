# OpenClaw Superpowers Layer

Adapted from the best transferable patterns in obra/superpowers for OpenClaw operations.

## Core Principle
Never jump straight into execution when the task is ambiguous, large, risky, or cross-functional.

Use this sequence:
1. **Clarify / Spec** — what outcome actually matters?
2. **Plan** — what are the minimum decisive steps?
3. **Dispatch** — what can run in parallel safely?
4. **Review** — did output match spec and quality bar?
5. **Verify** — did it work in reality, not just in logs?
6. **Complete** — only after proof

## Mandatory Workflow Modes

### 1. Spec-First Mode
Trigger when:
- the task is vague
- the task affects production systems
- the task spans multiple sites, layers, or tools
- the task could create collateral damage if misunderstood

Required behavior:
- restate the target outcome in one sentence
- identify constraints
- define success criteria before starting
- do not execute large writes until the spec is clear

### 2. Plan-First Mode
Trigger when:
- work is multi-step
- >1 deliverable exists
- >10 items will be touched
- the task mixes research + execution

Required behavior:
- produce a short execution plan
- split into bite-sized steps
- identify which steps are parallelizable
- identify rollback before first mutation

### 3. Parallel Dispatch Mode
Trigger when:
- work contains independent subtasks
- multiple URLs/posts/sites can be checked independently
- one worker can audit while another verifies or researches

Rules:
- one worker = one clear deliverable
- do not parallelize destructive writes blindly
- use workers for audit, research, classification, diffing, and safe batches
- after worker completion, do a main-session synthesis pass

### 4. Two-Stage Review Mode
Before claiming completion on complex work:
- **Review 1: Spec compliance** — did the result actually match the requested outcome?
- **Review 2: Quality** — is the result clean, non-duplicative, minimal, and enterprise-grade?

### 5. Verification-Before-Completion Mode
Never say “done” until the strongest relevant proof is collected.

Examples:
- content edit → API state + live render
- SEO audit → data evidence + prioritized action list
- batch cleanup → before/after counts + spot-checks
- server fix → endpoint response + live path confirmation

## OpenClaw-Specific Dispatch Matrix

| Task shape | Best strategy |
|---|---|
| Small, clear, low risk | Direct execution |
| Ambiguous or strategic | Clarify → plan → execute |
| Large single-site batch | Audit → batch plan → controlled waves |
| Multi-site | one worker per site + main synthesis |
| Research + implementation | worker for research, main for execution |
| Cleanup / QA after prior damage | audit first, mutate second |

## Anti-Patterns
- ❌ Write first, think later
- ❌ Batch-edit without sampling current state
- ❌ Claim completion from partial evidence
- ❌ Parallelize overlapping writes without ownership boundaries
- ❌ Let one giant script run blind on unstable infrastructure
- ❌ Keep stacking patches onto already-corrupted content without structural diagnosis

## Completion Standard
A task is only complete when all four are true:
1. the requested business outcome is addressed
2. the implementation path was efficient
3. the result was reviewed for quality
4. the result was verified in reality
