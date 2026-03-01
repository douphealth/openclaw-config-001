---
name: email-welcome-sequence-automation
description: Build and automate a high-conversion 5-email welcome sequence using AIM (Acknowledge, Include, Mobilize) with behavior-based branching. Use when creating subscriber onboarding and first-offer conversion flows.
---

# Email Welcome Sequence Automation

## Scope Ownership
### Own
- Execute Build and automate a high-conversion 5-email welcome sequence using AIM (Acknowledge, Include, Mobilize) with behavior-based branching. Use when creating subscriber onboarding and first-offer conversion flows.
- Apply workflows, gates, and outputs defined in this file and its references/scripts.

### Do Not Own
- Do not override responsibilities of more specific domain skills when one clearly matches.
- Do not claim completion for adjacent systems without their direct verification gates.

## Framework
AIM = Acknowledge → Include → Mobilize

## 5-email blueprint
- Email 1 (0h): welcome + promised asset + expectation set
- Email 2 (+24h): key insight + pain alignment
- Email 3 (+3d): proof signal + trust reinforcement
- Email 4 (+7d): clear offer path (single CTA)
- Email 5 (+14d): re-engagement question + reply prompt

## Automation rules
- trigger: new confirmed subscriber
- exit: conversion event or completion
- branching: click behavior → relevant nurture path

## Copy constraints
- one email = one idea
- one primary CTA
- human voice, specific context, no fluff

## Verification
- trigger tested end-to-end
- delay logic correct
- exit conditions verified
- link tracking/tagging active

## Output
- sequence map
- email drafts
- trigger/exit logic
- KPI baseline