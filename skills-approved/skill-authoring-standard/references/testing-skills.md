# Testing Skills

Use this reference for skills where failure is costly, fragile, or easy to rationalize away.

## When to test hard
Use stronger testing when a skill:
- enforces discipline
- controls risky sequences
- is likely to be bypassed under pressure
- must work consistently across repeated runs

## Lightweight RED-GREEN-REFINE loop

### 1. Baseline
Before polishing the skill, check what happens without it.
Ask:
- what would an agent naturally do here?
- where would it cut corners?
- what ambiguity would produce the wrong action?

### 2. Minimal skill
Write only enough to prevent the observed failure modes.
Do not write a giant “just in case” manual.

### 3. Pressure test
Test with realistic scenarios, especially where shortcuts are tempting:
- time pressure
- sunk cost
- ambiguity
- authority pressure
- tedious manual work

Force concrete choices where possible.

### 4. Refine
If the skill still fails:
- capture the exact ambiguity or loophole
- tighten the wording
- add a clearer check or decision rule
- re-test

## What to capture during testing
- the prompt/scenario
- the wrong or risky behavior
- the rationalization used
- the wording change that fixed it

## Good patterns
- bright-line rules for fragile operations
- explicit “do not” bullets when a known shortcut causes failure
- checklists for multi-step workflows
- verification steps near the action, not buried at the end

## Don’t overdo it
Do not run heavy pressure testing for every reference skill.
API docs, schemas, and lookup skills usually need retrieval/usefulness checks, not behavioral stress tests.

## Minimal acceptance questions
Before calling a skill done, ask:
1. Will another agent know when to trigger it?
2. Will another agent know what to do first?
3. Are the risky parts constrained tightly enough?
4. Are bulky details moved out of the main file?
5. Would this still be useful a month from now?
