#!/usr/bin/env bash
# OpenClaw Workspace Setup Script
# Initializes a new workspace with enterprise-grade config files

set -euo pipefail

WORKSPACE="${OPENCLAW_WORKSPACE:-$HOME/.openclaw/workspace}"
CONFIG_DIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "🚀 OpenClaw Workspace Setup"
echo "   Workspace: $WORKSPACE"
echo ""

# Create directories
mkdir -p "$WORKSPACE"/{memory,skills,ops,templates,.secrets}
mkdir -p "$WORKSPACE"/memory/{entities,people,sites,projects,ops}

# Copy config files
for file in AGENTS.md SOUL.md USER.md TOOLS.md IDENTITY.md MEMORY.md HEARTBEAT.md; do
    src="$CONFIG_DIR/$file"
    dst="$WORKSPACE/$file"
    if [ -f "$dst" ]; then
        echo "  ⚠️  $file exists — skipping (remove and rerun to overwrite)"
    else
        cp "$src" "$dst"
        echo "  ✅ $file"
    fi
done

# Create .gitignore for secrets
if [ ! -f "$WORKSPACE/.gitignore" ]; then
    cat > "$WORKSPACE/.gitignore" << 'GITIGNORE'
# Secrets - NEVER commit
.secrets/

# Memory - personal data
memory/

# OS files
.DS_Store
Thumbs.db

# Editor files
*.swp
*.swo
*~
GITIGNORE
    echo "  ✅ .gitignore"
fi

# Create heartbeat state
if [ ! -f "$WORKSPACE/memory/heartbeat-state.json" ]; then
    echo '{"lastChecks":{"memory":null,"projects":null,"sites":null}}' > "$WORKSPACE/memory/heartbeat-state.json"
    echo "  ✅ heartbeat-state.json"
fi

echo ""
echo "✅ Workspace initialized at $WORKSPACE"
echo ""
echo "Next steps:"
echo "  1. Edit USER.md with your profile and sites"
echo "  2. Edit TOOLS.md with your infrastructure"
echo "  3. Add secrets to .secrets/ directory"
echo "  4. Restart OpenClaw agent to pick up new config"
