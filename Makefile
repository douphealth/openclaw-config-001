SHELL := /usr/bin/env bash

validate:
bash scripts/validate.sh

backup:
bash scripts/backup.sh

restore-dry-run:
bash scripts/restore.sh --dry-run

health:
bash scripts/healthcheck.sh

release:
bash scripts/release.sh
