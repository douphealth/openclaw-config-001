---
name: git-sync
description: Automatically commit and push OpenClaw config changes to GitHub.
  Use after significant sessions, core file modifications, or on schedule.
---

# Git Sync

## When to Run
- After any core file modification (IDENTITY, AGENTS, MEMORY, USER, TOOLS, HEARTBEAT)
- After any skill file modification
- After significant execution sessions (>5 URLs changed)
- Daily at 23:00 Athens time (end of day backup)

## Workflow
1. `cd ~/openclaw-config`
2. `git status` — check for changes.
3. If no changes: log "git-sync: no changes" → exit.
4. `git diff --stat` — summarize what changed.
5. Review diff for credential leaks (grep for API keys, passwords, tokens).
6. If credentials detected: STOP. Alert Alex immediately. Do NOT commit.
7. Stage changes: `git add -A`
8. Commit: `git commit -m "auto: {YYYY-MM-DD} — {summary of changes}"`
9. Push: `git push origin main`
10. If push fails: log error, retry once after 60s, then flag for Alex.

## Safety Rules
- NEVER commit files matching .gitignore patterns.
- NEVER force-push (`git push --force` is forbidden).
- NEVER rewrite history (`git rebase`, `git reset --hard` on pushed commits).
- NEVER commit files containing API keys, passwords, or tokens.
- Always use descriptive commit messages (not just "auto update").
