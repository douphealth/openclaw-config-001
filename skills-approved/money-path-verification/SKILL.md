---
name: money-path-verification
description: Use when verifying that a revenue path, lead path, checkout, signup flow, booking flow, email automation, or product delivery flow actually works end to end. Triggers on requests to verify a launch, prove checkout, validate a funnel, test lead capture, confirm order creation, confirm delivery, or ensure a site’s primary money path is truly working.
---

# Money Path Verification

## Purpose
Prove that a site’s critical conversion path works in reality, not just in theory.

## Use this when
Use this skill for final checks, launch proof, regression verification, or when trust is low and evidence matters.

## Verification standard
Do not call a path complete until you have evidence for the relevant end-to-end steps.
Default to “not yet proven” when evidence is partial, stale, or indirect.

## Do this
1. Identify the site and primary path.
2. Read the site playbook in `ops/sites/`.
3. Read matching `ops/launch-packs/` and `ops/constraints/` files if they exist.
4. Use the shortest real-world proof path.
5. Capture evidence at each critical step.
6. Report exactly what is proven, what is inferred, and what remains unverified.

## Path types
### Product / commerce path
Prove:
- add to cart
- checkout loads
- payment options appear
- order is created or payment succeeds where safe to test
- delivery / access path works

### Lead capture path
Prove:
- CTA path opens correctly
- form or bot submits successfully
- contact record is created
- automation or first follow-up can be evidenced

### Booking / service path
Prove:
- primary CTA path
- booking or inquiry form submission
- lead capture / routing
- confirmation or follow-up path

## Evidence rules
Strong evidence includes:
- success response payloads
- created records visible via API or admin endpoints
- live browser evidence when UI state matters
- post-submit proof such as subscriber, order, or message creation
- a fresh end-to-end proof using a new test input when cached/old records could mislead

Weak evidence:
- button looks clickable
- page loads without actually submitting
- assumptions from static markup alone
- old order/lead artifacts reused as if they prove the current path still works

## Resources
Read when needed:
- `references/evidence-standard.md`
- `references/site-special-cases.md`

Pair with `launch-readiness-audit` when the task is an overall go/no-go decision rather than proof of one path.
Pair with `email-automation-debugging` when the unresolved risk is signup-to-email execution.

## Checks and common mistakes
- Do not stop at UI polish when the underlying path is unproven.
- Do not use the wrong submission mechanism if the real system uses AJAX or JS-rendered behavior.
- Do not mark a path done from front-end appearance alone.
- Do not hide uncertainty; state it plainly.

## Output Contract
**Artifact**: Skill-specific deliverable (report, fix, config, or document)
**Evidence**: Proof that the work was completed correctly
**Decision**: What was decided or recommended
**Next**: Follow-up action or monitoring period
