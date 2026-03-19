# Skill Trigger Engine Spec

A practical trigger policy for automatic skill activation in OpenClaw.

## Purpose
Make skill activation more automatic, less subjective, and more consistent across sessions.

## Trigger Priority Order
1. **Hard match** — explicit user request maps directly to one skill
2. **Risk match** — high-risk / unstable / ambiguous work activates meta-control skills first
3. **Workflow match** — multi-step work activates intake/orchestration skills
4. **Domain match** — specialist skill based on content/system/task type
5. **Fallback route** — if unclear, use `skill-router`

## Activation Rules

### Rule 1 — Use control/meta skills before specialist skills when:
- the task is ambiguous
- production risk exists
- multiple specialist skills could apply
- the task includes both research and execution
- the environment is unstable

Activate:
- `using-superpowers`
- `task-intake-spec-writer`
- `failure-recovery-director` (if failure/instability present)

### Rule 2 — Use orchestration skills when scale exists
Activate:
- `parallel-execution-director` when independent subtasks exist
- `batch-mutation-controller` when >10 similar writes may occur
- `execution-state-ledger` when work is interruption-prone or long-running

### Rule 3 — Use recovery skills when damage or instability already exists
Activate:
- `failure-recovery-director` for partial failures / unstable infrastructure / broken state
- `content-integrity-cleanup` for duplicated or malformed content/render issues
- `wp-error-recovery` for WordPress-specific failure modes

### Rule 4 — Use audit synthesis before execution on serious site reviews
Activate:
- `site-audit-director` for full-site audits
- then route to implementation skills only after the prioritized queue exists

## Trigger Keywords by Intent

### Meta / Control
- best strategy
- most efficient
- enterprise grade
- serious
- autonomous
- parallel
- orchestration
- plan this
- high quality

### Recovery
- broken
- duplicated
- distorted
- not showing correctly
- corrupted
- timeouts
- unstable
- rollback
- restore

### Batch / Scale
- all posts
- all pages
- sitewide
- in bulk
- across all
- scan everything
- batch

## Decision Table
| Situation | First skill |
|---|---|
| vague, risky, multi-step | `using-superpowers` |
| vague request that needs spec | `task-intake-spec-writer` |
| many independent subtasks | `parallel-execution-director` |
| many similar writes | `batch-mutation-controller` |
| unstable or failed execution | `failure-recovery-director` |
| duplicated/broken content render | `content-integrity-cleanup` |
| full site audit | `site-audit-director` |
| still unclear | `skill-router` |

## Completion Rule
The trigger engine succeeded when:
- the correct class of skill activated early
- unnecessary skills were not loaded
- execution mode matched task risk and scale
