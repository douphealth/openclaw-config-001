# Rollback

1. Identify last known good release in `releases/`.
2. Verify checksum.
3. Restore repo bundle.
4. Restore secrets from vault.
5. Run `make validate`.
6. Run `make health`.
