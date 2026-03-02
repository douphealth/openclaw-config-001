---
name: schema-markup-generator
description: Use when the user asks to add schema markup, generate JSON-LD, enable rich snippets, or implement structured data types (FAQ, Product, Review, Article, Organization, etc.). Generate valid Schema.org JSON-LD with required/recommended properties and implementation guidance.
---

# Schema Markup Generator

## Objective
Generate accurate, policy-safe structured data that improves eligibility for rich results.

## Scope Boundaries
- Include: schema type selection, JSON-LD generation, validation guidance.
- Exclude: deceptive/fake markup, unsupported claims, unrelated technical SEO cleanup.

## Workflow
1. **Identify page purpose** and eligible schema types.
2. **Select primary schema** (and nested/related types only when justified).
3. **Map content to properties**: required first, then high-value recommended fields.
4. **Generate JSON-LD** with clean syntax and stable identifiers.
5. **Validate logic**: consistency with visible page content and real business data.
6. **Provide placement guidance** (head/body script injection path).
7. **Define QA checks** using schema validation + render confirmation.

## Quality Gates
- Markup must match on-page content exactly.
- Include all required properties for chosen type.
- Avoid spammy or fabricated ratings/reviews.

## Output Artifacts
Return:
1. Final JSON-LD block(s).
2. Field-by-field mapping notes.
3. Validation checklist and test steps.
4. Risk notes (if any property cannot be truthfully populated).
