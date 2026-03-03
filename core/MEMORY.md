# MEMORY.md — Long-Term Operating Memory

# schema
_version: 2.0
# last_
updated: 2026-02-28

Memory is the compounding advantage. Degraded memory = repeated failures.

## Mission

→ Aligned with USER.md §Goals. Summary: Organic traffic · topical authority · GEO/AEO visibility · affiliate revenue · monetization quality.

## Lessons Learned (Permanent — append only, never delete)

1.   Speed without safeguards causes costly failures.
2.   Homepages and trust pages are high-blast-radius surfaces.
3.   Quality consolidation beats raw volume.
4.   AEO wins require answer-first formatting and clean structure.
5.   Memory quality degrades without same-day evidence logging.
6.   Memory hygiene requests: apply immediately in-session.
7.   Growth OS beats ad-hoc hotfix loops.
8.   Blind text replacement on live content is dangerous.
9.   Cache/parser variance creates false signals; require dual confirmation.
10.   Internal linking must not be fully automated.
11.   Programmatic page creation must be paced and gated.
12.   Entity optimization beats keyword repetition.
13.   Content refresh is S-tier and underused.
14.   Schema injection should be per-template where possible.
15.   Never fabricate EPC, conversion rates, ranking certainty, or benchmarks.
16.   Never collapse subsystem truth into a single status label without verifying each gate.
17.   If user trust is impacted by missed disclosure, prioritize immediate correction over routine optimization.

## Superseded Claims Register (append only — never delete)

| Claim ID | Superseded At | Evidence | Reason |
|---|---|---|---|
| canonical-2026-02-24-noise-fail-loop | 2026-02-24T19:38Z | reports/gearuptofit-homepage-canonical-watchdog.log | Parser/network variance |
| gutf-blind-year-replacement-safe | 2026-02-24T16:02Z | reports/gearuptofit-year-correction-pass-2026-02-24.md | Corrected from blind to context-safe |

## Workflow Baseline (Growth OS)

1. **Stabilize** — health / canonical / indexability / schema
2. **Monetize** — offer map, intent tiers, affiliate compliance, CTA architecture
3. **Rank** — entity optimization, clustering, AEO/snippet/schema
4. **Scale** — template-level fixes, controlled automation, paced programmatic
5. **Verify + Log** — hard evidence, same-session memory update

## Memory Hygiene

-   Every supersession needs evidence anchor (message ID / timestamp).
-   No mental notes — externalize everything to files.
-   Episodic logs → memory/YYYY-MM-DD.md (→ AGENTS.md §Documentation).

## Structured Memory Store
- Facts + Events stored in `state/memory_store.db` (sqlite)
- Query: `python3 core/memory_query.py facts --limit 20`
- Route new items: `python3 core/memory_router.py --kind fact --key <key> --value <value>`
- Compact old daily logs: `python3 core/memory_compact.py --days 5`
- Lint: `python3 core/memory_hygiene_lint.py`
