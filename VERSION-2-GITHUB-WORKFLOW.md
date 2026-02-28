# OpenClaw Version 2 - Definitive GitHub Workflow Guide

This guide outlines the EXACT workflow for managing your consolidated OpenClaw configuration using GitHub.

## 🚀 Phase 1: Local Initialization (Do This First)

Establish your local workspace as the canonical source of truth.

```bash
cd ~
mkdir openclaw-config && cd openclaw-config
git init
git branch -M main

# Set up .gitignore with credential protection
cat > .gitignore << 'EOF'
.secrets/
*.env
**/vault/
**/.env.*
core/STATUS.md
world-model/**/*.json
__pycache__/
*.pyc
.venv/
node_modules/
.DS_Store
EOF

git add .gitignore
git commit -m "init: gitignore with credential protection"
```

## 📦 Phase 2: Importing Current State (Pre-Consolidation Snapshot)

Capture your existing 24-skill setup before applying the v2 architecture.

```bash
# Core files
mkdir -p core/
cp /path/to/openclaw/*.md core/

# Skills
cp -r /path/to/openclaw/skills/ skills/

# Memory & Reports
mkdir -p memory/ reports/
cp /path/to/openclaw/memory/*.md memory/ 2>/dev/null || true
cp /path/to/openclaw/reports/* reports/ 2>/dev/null || true

git add -A
git commit -m "archive: complete pre-consolidation snapshot — 24 skills, 7 core files"
git tag v1.0-pre-consolidation
```

## 🔄 Phase 3: Applying Version 2 Consolidation

Apply the consolidation in atomic commits for maximum reliability.

### Step 1: Core File Optimization
Replace `core/` files with the optimized v2 versions (IDENTITY, AGENTS, MEMORY, USER, TOOLS, HEARTBEAT, STATUS).
```bash
git add -A
git commit -m "core: consolidate SOUL→IDENTITY, deduplicate files (59% token reduction)"
```

### Step 2: Skill Consolidation (24 → 9)
Create new structures and migrate functional scripts/references.
```bash
# Example for Technical Health
mkdir -p skills/wordpress-technical-health/{references,scripts}
# ... (repeat for all 9 skills)

git add -A
git commit -m "skills: create 9 consolidated skills with migrated scripts + references"
```

### Step 3: Cleanup
Remove the 15 eliminated skills and dead-weight files.
```bash
# rm -rf skills/old-skill-name
git add -A
git commit -m "cleanup: remove 15 eliminated skills + dead-weight files"
git tag v2.0-consolidated
```

## 🤖 Automated Sync Skill (`skills/git-sync/SKILL.md`)

Incorporate this skill into your consolidated setup for autonomous versioning.

```markdown
---
name: git-sync
description: Automatically commit and push OpenClaw config changes to GitHub.
---

# Git Sync Workflow
1. cd ~/openclaw-config
2. Review diff for credential leaks (grep for API keys).
3. Stage changes: `git add -A`
4. Commit: `git commit -m "auto: {YYYY-MM-DD} — {summary}"`
5. Push: `git push origin main`
```

## 🔐 Security & Safety Protocols

- **Private Repo Only**: `gh repo edit --visibility private`
- **Pre-Commit Hook**: Block commits containing `API_KEY`, `SECRET_KEY`, etc.
- **No Force Push**: Protected `main` branch.
- **Sanitization**: Remove PII before any community sharing.

## 📊 Daily Workflow Summary

| Task | Command |
|------|---------|
| Check Changes | `git status` |
| Review Diffs | `git diff core/ skills/` |
| Save Session | `git add -A && git commit -m "session: {desc}" && git push` |
| Rollback File | `git checkout -- <file>` |
| Full Revert | `git checkout v1.0-pre-consolidation -- .` |

---
**Status**: Ready for Implementation
**Version**: 2.0.0 (Consolidated)
**Owner**: Alexios Papaioannou
