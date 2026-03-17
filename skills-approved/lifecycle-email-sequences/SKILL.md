---
name: lifecycle-email-sequences
description: Use when designing or improving welcome sequences, nurture sequences, onboarding emails, re-engagement emails, post-purchase flows, or automated lifecycle email programs. Triggers on requests for drip campaigns, lead nurture, onboarding emails, email automation, follow-up flows, or conversion-oriented email sequences.
---

# Lifecycle Email Sequences

## Do NOT Use This For
- debugging broken email automation (use `email-automation-debugging`)
- setting up the email marketing platform (use `email-marketing-engine`)

## Purpose
Design email sequences that move people through a lifecycle stage with clear timing, clear purpose, and measurable conversion intent.

## Use this when
The user needs a sequence rather than a single one-off email. Not for standalone page copy (use `conversion-copywriting`) or debugging whether automation fires (use `email-automation-debugging`).

## Decision Tree

```
Email sequence needed?
├── New subscriber just opted in? → Welcome sequence
├── Lead not converting? → Nurture sequence
├── New customer/account? → Onboarding sequence
├── Inactive subscriber? → Re-engagement/winback
├── Just purchased? → Post-purchase sequence
└── Custom lifecycle stage? → Define stage → Map goals → Build
```

## Sequence Architecture Template

```
Sequence: [NAME]
Trigger: [What starts enrollment]
Exit conditions: [What removes someone — purchase, goal met, unsubscribe]
Goal: [Primary business outcome + stage goal]
Audience state: What they know, believe, and hesitate about

Email 1: [Job] → CTA → Timing: [X hours after trigger]
Email 2: [Job] → CTA → Timing: [+X hours]
Email 3: [Job] → CTA → Timing: [+X hours]
...
Success metric: [Open rate, click rate, conversion, reply rate]
Failure signals: [High unsubscribe, no opens after email 3, spam complaints]
```

### One Email = One Job
Before writing, define the single job for each email:
- **Belief shift**: Change what they think about X
- **Objection handling**: Remove barrier Y
- **Social proof**: Show others like them succeeding
- **Value delivery**: Teach something useful
- **Conversion ask**: Make the specific offer

## Sequence Defaults (Production-Validated)

| Sequence | Emails | Duration | Cadence |
|---|---|---|---|
| Welcome | 7 | 14 days | 0h, 24h, 72h, 120h, 168h, 240h, 336h |
| Nurture | 8 | 65 days | Weekly after welcome |
| Onboarding | 4-7 | 14-21 days | Every 2-3 days |
| Re-engagement | 3 | 16 days | 0h, 72h, 336h (after 30d inactive) |
| Post-purchase | 3-5 | 14-21 days | Every 3-5 days |

**Guidelines**:
- Fewer, better emails > padded sequences
- Daily emails are too aggressive for most audiences
- Weekly is the sweet spot for nurture
- Front-load value in welcome sequences (first 3 emails set the tone)

## Timing Optimization

### When to Speed Up
- High-intent trigger (just purchased, just signed up for trial)
- Time-sensitive offer or deadline
- Audience expects fast follow-up (B2B demo requests)

### When to Slow Down
- Complex product needs education before buying
- Audience is skeptical or has long buying cycles
- Previous sequences showed high unsubscribe in first 3 days

### Send Time Rules
- Test Tuesday-Thursday vs. Monday/Friday (Tues-Wed typically wins for B2B)
- Send during audience's local business hours for B2B
- For B2C, evenings and weekends often outperform
- Avoid sending during major holidays unless seasonal

## Segment-Based Personalization

### Personalization Layers
| Layer | Example | Impact |
|---|---|---|
| **Identity** | Name, company | Low (table stakes) |
| **Context** | Lead source, page visited | Medium (relevance) |
| **Behavior** | Clicked X, opened Y emails | High (engagement) |
| **Stage** | New lead vs. warm lead vs. hot lead | Highest (timing) |

### Branch Logic Template
```
IF [segment condition] THEN [send Email X]
ELSE IF [different condition] THEN [send Email Y]
ELSE [default Email Z]

Example:
IF clicked "pricing" link → send objection-handling email
ELSE IF opened 3+ emails but no clicks → send different CTA angle
ELSE → standard sequence continues
```

**Rule**: Don't branch on identity alone (name, company). Branch on behavior and stage.

## Conversion Tracking Per Email

Track these metrics for each email in a sequence:

| Metric | Benchmark (welcome) | Benchmark (nurture) | Red Flag |
|---|---|---|---|
| Open rate | 40-60% | 25-40% | <20% = subject line problem |
| Click rate | 5-15% | 3-8% | <2% = CTA/offer problem |
| Conversion rate | 2-8% | 1-4% | <1% = landing page or offer mismatch |
| Unsubscribe rate | <0.5% | <0.3% | >1% = relevance/timing problem |
| Reply rate (B2B) | 5-15% | 3-10% | <2% = not personal enough |

### Diagnostic by Drop-off Point
```
Email 1 low opens → Subject line or sender name problem
Email 1 high opens, low clicks → Content doesn't deliver on subject promise
Email 2-3 opens drop sharply → Timing too aggressive or content not valuable
Email 4+ no conversions → Offer is wrong for this segment
Steady opens/clicks, no conversions → Landing page or checkout issue
```

## Per-Email Blueprint

Each email should follow this structure:

```
Subject: [Curiosity/benefit-driven, <50 chars]
Preview: [Completes the thought, <90 chars]

Hook (first 2 lines): [Pattern interrupt or relevance statement]
Body: [One idea, expanded with proof/story]
CTA: [One clear action — button + text link]
PS: [Optional — urgency, social proof, or secondary angle]
```

## Core Rules
- One email, one job.
- Value before ask.
- Relevance beats frequency.
- Clear next step beats vague "learn more" wandering.
- Don't send a sequence without a trigger, goal, and exit logic.
- Do not ship email sequences that sound like generic AI filler; subject, hook, and CTA should feel intentionally different.

## Output Template

```markdown
## Sequence: [NAME]
**Trigger**: [event]
**Exit**: [conditions]
**Goal**: [business outcome]
**Audience stage**: [awareness level]

### Performance Targets
| Metric | Target | Red Flag |
|---|---|---|
| Open rate | [X%] | [<Y%] |
| Click rate | [X%] | [<Y%] |
| Conversion | [X%] | [<Y%] |

### Email Map
| # | Job | Subject | CTA | Timing |
|---|---|---|---|---|
| 1 | [job] | [subject] | [CTA] | 0h |
| 2 | [job] | [subject] | [CTA] | +24h |
| ... | | | | |

### Branch Points
[Segment logic or behavioral triggers]

### Success/Failure Criteria
- Success: [what indicates the sequence is working]
- Failure: [what triggers a rethink]
```

## Output Contract
**Artifact**: Email sequence with timing, content map, and branch logic
**Evidence**: Sequence structure documented, enrollment rules defined
**Decision**: Sequence active and enrolling with clear success criteria
**Next**: Monitor engagement metrics for 2 weeks, optimize based on drop-off data

## Checks and Common Mistakes
- Do not make every email sell.
- Do not repeat the same argument in five slightly different forms.
- Do not overload emails with multiple primary asks.
- Do not forget the operational side: trigger, segmentation, and exit rules.
- Do not launch without defining what "working" looks like numerically.
- Do not skip the first email's subject line test — it sets open-rate baseline for the whole sequence.

## Resources
Read when needed:
- `references/sequence-types.md`
- `references/email-structure.md`

## Performance Optimizations

### Speed Multipliers
- Use proven email templates as starting point (subject lines, CTAs, structure)
- Batch API calls for email platform operations
- Pre-fetch subscriber data and sequence info in parallel
- Template-based email generation (don't start from blank)
- A/B test subject lines and CTAs

### Self-Critique Scorecard (/25)
1. **Functionality** (1-5): Does the email/sequence work perfectly?
2. **Quality** (1-5): Is the copy enterprise-grade?
3. **Verification** (1-5): Verified via API + test email + automation check?
4. **Speed** (1-5): Optimal execution?
5. **Learning** (1-5): Patterns documented?

**Target: 22+/25**

### Auto-Check
- [ ] Pre-flight checks (credentials, list/sequence exists)
- [ ] Verified via API + test send
- [ ] Subject line and CTA optimized
- [ ] Score logged to memory

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
