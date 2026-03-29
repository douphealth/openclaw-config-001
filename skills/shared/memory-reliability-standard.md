# Memory Reliability Standard

## Purpose
Make memory handling more reliable, more responsive to explicit user instructions, and more useful under operational pressure.

## Core Rules
1. If the user specifies a cadence, reminder, reporting rhythm, or operational constraint, treat it as an execution requirement, not a suggestion.
2. Operational commitments should be written into durable workspace memory or task state, not trusted to conversational continuity alone.
3. Do not claim a timed follow-up unless there is a reliable support path for it; truthful constraint disclosure is better than a missed promise.
4. Memory should distinguish clearly between:
   - confirmed facts
   - current commitments
   - pending work
   - known failures
   - verified results
4. When a commitment is missed, record the failure pattern and tighten the system.
5. Prefer small durable operational facts over vague summaries.

## What Must Be Stored
When relevant, store:
- user preferences that shape execution style
- required reporting cadence
- quality bar / non-negotiables
- active site priorities
- blocked/unfinished work that must resume
- important truth about what is and is not solved

## Reliability Rules
- do not overstore noise
- do store commitments that affect behavior
- update stale commitments when reality changes
- prefer one clear durable note over repeated partial notes

## Anti-Patterns
- forgetting explicit timing/reporting instructions
- storing only outcomes but not obligations
- saying work is continuing without durable task-state support
- leaving active execution mode implicit instead of recorded
