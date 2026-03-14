# Memory Configuration

Enterprise-grade memory system configuration for OpenClaw.

## Files

### Core
| File | Purpose |
|------|---------|
| `MEMORY-RULES.md` | Complete memory operating manual |
| `INDEX.md` | Fast-retrieval index template |
| `README.md` | This file |

### Operations (`ops/`)
| File | Purpose |
|------|---------|
| `memory-health-signals.md` | Diagnose healthy/degraded/blocked memory |
| `memory-maintenance-system.md` | Ongoing maintenance procedures |
| `weekly-memory-review-checklist.md` | Weekly review step-by-step |

### Templates (`templates/`)
| File | Purpose |
|------|---------|
| `memory-note-template.md` | Structured note format |

### Macros (`macros/`)
| File | Purpose |
|------|---------|
| `memory-health-check.md` | Run a memory system health check |
| `memory-review.md` | Full memory review and consolidation |

## Quick Setup

```bash
# Copy memory config to workspace
cp config/memory/MEMORY-RULES.md ~/.openclaw/workspace/
cp config/memory/INDEX.md ~/.openclaw/workspace/memory/
cp config/memory/ops/*.md ~/.openclaw/workspace/memory/ops/
cp config/memory/templates/*.md ~/.openclaw/workspace/memory/templates/
cp config/memory/macros/*.md ~/.openclaw/workspace/ops/macros/

# Create entity directories
mkdir -p ~/.openclaw/workspace/memory/{people,sites,projects,ops}
```

## Architecture

```
memory/
├── MEMORY-RULES.md      # Operating manual
├── INDEX.md             # Fast-retrieval index
├── YYYY-MM-DD.md        # Daily raw logs
├── entities/            # Or direct subdirs:
│   ├── people/          # Person-specific context
│   ├── sites/           # Site state and knowledge
│   ├── projects/        # Project tracking
│   └── ops/             # Operational patterns
├── ops/                 # Memory system ops
│   ├── memory-health-signals.md
│   ├── memory-maintenance-system.md
│   └── weekly-memory-review-checklist.md
└── templates/
    └── memory-note-template.md
```

## Principles

1. **Three layers**: Daily (chronological) → Entity (subject) → Long-term (durable)
2. **Promote upward**: Daily → Entity → MEMORY.md (only durable truths)
3. **One current truth**: Update in place, don't accumulate fragments
4. **Retrieval order**: Entity file → semantic search → daily notes → MEMORY.md
5. **Never store secrets**: Use `.secrets/` directory
6. **Weekly review**: Consolidate, promote, prune

## Version

Memory config version: **1.0.0** (2026-03-14)
