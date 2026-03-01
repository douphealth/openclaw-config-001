# One-Click Recovery (OpenClaw Config)

```bash
# 1) Clone
cd ~/.openclaw/workspace
git clone https://github.com/douphealth/openclaw-config.git recovered-openclaw-config

# 2) Use enterprise branch
git -C recovered-openclaw-config checkout enterprise-curated

# 3) Sync skills + core scripts into active workspace
rsync -a recovered-openclaw-config/skills/ ~/.openclaw/workspace/skills/
rsync -a recovered-openclaw-config/core/ ~/.openclaw/workspace/scripts/

# 4) Verify key controls
python3 ~/.openclaw/workspace/scripts/autonomy_control.py status
python3 ~/.openclaw/workspace/scripts/trend_blog_automation_control.py status
```

## Notes
- Secrets are intentionally not stored in git; restore `.secrets/*.env` separately.
- Recommended branch for production restore: `enterprise-curated`.
