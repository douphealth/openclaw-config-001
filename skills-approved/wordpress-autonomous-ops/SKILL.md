---
name: wordpress-autonomous-ops
description: Autonomous WordPress operations with self-improvement, error pattern learning, outcome tracking, and auto-optimization. Use when WordPress operations need continuous improvement, error prediction, performance regression detection, or self-evolving optimization strategies. Triggers on: self-improving WP ops, autonomous optimization, error learning, performance tracking, auto-evolving strategies.
---

# WordPress Autonomous Ops — Self-Improving Enterprise Operations

## Purpose
Enable WordPress operations to learn from past errors, predict failures before they happen, auto-optimize execution strategies, and continuously improve operational quality through outcome tracking and pattern matching.

## When to Use
- After any WordPress operation that failed or had unexpected results
- Before batch operations (predict and prevent known error patterns)
- When performance has regressed (detect and diagnose)
- For continuous optimization of WordPress workflows
- When you need to learn from past site operations

**Do NOT use for:** Initial WordPress operations (→`wordpress-growth-ops`), SEO auditing (→`seo-audit-playbook`), general copywriting (→`conversion-copywriting`).

## Compatibility
- WordPress 6.9+ (REST API, WP-CLI, Application Passwords)
- PHP 8.0+ recommended
- WP-CLI preferred for backend operations
- Browser automation only when REST API insufficient

## Inputs Required (Pre-Flight)
- Target site URL and WordPress root path
- Authentication method (app password, WP-CLI, file access)
- Environment: production/staging (assume production unless stated)
- Constraints: no downtime, preserve SEO, preserve data

## Triage Protocol
Before ANY operation:
1. Identify content type (page vs post vs CPT) via body class or REST API
2. Check current state via API (GET before POST/PUT/DELETE)
3. Verify credentials work (test API call)
4. Check for conflicts (slug duplicates, concurrent modifications)
5. Plan rollback (how to undo if something breaks)

## Speed Optimizations (Official Patterns)
- Use `_fields` parameter to fetch only needed data (80%+ payload reduction)
- Batch operations: `per_page=100` for list endpoints
- Parallel API calls via `concurrent.futures` (max 10/site)
- WP-CLI for bulk operations (faster than REST API for many tasks)
- Cache post/category maps in session (don't re-fetch)
- Use `wp db query` for direct DB operations when REST API is too slow

## Self-Critique Scorecard (/25)
1. **Triage** (1-5): Was current state fully understood before changes?
2. **Execution** (1-5): Was the operation clean and efficient?
3. **Verification** (1-5): Verified via API + live page + body class?
4. **Rollback** (1-5): Can changes be undone if issues found?
5. **Learning** (1-5): Were new patterns documented?

**Target: 22+/25**

## Error Recovery (Auto-Learning)
- Track error patterns per site (404s, auth failures, cache issues)
- After 2 failures on same operation → try alternative approach
- Log recurring fixes to memory/YYYY-MM-DD.md
- Update error-patterns.md reference when new patterns discovered

## Output Contract
**Artifact**: WordPress operation completed and verified
**Evidence**: API response proof + live page verification + body class check
**Decision**: Operation successful or error pattern identified with recovery path
**Next**: Log pattern, update memory, or schedule follow-up verification

## Architecture

```
Operation History DB ←→ Pattern Matcher ←→ Prediction Engine
         ↑                    ↓                    ↓
    Outcome Log      Known Error Patterns   Prevention Rules
         ↓                    ↓                    ↓
    Success/Failure    Auto-Fix Suggestions   Optimized Strategy
```

## Core Concepts

### 1. Error Pattern Database
Maintain a persistent log of WordPress operation errors, their causes, and fixes:

```python
# Error patterns are stored in memory files
error_pattern = {
    "pattern": "wpautop_artifact_in_style",
    "symptoms": ["<p> inside <style>", "CSS broken", "visual artifacts"],
    "cause": "wpautop() ran on raw HTML content",
    "prevention": "Always wrap in <!-- wp:html --> blocks",
    "auto_fix": "scripts/wp-content-fix.py",
    "confidence": 0.95,  # How often this is the cause
    "occurrences": 373,  # How many times we've seen this
    "last_seen": "2026-03-16"
}
```

### 2. Operation Outcome Tracking
After every WordPress operation, log the outcome:

```python
outcome = {
    "operation": "batch_style_fix",
    "site": "gearuptofit.com",
    "timestamp": "2026-03-16T10:32:00Z",
    "scope": 373,  # items affected
    "duration_seconds": 180,
    "success": True,
    "errors": 0,
    "error_patterns": [],
    "pre_verification": {"posts_scanned": 1286, "artifacts_found": 373},
    "post_verification": {"posts_checked": 19, "artifacts_remaining": 0},
    "confidence": 0.98  # How confident we are in the result
}
```

### 3. Self-Critique Engine
Before claiming completion, run automated self-critique:

```markdown
## Self-Critique Scorecard

| Check | Status | Weight | Score |
|-------|--------|--------|-------|
| Live page verified | ✅ | 25% | 25 |
| API response checked | ✅ | 15% | 15 |
| Body class matches | ✅ | 15% | 15 |
| No slug conflicts | ✅ | 10% | 10 |
| Mobile rendering OK | ✅ | 10% | 10 |
| Money path intact | ✅ | 15% | 15 |
| No side effects detected | ✅ | 10% | 10 |

**Total**: 100/100 — Claim completion
**Threshold**: 80/100 to claim done, 60/100 for partial
```

### 4. Performance Regression Detection
Track key metrics over time and alert on regression:

```python
metrics_to_track = {
    "page_load_time": {"threshold": 3.0, "unit": "seconds"},
    "content_length": {"threshold_pct_change": 50, "unit": "chars"},
    "api_response_time": {"threshold": 2.0, "unit": "seconds"},
    "error_rate": {"threshold": 0.05, "unit": "ratio"},
    "style_block_artifacts": {"threshold": 0, "unit": "count"}
}
```

## Known Error Patterns (Learned)

### EP-001: Slug Conflict (Page vs Post)
```
Frequency: 3 occurrences
Symptom: Blank page despite content in DB
Detection: Body class page-id-N instead of postid-N
Prevention: Before modifying any content, check for duplicate slugs
Auto-fix: Force-delete the conflicting page
Risk: HIGH — Content completely invisible
```

### EP-002: wpautop Style Block Corruption
```
Frequency: 373+ occurrences
Symptom: CSS broken, <p> tags inside <style>
Detection: Regex scan for <p> or <br> inside <style>
Prevention: Always wrap content in <!-- wp:html --> for raw HTML
Auto-fix: scripts/wp-content-fix.py
Risk: MEDIUM — Visual breakage but content visible
```

### EP-003: post_content Wiped to 0
```
Frequency: 2 occurrences
Symptom: content.raw = 0 but content.rendered has data
Detection: Check raw vs rendered length discrepancy
Prevention: Always verify raw content after batch operations
Auto-fix: Restore from rendered field
Risk: CRITICAL — Content lost from database
```

### EP-004: Elementor Template Blocking Content
```
Frequency: 1 occurrence
Symptom: Page blank between header/footer
Detection: Body class shows elementor_header_footer template
Prevention: Verify template before applying
Auto-fix: Change template to default or delete page
Risk: HIGH — Content invisible despite being correct
```

### EP-005: Script Tag Sanitization
```
Frequency: Multiple
Symptom: JavaScript not executing in post content
Detection: <script> tags absent from rendered content
Prevention: Use Code Snippets plugin or mu-plugins, not post content
Auto-fix: Migrate to Code Snippets REST API
Risk: MEDIUM — Functionality missing but content visible
```

## Execution Strategies

### Strategy A: Safe First (Default)
1. Check error patterns for known issues matching current operation
2. Apply prevention rules proactively
3. Execute operation with rate limiting
4. Verify first 3 items before continuing
5. Run self-critique on completion
6. Log outcome to history

### Strategy B: Aggressive (Batch Operations)
1. Pre-scan for all known error patterns
2. Fix all detected patterns before main operation
3. Execute in batches of 10
4. Verify every 10th item
5. Pause if error rate > 5%
6. Run full verification on completion
7. Log outcome and update error patterns

### Strategy C: Learning (New Operations)
1. Execute cautiously with verbose logging
2. Note any unexpected behavior
3. If error occurs, classify against known patterns
4. If new pattern, add to error database
5. Retry with adjusted approach
6. Log new pattern with symptoms, cause, prevention

## Auto-Optimization Rules

### Rule 1: Speed Optimization
```
IF operation took > 2x expected time THEN
    Identify bottleneck (network, API, processing)
    If API: increase batch size or parallelize
    If network: check for rate limiting, add delays
    If processing: optimize script or pre-compute
```

### Rule 2: Error Rate Optimization
```
IF error_rate > 5% THEN
    Pause operation
    Analyze error patterns
    If known pattern: apply auto-fix
    If new pattern: classify and learn
    Resume with adjusted approach
    If error_rate still > 5%: abort and escalate
```

### Rule 3: Verification Optimization
```
IF verification confidence > 0.95 AND items > 100 THEN
    Reduce verification sampling to 2%
    Still verify first 3 and last 3 items
    Trust intermediate verification
IF verification confidence < 0.80 THEN
    Increase verification sampling to 20%
    Add extra checks (live page, body class)
```

### Rule 4: Pattern Confidence Update
```
IF error_pattern matches AND fix works THEN
    confidence = min(confidence + 0.02, 0.99)
    occurrences += 1
    last_seen = now()
IF error_pattern matches BUT fix fails THEN
    confidence = max(confidence - 0.10, 0.10)
    Review cause and prevention rules
```

## Self-Improvement Protocol

### After Every Operation (Automatic)
1. Log outcome to `memory/YYYY-MM-DD.md`
2. If errors occurred → update error pattern database
3. If new pattern discovered → add with confidence 0.50
4. If operation was slow → identify bottleneck for next time
5. Update success rate metrics

### Weekly Review (Manual Trigger)
1. Review all operations from past week
2. Identify most common error patterns
3. Update prevention rules
4. Optimize execution strategies based on performance data
5. Update confidence scores for error patterns
6. Generate weekly performance report

### Monthly Evolution (Manual Trigger)
1. Analyze cumulative error patterns
2. Retire low-confidence patterns (< 0.20)
3. Merge similar patterns
4. Update auto-fix scripts based on learned patterns
5. Revise execution strategies for optimal performance

## Integration Points

### With wordpress-growth-ops
- Provides error pattern prevention before growth operations
- Receives operation outcomes for learning
- Shares auto-fix scripts for known patterns

### With auto-verification
- Uses verification results as outcome data
- Provides confidence scores for verification decisions
- Shares error patterns for pre-verification checks

### With memory-operations
- Stores error patterns in daily memory files
- Promotes high-confidence patterns to MEMORY.md
- Retrieves historical patterns for prediction

## Performance Optimizations

### Speed Multipliers
- Use `_fields` parameter to fetch only needed data
- Parallel API calls (max 10/site)
- Batch by site, never context-switch
- Pre-fetch auth before starting
- Cache category/post maps

### WP-CLI Speed Patterns
- `wp post list --field=ID` for fast ID-only queries
- `wp post meta get/update` for bulk meta operations
- `wp db query "SELECT..."` for complex data operations
- `wp cache flush` after major content changes
- `wp rewrite flush` after permalink changes
- `wp search-replace` for URL migrations (faster than REST API)

### Self-Critique Scorecard (/25)
1. **Functionality** (1-5): Does it work perfectly?
2. **Quality** (1-5): Enterprise-grade?
3. **Verification** (1-5): Verified via API + live + visual?
4. **Speed** (1-5): Optimal execution?
5. **Learning** (1-5): Patterns documented?

**Target: 22+/25**

### Auto-Check
- [ ] Pre-flight checks completed
- [ ] Verified via multiple methods
- [ ] Anti-patterns avoided
- [ ] Score logged to memory

## Output Contract
**Artifact**: Optimized operation with self-critique passed
**Evidence**: Error pattern check results, self-critique scorecard, outcome log
**Decision**: Operation successful with learned patterns updated
**Next**: Apply learned patterns to future operations

## Scripts
- `scripts/error-tracker.py` — Log and query error patterns
- `scripts/self-critique.py` — Automated self-critique scoring
- `scripts/performance-tracker.py` — Track and detect regressions
- `scripts/pattern-matcher.py` — Match current operation against known patterns

## References
- `references/error-patterns.md` — Full error pattern database
- `references/execution-strategies.md` — Detailed strategy selection guide
- `references/self-critique-criteria.md` — Complete self-critique checklist
- `references/performance-baselines.md` — Expected performance metrics
