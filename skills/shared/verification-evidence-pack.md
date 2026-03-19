# Verification Evidence Pack

Reusable verification templates for common OpenClaw execution classes.

## 1. WordPress Content Edit Verification
Collect:
- pre-change backup exists
- REST API post state reflects expected content/title/excerpt/meta
- live page renders expected change
- H1 count correct
- canonical still correct
- no duplicate injected modules appeared

## 2. Batch Mutation Verification
Collect:
- number of targeted items
- number successfully changed
- number failed/skipped
- sampled live verification on at least 3 items or 10%, whichever is greater
- site health before/during/after batch
- rollback readiness still intact

## 3. SEO Audit Verification
Collect:
- GSC data source used and date range
- Bing source used and date range
- crawl / robots / sitemap checks
- top opportunities ranked by evidence and impact
- exact next move identified

## 4. Render Integrity Verification
Collect:
- duplicate block counts before/after
- H1 count before/after
- presence/absence of malformed wrappers (`<!DOCTYPE`, `<html>`, `<body>`, embedded `<article>`)
- visual/live page confirmation on repaired sample pages

## 5. Money Path / Funnel Verification
Collect:
- critical path URL list
- each step loads successfully
- event / lead / order / email / redirect outcomes observed
- failure point identified if path breaks

## 6. Recovery Verification
Collect:
- current state snapshot
- canary restore/fix result
- post-fix health check
- before/after evidence
- explicit decision: recovered / partial / blocked
