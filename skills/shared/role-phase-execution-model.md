# Role / Phase Execution Model

Use this model when a task benefits from specialist thinking without needing a whole foreign framework.

## Roles
- **Strategist** — clarifies the outcome, constraints, and success criteria
- **Researcher** — gathers facts, audits current state, compares options
- **Implementer** — makes the change
- **Verifier** — checks reality independently of the implementer
- **Release Operator** — handles shipping, rollout, closure, and post-change monitoring

## Phases
1. **Intake** — what problem are we actually solving?
2. **Plan** — what are the minimum decisive steps?
3. **Build** — execute the smallest real change
4. **Review** — spec compliance + quality review
5. **Verify** — gather real proof
6. **Release/Close** — finalize state, docs, and next-step posture

## Usage Rules
- Tiny tasks may collapse all roles into one session.
- Meaningful tasks should at least separate implementer and verifier mentally, and often operationally.
- High-risk tasks should explicitly separate strategist, implementer, and verifier.

## Quality Trigger
If a task is ambiguous, public-facing, cross-system, or long-running, use explicit role/phase language in the plan and/or ledger.

## Why This Exists
This captures the best practical part of role-heavy systems like gstack and paperclip without importing command sprawl or alien runtime assumptions.
