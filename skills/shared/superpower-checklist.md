# Superpower Checklist

Use this before and after serious work.

## Before execution
- [ ] Is the task outcome truly clear?
- [ ] If not, did I clarify/spec it first?
- [ ] Is there a short execution plan?
- [ ] Did I identify what can be parallelized safely?
- [ ] Did I identify rollback before mutation?
- [ ] Did I verify site/system health first?

## During execution
- [ ] Am I using the smallest decisive operation first?
- [ ] Am I batching or parallelizing where safe?
- [ ] Am I avoiding duplicate or overlapping writes?
- [ ] Am I reporting progress for long tasks?
- [ ] Am I stopping when infrastructure becomes unstable?

## Before completion
- [ ] Review 1: does the result match the requested outcome?
- [ ] Review 2: is the output clean, minimal, non-duplicative, and high-quality?
- [ ] Did I verify live reality, not just save state?
- [ ] Did I capture lessons / patterns if this exposed a repeatable workflow?
