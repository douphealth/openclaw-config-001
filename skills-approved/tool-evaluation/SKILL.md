---
name: tool-evaluation
description: Use when comparing software, vendors, services, platforms, or internal tool choices for adoption, replacement, or standardization. Triggers on requests to evaluate tools, compare platforms, choose between vendors, assess ROI, assess security/integration fit, or recommend the best tool for a business workflow.
---

# Tool Evaluation

## Do NOT Use This For
- implementing the chosen tool (use the relevant operational skill)
SEO-specific analysis (use seo-audit-playbook)

## Purpose
Choose tools with less bias, less vendor fantasy, and better total-cost judgment. Deliver a defensible recommendation, not a feature checklist.

## Use this when
- Comparing software, vendors, platforms, or internal tool choices
- Assessing ROI, security fit, or integration compatibility
- Choosing between 2+ options for a specific business workflow
- Standardizing tooling across a team or organization

Do **not** use for: implementing an already-chosen tool (go straight to implementation), reviewing open-source contributions (not a tool decision), or generic "what's the best X" without a specific use case.

## Do this

### Phase 1: Define the job
1. Write the job-to-be-done in one sentence: "We need [tool] to [outcome] for [audience] given [constraints]."
2. List non-negotiable constraints (must-have integrations, compliance, budget ceiling, deployment model).
3. Identify the evaluation team and decision-maker.

### Phase 2: Evaluation rubric
4. Score each option across these dimensions (1–5 scale):

| Dimension | Weight | What it measures |
|-----------|--------|-----------------|
| **Functionality fit** | 25% | Does it actually do the job well? |
| **Integration fit** | 20% | Connects to existing stack without duct tape |
| **Usability** | 15% | Team can adopt without heavy training |
| **Security & risk** | 15% | Data handling, compliance, vendor stability |
| **Total cost** | 15% | Price + training + migration + maintenance |
| **Vendor quality** | 10% | Support, roadmap, community, documentation |

5. Adjust weights for context: security-heavy orgs bump risk, startups bump usability.
6. Test claims against realistic scenarios — vendor demos are theater.

**Scoring guide:**
| Score | Meaning |
|-------|---------|
| 5 | Exceeds requirement, category leader |
| 4 | Meets requirement with room to spare |
| 3 | Meets requirement adequately |
| 2 | Partially meets requirement, gaps exist |
| 1 | Fails requirement or not available |

### Phase 3: Decision matrix
7. Build the comparison matrix with scores and written rationale per cell.
8. Separate must-haves from nice-to-haves — fail any must-have = eliminated.
9. Note switching cost, training cost, and lock-in risk for each option.
10. Distinguish "best in class" from "best for this team right now."

**Decision matrix format:**
| Option | Functionality (25%) | Integration (20%) | Usability (15%) | Security (15%) | Cost (15%) | Vendor (10%) | Weighted Total |
|--------|-------------------|------------------|----------------|---------------|-----------|-------------|---------------|
| Tool A | 4 → 1.00 | 3 → 0.60 | 4 → 0.60 | 5 → 0.75 | 3 → 0.45 | 4 → 0.40 | **3.80** |
| Tool B | 5 → 1.25 | 2 → 0.40 | 3 → 0.45 | 4 → 0.60 | 5 → 0.75 | 3 → 0.30 | **3.75** |

### Phase 4: Recommend
11. Recommend with explicit tradeoffs: what you gain and what you give up.
12. State adoption risks and mitigation steps.
13. Provide a 90-day adoption plan if recommendation is accepted.

## Core rules
- Do not recommend a tool purely because it is popular.
- Include switching cost, training cost, and lock-in risk.
- Security and integration fit are default dimensions, not optional extras.
- Do not assume enterprise pricing is justified by brand alone.
- Do not hide uncertainty where hands-on testing was limited.

## Output contract
Deliver:
1. **Job definition** — one-sentence job-to-be-done with constraints
2. **Options compared** — table with all candidates
3. **Evaluation matrix** — weighted scores per dimension with rationale
4. **Strengths / weaknesses** — top 3 per option
5. **Cost / risk notes** — TCO, lock-in, migration friction
6. **Recommendation** — clear pick with tradeoffs stated
7. **Adoption plan** — 90-day rollout steps, risks, and mitigations
8. **Confidence level** — based on hands-on testing vs. desk research

## Verification steps
- [ ] All non-negotiable constraints are checked for each option
- [ ] At least one realistic scenario tested per option (not just vendor claims)
- [ ] TCO includes training, migration, and maintenance — not just license cost
- [ ] Recommendation explicitly states tradeoffs and risks
- [ ] Decision-maker can defend this choice in a meeting
- [ ] Weights are justified and appropriate for the context

## Resources
Read when needed:
- `references/evaluation-criteria-starter.md`

## Checks and common mistakes
- Do not evaluate tools as feature-checklist theater.
- Do not ignore migration friction — it kills adoption.
- Do not weight flashy features over daily workflow fit.
- Do not present one option as "obviously best" without the matrix to back it.
- Do not skip the adoption plan — choosing the tool is half the job.
- Do not let one enthusiastic stakeholder override the evaluation.

## Output Contract
**Artifact**: Skill-specific deliverable (report, fix, config, or document)
**Evidence**: Proof that the work was completed correctly
**Decision**: What was decided or recommended
**Next**: Follow-up action or monitoring period
