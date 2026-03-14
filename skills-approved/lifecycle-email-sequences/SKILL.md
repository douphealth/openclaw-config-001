---
name: lifecycle-email-sequences
description: Use when designing or improving welcome sequences, nurture sequences, onboarding emails, re-engagement emails, post-purchase flows, or automated lifecycle email programs. Triggers on requests for drip campaigns, lead nurture, onboarding emails, email automation, follow-up flows, or conversion-oriented email sequences.
---

# Lifecycle Email Sequences

## Do NOT Use This For
- debugging broken email automation (use email-automation-debugging)
setting up the email marketing platform (use email-marketing-engine)

## Purpose
Design email sequences that move people through a lifecycle stage with clear timing, clear purpose, and measurable conversion intent.

## Use this when
Use this skill when the user needs a sequence rather than a single one-off email.

Do **not** use this skill for standalone page copy; use `conversion-copywriting`.
Do **not** use this skill to debug whether automation fires; use `email-automation-debugging`.

## Do this
1. Identify the trigger into the sequence.
2. Define the primary business goal and the stage goal.
3. Clarify what the audience already knows, believes, and hesitates about.
4. Map the sequence so each email has one job.
5. Set sensible timing based on urgency, complexity, and audience.
6. Write each email with one main CTA.
7. Define exit conditions and what success means.

## Sequence defaults
Common defaults (validated on production systems):
- welcome: 7 emails over 14 days (0h, 24h, 72h, 120h, 168h, 240h, 336h)
- nurture: 8 emails over 65 days (weekly after welcome)
- onboarding: 4-7 emails
- re-engagement/winback: 3 emails (0h, 72h, 336h after 30d inactive)
- post-purchase: 3-5 emails

Use fewer, better emails over padded sequences.
Daily emails are too aggressive for most audiences. Weekly is the sweet spot for nurture.

## Core rules
- One email, one job.
- Value before ask.
- Relevance beats frequency.
- Clear next step beats vague “learn more” wandering.
- Don’t send a sequence without a trigger, goal, and exit logic.
- Do not ship email sequences that sound like generic AI filler; subject, hook, and CTA should feel intentionally different.

## Output
Default output should include:
- sequence name
- trigger
- audience stage
- goal
- email-by-email map
- timing between emails
- subject line + preview line for each email
- main CTA for each email
- success metrics

## Resources
Read when needed:
- `references/sequence-types.md`
- `references/email-structure.md`


## Output Contract
**Artifact**: Email sequence with timing and content
**Evidence**: Sequence structure, enrollment proof
**Decision**: Sequence active and enrolling
**Next**: Monitor engagement metrics
## Checks and common mistakes
- Do not make every email sell.
- Do not repeat the same argument in five slightly different forms.
- Do not overload emails with multiple primary asks.
- Do not forget the operational side: trigger, segmentation, and exit rules.
