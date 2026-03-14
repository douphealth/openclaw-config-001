# Workflow: Keyword Architecture

## Output schema per URL
- url
- primary_keyword
- dominant_intent
- funnel_stage
- secondary_keywords[]
- question_keywords[]
- core_entities[]
- supporting_entities[]
- contextual_entities[]
- required_sections[]
- internal_link_targets[]

## Architecture rules
- One URL, one dominant primary family.
- Secondary terms must support the same intent.
- If two terms require different user outcomes, split URLs.
- Prioritize terms with clear solve-intent over vague broad terms.
