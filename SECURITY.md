# SECURITY

## Hard rules
- Never commit secrets.
- Never store live `.env` files in Git.
- Keep OpenClaw on a dedicated VPS or isolated runtime.
- Use SSH keys only.
- Limit exposed ports.
- Review every external skill before adoption.

## Repo security controls
- secret-pattern validation in `scripts/validate.sh`
- release checksums in `scripts/release.sh`
- backup packaging isolated from Git history

## Runtime security
- keep `~/.openclaw` permissions tight
- audit exposed channels regularly
- run `openclaw doctor` after changes
