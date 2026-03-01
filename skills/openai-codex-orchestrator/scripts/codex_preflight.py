#!/usr/bin/env python3
import argparse
import json
import subprocess

ROOT = '/home/openclaw/.openclaw/workspace/skills/openai-codex-orchestrator/scripts'


def run(cmd):
    cp = subprocess.run(cmd, capture_output=True, text=True)
    raw = cp.stdout.strip() or cp.stderr.strip()
    try:
        data = json.loads(raw)
    except Exception:
        data = {'raw': raw}
    return cp.returncode, data


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Single preflight gate for Codex API usage')
    ap.add_argument('--est-cost', type=float, default=0.02)
    ap.add_argument('--est-tokens', type=int, default=1500)
    ap.add_argument('--skip-network-auth', action='store_true')
    a = ap.parse_args()

    auth_cmd = ['python3', f'{ROOT}/codex_auth_verify.py']
    if a.skip_network_auth:
        auth_cmd.append('--skip-network')

    c1, auth = run(auth_cmd)
    c2, budget = run(['python3', f'{ROOT}/codex_budget_guard.py', '--est-cost', str(a.est_cost), '--est-tokens', str(a.est_tokens)])
    c3, rate = run(['python3', f'{ROOT}/codex_rate_limiter.py', 'precheck', '--estimated-tokens', str(a.est_tokens)])
    c4, gateway = run(['python3', f'{ROOT}/codex_gateway_enforcer.py'])

    allow = (
        auth.get('status') in ('authenticated', 'refresh_needed') and
        budget.get('allow') is True and
        rate.get('allow') is True and
        gateway.get('pass') is True
    )

    out = {
        'allow': allow,
        'decision': 'proceed' if allow else ('fallback_or_defer'),
        'auth': auth,
        'budget': budget,
        'rate': rate,
        'gateway': gateway,
    }
    print(json.dumps(out, indent=2))
    raise SystemExit(0 if allow else 1)
