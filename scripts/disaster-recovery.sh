#!/bin/bash
# ============================================================================
# DISASTER RECOVERY — Full OpenClaw Workspace Backup & Restore
# Created: 2026-03-17
# Usage: 
#   Backup:  ./disaster-recovery.sh backup
#   Restore: ./disaster-recovery.sh restore <backup-file.tar.gz>
#   Full:    ./disaster-recovery.sh full-backup
# ============================================================================

set -e

WORKSPACE="$HOME/.openclaw/workspace"
BACKUP_DIR="$WORKSPACE/backups"
DATE=$(date +%Y%m%d-%H%M%S)
BACKUP_NAME="openclaw-disaster-recovery-$DATE"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

log() { echo -e "${GREEN}[$(date +%H:%M:%S)]${NC} $1"; }
warn() { echo -e "${YELLOW}[$(date +%H:%M:%S)]${NC} $1"; }
error() { echo -e "${RED}[$(date +%H:%M:%S)]${NC} $1"; }

# ============================================================================
# BACKUP
# ============================================================================
backup() {
    log "Starting disaster recovery backup..."
    
    TEMP_DIR="/tmp/$BACKUP_NAME"
    mkdir -p "$TEMP_DIR"
    
    # 1. Core config files
    log "Backing up core config files..."
    mkdir -p "$TEMP_DIR/core"
    for f in AGENTS.md SOUL.md USER.md TOOLS.md MEMORY.md HEARTBEAT.md IDENTITY.md SWARM.md MEMORY-RULES.md; do
        [ -f "$WORKSPACE/$f" ] && cp "$WORKSPACE/$f" "$TEMP_DIR/core/"
    done
    
    # 2. ALL skills
    log "Backing up all skills..."
    cp -r "$WORKSPACE/skills" "$TEMP_DIR/skills"
    
    # 3. Memory files
    log "Backing up memory..."
    cp -r "$WORKSPACE/memory" "$TEMP_DIR/memory"
    
    # 4. Ops scripts & configs
    log "Backing up ops..."
    mkdir -p "$TEMP_DIR/ops"
    cp -r "$WORKSPACE/ops/scripts" "$TEMP_DIR/ops/" 2>/dev/null || true
    cp -r "$WORKSPACE/ops/macros" "$TEMP_DIR/ops/" 2>/dev/null || true
    cp -r "$WORKSPACE/ops/checklists" "$TEMP_DIR/ops/" 2>/dev/null || true
    cp -r "$WORKSPACE/ops/portfolio" "$TEMP_DIR/ops/" 2>/dev/null || true
    cp -r "$WORKSPACE/ops/self-improvement" "$TEMP_DIR/ops/" 2>/dev/null || true
    cp -r "$WORKSPACE/ops/seo" "$TEMP_DIR/ops/" 2>/dev/null || true
    cp -r "$WORKSPACE/ops/sites" "$TEMP_DIR/ops/" 2>/dev/null || true
    cp -r "$WORKSPACE/ops/templates" "$TEMP_DIR/ops/" 2>/dev/null || true
    
    # 5. Secrets templates (NOT actual secrets!)
    log "Backing up secrets structure (templates only)..."
    mkdir -p "$TEMP_DIR/.secrets"
    # Save site config (non-sensitive)
    [ -f "$WORKSPACE/.secrets/seo-sites.json" ] && cp "$WORKSPACE/.secrets/seo-sites.json" "$TEMP_DIR/.secrets/"
    # Create restore template
    cat > "$TEMP_DIR/.secrets/RESTORE-TEMPLATE.md" << 'EOF'
# Secrets Restoration Guide

After restoring, recreate these files in .secrets/:

## WordPress Site Credentials
For each site, create: .secrets/{domain}.access.env
```
WP_USERNAME=your_username
WP_APP_PASSWORD=xxxx xxxx xxxx xxxx
```

## GSC Service Account
Create: .secrets/gsc-service-account.json
(Get from Google Cloud Console → Service Accounts)

## Bing API Key
Create: .secrets/bing-api-key.txt
(Get from Bing Webmaster Tools → Settings → API Access)

## Sites
affiliatemarketingforsuccess.com
efficientgptprompts.com
frenchyfab.com
gearuptofit.com
gearuptogrow.com
micegoneguide.com
mysticaldigits.com
plantastichaven.com
outdoormisting.com
openclaw-skillshub.com
EOF
    
    # 6. SEO cache data
    log "Backing up SEO data cache..."
    cp -r "$WORKSPACE/cache" "$TEMP_DIR/cache" 2>/dev/null || true
    
    # 7. Framework files
    log "Backing up framework files..."
    mkdir -p "$TEMP_DIR/framework"
    for f in performance-patterns.md quality-framework.md token-efficiency.md; do
        [ -f "$WORKSPACE/skills/$f" ] && cp "$WORKSPACE/skills/$f" "$TEMP_DIR/framework/"
    done
    
    # 8. Recovery script itself
    cp "$0" "$TEMP_DIR/disaster-recovery.sh"
    
    # 9. Create manifest
    cat > "$TEMP_DIR/MANIFEST.md" << EOF
# OpenClaw Disaster Recovery Backup
Created: $(date -Iseconds)
Hostname: $(hostname)
Workspace: $WORKSPACE

## Contents
- core/ — Core config files (AGENTS, SOUL, USER, MEMORY, etc.)
- skills/ — All $(ls "$WORKSPACE/skills" | wc -l) skills
- memory/ — Daily notes and entity memory
- ops/ — Scripts, macros, checklists, templates
- .secrets/ — Secrets template (restore guide)
- cache/ — SEO data cache (GSC, keyword research)
- framework/ — Performance, quality, token-efficiency docs

## Restore Command
./disaster-recovery.sh restore openclaw-disaster-recovery-*.tar.gz

## After Restore
1. Recreate .secrets/ files (see .secrets/RESTORE-TEMPLATE.md)
2. Install dependencies: pip install google-api-python-client google-auth requests
3. Verify: openclaw status
4. Test GSC: python3 skills/seo-intelligence/scripts/gsc-bing-intel.py --gsc --site https://example.com
EOF
    
    # Create archive
    log "Creating archive..."
    mkdir -p "$BACKUP_DIR"
    cd /tmp
    tar -czf "$BACKUP_DIR/$BACKUP_NAME.tar.gz" "$BACKUP_NAME"
    
    SIZE=$(du -sh "$BACKUP_DIR/$BACKUP_NAME.tar.gz" | cut -f1)
    log "✅ Backup complete: $BACKUP_DIR/$BACKUP_NAME.tar.gz ($SIZE)"
    
    # Also create a minimal git bundle for the repo
    if [ -d "$WORKSPACE/.git" ]; then
        log "Creating git bundle..."
        cd "$WORKSPACE"
        git bundle create "$BACKUP_DIR/$BACKUP_NAME.bundle" --all 2>/dev/null || warn "Git bundle failed (no git repo)"
    fi
    
    # Cleanup
    rm -rf "$TEMP_DIR"
    
    echo ""
    log "📦 BACKUP LOCATION: $BACKUP_DIR/$BACKUP_NAME.tar.gz"
    log "📋 Copy this file to a safe location (cloud storage, another server, USB drive)"
}

# ============================================================================
# FULL BACKUP (includes repos and larger files)
# ============================================================================
full_backup() {
    log "Starting FULL backup (including repos)..."
    
    TEMP_DIR="/tmp/$BACKUP_NAME-full"
    mkdir -p "$TEMP_DIR"
    
    # Everything from regular backup
    backup
    
    # Plus repos
    log "Backing up repos..."
    [ -d "$WORKSPACE/repos" ] && cp -r "$WORKSPACE/repos" "$TEMP_DIR/repos"
    
    # Plus distributions
    log "Backing up distributions..."
    [ -d "$WORKSPACE/dist" ] && cp -r "$WORKSPACE/dist" "$TEMP_DIR/dist"
    
    # Create full archive
    cd /tmp
    tar -czf "$BACKUP_DIR/$BACKUP_NAME-full.tar.gz" "$BACKUP_NAME-full"
    SIZE=$(du -sh "$BACKUP_DIR/$BACKUP_NAME-full.tar.gz" | cut -f1)
    log "✅ Full backup complete: $BACKUP_DIR/$BACKUP_NAME-full.tar.gz ($SIZE)"
    
    rm -rf "$TEMP_DIR"
}

# ============================================================================
# RESTORE
# ============================================================================
restore() {
    local BACKUP_FILE="$1"
    
    if [ -z "$BACKUP_FILE" ]; then
        error "Usage: $0 restore <backup-file.tar.gz>"
        exit 1
    fi
    
    if [ ! -f "$BACKUP_FILE" ]; then
        error "Backup file not found: $BACKUP_FILE"
        exit 1
    fi
    
    log "⚠️  RESTORING from: $BACKUP_FILE"
    warn "This will overwrite existing workspace files!"
    read -p "Continue? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        log "Aborted."
        exit 0
    fi
    
    # Extract to temp
    TEMP_DIR="/tmp/restore-$$"
    mkdir -p "$TEMP_DIR"
    tar -xzf "$BACKUP_FILE" -C "$TEMP_DIR"
    
    # Find the extracted directory
    EXTRACT_DIR=$(find "$TEMP_DIR" -maxdepth 1 -type d | grep -v "^$TEMP_DIR$" | head -1)
    
    log "Restoring from: $EXTRACT_DIR"
    
    # Restore core files
    log "Restoring core config..."
    [ -d "$EXTRACT_DIR/core" ] && cp -r "$EXTRACT_DIR/core/"* "$WORKSPACE/" 2>/dev/null || true
    
    # Restore skills
    log "Restoring skills..."
    [ -d "$EXTRACT_DIR/skills" ] && cp -r "$EXTRACT_DIR/skills/"* "$WORKSPACE/skills/" 2>/dev/null || true
    
    # Restore memory
    log "Restoring memory..."
    [ -d "$EXTRACT_DIR/memory" ] && cp -r "$EXTRACT_DIR/memory/"* "$WORKSPACE/memory/" 2>/dev/null || true
    
    # Restore ops
    log "Restoring ops..."
    [ -d "$EXTRACT_DIR/ops" ] && cp -r "$EXTRACT_DIR/ops/"* "$WORKSPACE/ops/" 2>/dev/null || true
    
    # Restore cache
    log "Restoring cache..."
    [ -d "$EXTRACT_DIR/cache" ] && cp -r "$EXTRACT_DIR/cache/"* "$WORKSPACE/cache/" 2>/dev/null || true
    
    # Restore secrets (template only)
    log "Restoring secrets structure..."
    [ -d "$EXTRACT_DIR/.secrets" ] && cp -r "$EXTRACT_DIR/.secrets/"* "$WORKSPACE/.secrets/" 2>/dev/null || true
    
    # Cleanup
    rm -rf "$TEMP_DIR"
    
    log "✅ RESTORE COMPLETE!"
    echo ""
    warn "NEXT STEPS:"
    echo "  1. Recreate .secrets/ files (see .secrets/RESTORE-TEMPLATE.md)"
    echo "  2. Install: pip install google-api-python-client google-auth requests"
    echo "  3. Verify: openclaw status"
    echo "  4. Test GSC: python3 skills/seo-intelligence/scripts/gsc-bing-intel.py --gsc --site https://example.com"
}

# ============================================================================
# GITHUB SYNC (push everything to repo)
# ============================================================================
github_sync() {
    log "Syncing to GitHub repo..."
    
    REPO_DIR="/tmp/openclaw-config-001"
    
    if [ ! -d "$REPO_DIR" ]; then
        log "Cloning repo..."
        git clone https://github.com/douphealth/openclaw-config-001.git "$REPO_DIR" 2>&1
    fi
    
    cd "$REPO_DIR"
    git pull --rebase origin main 2>&1 || true
    
    # Sync everything
    log "Syncing skills..."
    for skill_dir in "$WORKSPACE/skills"/*/; do
        skill=$(basename "$skill_dir")
        [ -f "$skill_dir/SKILL.md" ] || continue
        mkdir -p "skills-approved/$skill"
        cp "$skill_dir/SKILL.md" "skills-approved/$skill/"
        [ -d "$skill_dir/references" ] && cp -r "$skill_dir/references" "skills-approved/$skill/"
        [ -d "$skill_dir/scripts" ] && cp -r "$skill_dir/scripts" "skills-approved/$skill/"
    done
    
    # Sync core files
    log "Syncing core files..."
    cp "$WORKSPACE/MEMORY.md" memory/ 2>/dev/null || true
    cp "$WORKSPACE/AGENTS.md" core/ 2>/dev/null || true
    cp "$WORKSPACE/SOUL.md" core/ 2>/dev/null || true
    cp "$WORKSPACE/USER.md" core/ 2>/dev/null || true
    cp "$WORKSPACE/TOOLS.md" core/ 2>/dev/null || true
    cp "$WORKSPACE/HEARTBEAT.md" core/ 2>/dev/null || true
    
    # Sync scripts
    log "Syncing scripts..."
    mkdir -p scripts/self-improvement
    cp "$WORKSPACE/ops/self-improvement/"*.py scripts/self-improvement/ 2>/dev/null || true
    
    # Create recovery manifest
    cat > DISASTER-RECOVERY.md << 'DRMEOF'
# Disaster Recovery Guide

## Quick Restore (New Machine)

### 1. Install OpenClaw
```bash
npm install -g openclaw
openclaw configure
```

### 2. Clone This Repo
```bash
git clone https://github.com/douphealth/openclaw-config-001.git
cd openclaw-config-001
```

### 3. Restore Workspace
```bash
# Copy skills to workspace
cp -r skills-approved/* ~/.openclaw/workspace/skills/

# Copy core configs
cp core/AGENTS.md ~/.openclaw/workspace/
cp core/SOUL.md ~/.openclaw/workspace/
cp core/USER.md ~/.openclaw/workspace/
cp core/TOOLS.md ~/.openclaw/workspace/
cp core/HEARTBEAT.md ~/.openclaw/workspace/
cp memory/MEMORY.md ~/.openclaw/workspace/

# Copy scripts
mkdir -p ~/.openclaw/workspace/ops/self-improvement
cp scripts/self-improvement/*.py ~/.openclaw/workspace/ops/self-improvement/
```

### 4. Restore Secrets
Create these files in `~/.openclaw/workspace/.secrets/`:
- `gsc-service-account.json` — Google service account key
- `bing-api-key.txt` — Bing Webmaster Tools API key
- `seo-sites.json` — Site configuration
- `{domain}.access.env` — WordPress credentials per site

### 5. Install Dependencies
```bash
pip install google-api-python-client google-auth requests
```

### 6. Verify
```bash
openclaw status
python3 ~/.openclaw/workspace/skills/seo-intelligence/scripts/gsc-bing-intel.py --gsc --site https://example.com
```

## What's Included
- 47 enterprise-grade skills
- SEO intelligence system (GSC + Bing API)
- WordPress optimization skills
- Content enhancement system
- Keyword research pipeline
- Self-improvement infrastructure

## What's NOT Included (Add Manually)
- `.secrets/` credentials (API keys, passwords)
- `cache/` data (will regenerate on first run)
- `memory/daily/` old notes (only current preserved)
DRMEOF
    
    # Commit and push
    git add -A
    git commit -m "disaster-recovery: Full backup $(date +%Y-%m-%d)" 2>&1 || true
    
    log "Push to GitHub? (requires auth)"
    read -p "Push now? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git push origin main 2>&1 || error "Push failed — check auth"
    fi
    
    log "✅ GitHub sync complete"
}

# ============================================================================
# MAIN
# ============================================================================
case "${1:-}" in
    backup)
        backup
        ;;
    full-backup)
        full_backup
        ;;
    restore)
        restore "$2"
        ;;
    github-sync)
        github_sync
        ;;
    *)
        echo "Disaster Recovery — OpenClaw Workspace"
        echo ""
        echo "Usage:"
        echo "  $0 backup        — Backup skills, config, memory, ops"
        echo "  $0 full-backup   — Backup everything including repos"
        echo "  $0 restore FILE  — Restore from backup archive"
        echo "  $0 github-sync   — Push everything to GitHub repo"
        echo ""
        echo "For disaster recovery:"
        echo "  1. Keep a copy of this script + backup archive offsite"
        echo "  2. Also push to GitHub regularly (github-sync)"
        echo "  3. Store .secrets/ separately (password manager, encrypted)"
        ;;
esac
