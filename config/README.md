# OpenClaw Workspace Configuration

Enterprise-grade workspace configuration files for OpenClaw agent deployments.

## Files

| File | Purpose | Required |
|------|---------|----------|
| `AGENTS.md` | Root operating instructions | ✅ Yes |
| `SOUL.md` | Agent personality and values | ✅ Yes |
| `USER.md` | User profile template | ✅ Yes |
| `TOOLS.md` | Infrastructure cheat sheet template | ✅ Yes |
| `IDENTITY.md` | Agent identity template | ✅ Yes |
| `MEMORY.md` | Long-term memory template | ✅ Yes |
| `HEARTBEAT.md` | Periodic check instructions | ✅ Yes |

## Quick Setup

```bash
# Copy all config files to workspace
cp config/AGENTS.md ~/.openclaw/workspace/
cp config/SOUL.md ~/.openclaw/workspace/
cp config/USER.md ~/.openclaw/workspace/
cp config/TOOLS.md ~/.openclaw/workspace/
cp config/IDENTITY.md ~/.openclaw/workspace/
cp config/MEMORY.md ~/.openclaw/workspace/
cp config/HEARTBEAT.md ~/.openclaw/workspace/

# Create memory directory
mkdir -p ~/.openclaw/workspace/memory

# Create secrets directory (never commit this)
mkdir -p ~/.openclaw/workspace/.secrets
```

Or use the setup script:
```bash
bash config/scripts/setup-workspace.sh
```

## Customization

1. **SOUL.md**: Adjust personality to match your preferences
2. **USER.md**: Fill in your profile, sites, and preferences
3. **TOOLS.md**: Add your infrastructure details
4. **IDENTITY.md**: Let the agent choose its own identity
5. **HEARTBEAT.md**: Configure periodic checks for your workflow


## Memory Configuration

Full memory system configuration in `config/memory/`:
- `MEMORY-RULES.md` — Complete memory operating manual
- `INDEX.md` — Fast-retrieval index template
- `ops/` — Health signals, maintenance system, weekly checklist
- `templates/` — Structured memory note template
- `macros/` — Memory health check and review macros

See `config/memory/README.md` for full documentation.
## Security

- **Never commit** `.secrets/` directory
- **Never store** credentials in MEMORY.md or TOOLS.md
- **MEMORY.md** should only be loaded in main sessions (security)
- All credential references use `.secrets/` paths

## Architecture

```
~/.openclaw/workspace/
├── AGENTS.md          # Root instructions (always read first)
├── SOUL.md            # Personality (always read)
├── USER.md            # User profile (always read)
├── TOOLS.md           # Infrastructure (read as needed)
├── IDENTITY.md        # Agent identity (read on bootstrap)
├── MEMORY.md          # Long-term memory (main session only)
├── HEARTBEAT.md       # Heartbeat instructions
├── memory/
│   ├── YYYY-MM-DD.md  # Daily raw logs
│   ├── entities/      # People, sites, projects
│   └── heartbeat-state.json
├── skills/            # Skill definitions (from skills-approved/)
├── ops/               # Operational scripts and configs
├── .secrets/          # Credentials (NEVER commit)
└── templates/         # Reusable templates
```

## Version

Config version: **1.0.0** (2026-03-14)
Aligned with: **MANIFEST.yaml v3** (36 enterprise-grade skills)
