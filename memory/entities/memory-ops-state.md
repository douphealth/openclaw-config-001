# Entity: Memory Ops State

## Type
system

## Context
Durable record of the upgraded memory system so future sessions do not regress to weaker assumptions.

## Current State
- Memory search is enabled and actively tuned.
- Active `memory/` now contains only real daily logs plus control files; placeholder stubs were archived to `artifacts/memory/placeholder-daily-archive/`.
- `MEMORY.md` remains concise and curated.
- `memory/entities/` is now a first-class durable memory layer.
- Weekly memory maintenance is automated by cron job `weekly-memory-maintenance`.

## Runtime Tuning
- `sources = ["memory"]`
- `sync.onSessionStart = true`
- `sync.onSearch = true`
- `sync.watch = true`
- `sync.watchDebounceMs = 1500`
- `sync.intervalMinutes = 15`
- `query.maxResults = 8`
- `query.minScore = 0.32`
- `cache.enabled = true`
- `cache.maxEntries = 20000`
- `chunking.tokens = 420`
- `chunking.overlap = 80`

## Durable Rules
- Keep durable facts in `MEMORY.md` or `memory/entities/*.md`, not buried only in daily logs.
- Archive synthetic placeholder date files rather than leaving them in active indexed paths.
- Prefer subtraction of memory noise before adding more retrieval complexity.
- Memory health should be measured with deterministic checks and scoring, not intuition.

## Evidence
- `artifacts/memory/2026-03-22-memory-upgrade.md`
- `artifacts/memory/2026-03-22-memory-phase2-complete.md`

## Status
active
