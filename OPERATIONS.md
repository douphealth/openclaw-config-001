# OPERATIONS

## Daily
- Run `make health`
- Run `make validate`
- Confirm latest encrypted backup exists outside the VPS

## Weekly
- Run `make release`
- Review `MANIFEST.yaml`
- Review approved skills for overlap, drift, or redundancy

## Change policy
Every material change should update:
- `MANIFEST.yaml`
- relevant docs
- scripts if workflow changed

## Production rule
Only skills listed as `production: true` in `MANIFEST.yaml` should be considered active for routing and operations.
