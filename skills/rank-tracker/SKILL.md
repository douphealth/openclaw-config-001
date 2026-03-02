---
name: rank-tracker
description: Use when the user asks to track rankings, monitor keyword positions, detect ranking changes, or review SERP movement over time. Track baseline and deltas across priority keywords, pages, and SERP features, then flag significant wins/losses with likely causes.
---

# Rank Tracker

## Objective
Provide reliable visibility into ranking movement and what action should happen next.

## Scope Boundaries
- Include: keyword position tracking, trend analysis, volatility alerts, page-keyword mapping.
- Exclude: full technical remediation and long-form content writing.

## Workflow
1. **Define tracking set**: domain, location/device, keyword clusters, mapped URLs.
2. **Capture baseline**: initial positions, SERP features, and ownership status.
3. **Track intervals**: daily/weekly snapshots with consistent methodology.
4. **Calculate deltas**: gains/losses by keyword, URL, and cluster.
5. **Detect events**: significant moves, feature wins/losses, cannibalization signals.
6. **Diagnose likely drivers**: content changes, technical issues, competitor displacement.
7. **Recommend actions**: refresh content, improve internal links, snippet optimization, etc.

## Quality Gates
- Never report movement without baseline reference.
- Distinguish noise from meaningful trend.
- Flag data-quality uncertainty explicitly.

## Output Artifacts
Return:
1. Position change table (now vs previous period).
2. Winners/losers summary by cluster and URL.
3. Alert list for material drops/opportunities.
4. Next-step action queue with priority.
