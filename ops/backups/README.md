# Workspace Backups

## Critical backup script
Run:
```bash
bash /home/openclaw/.openclaw/workspace/ops/backups/create_workspace_critical_backup.sh
```

## Daily 23:30 cron example
Add this to the crontab on the VPS:
```cron
30 23 * * * /bin/bash /home/openclaw/.openclaw/workspace/ops/backups/create_workspace_critical_backup.sh >> /home/openclaw/.openclaw/workspace/ops/backups/system/backup-cron.log 2>&1
```

## What gets backed up
- AGENTS.md
- SOUL.md
- USER.md
- TOOLS.md
- IDENTITY.md
- MEMORY.md
- skills/
- memory/
- clawflows/
- openclaw.json

## Output location
`/home/openclaw/.openclaw/workspace/ops/backups/system/`
