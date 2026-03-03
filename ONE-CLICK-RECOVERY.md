# One-Click Recovery

## Steps

1. Clone:
   cd ~/.openclaw/workspace
   git clone https://github.com/douphealth/openclaw-config.git recovered-config

2. Use enterprise branch:
   cd recovered-config && git checkout enterprise-curated

3. Sync to active workspace:
   rsync -a skills/ ~/.openclaw/workspace/skills/
   rsync -a core/ ~/.openclaw/workspace/scripts/

4. Verify:
   python3 ~/.openclaw/workspace/openclaw-config/core/mode_control.py all status
   openclaw doctor --non-interactive

## Notes
- Secrets are NOT in git. Restore .secrets/*.env manually.
- Recommended branch: enterprise-curated
- After recovery: python3 ~/.openclaw/workspace/scripts/build_skill_index.py
