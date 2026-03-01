# Cadence Proof + KPI Hygiene

## UI-independent cadence proof
Run:
- `python3 /home/openclaw/.openclaw/workspace/scripts/amfs_timing_proof.py`

Purpose:
- verify welcome-step timing drift against expected schedule (0h, 24h, 72h, 168h, 336h)
- reduce dependency on manual ESP UI screenshots

## Test-contact KPI hygiene
Run:
- `python3 /home/openclaw/.openclaw/workspace/scripts/amfs_test_contact_suppression.py`

Purpose:
- remove test-domain/test-alias contacts from active sequence KPI state
- keep open/CTR/CTOR interpretation clean

## Release rule
Do not claim cadence stability or KPI trend quality unless:
1) timing proof report exists and is pass/warn-explained
2) test-contact suppression report exists for current window
