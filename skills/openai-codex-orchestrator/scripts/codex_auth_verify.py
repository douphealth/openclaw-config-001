#!/usr/bin/env python3
import argparse, json, os, time
from pathlib import Path
import requests

ROOT = Path('/home/openclaw/.openclaw/workspace')
ENV = ROOT / '.secrets/openai-codex.env'
STATE = ROOT / 'state/codex_auth_state.json'
MODELS_URL = 'https://api.openai.com/v1/models'


def load_env(path):
    d = {}
    if not path.exists():
        return d
    for l in path.read_text().splitlines():
        if '=' in l and not l.strip().startswith('#'):
            k, v = l.split('=', 1)
            d[k.strip()] = v.strip().strip('"').strip("'")
    return d


def verify_with_api_key(env):
    key = env.get('OPENAI_API_KEY')
    if not key:
        return {'status': 'auth_failed', 'reason': 'missing_api_key'}
    h = {'Authorization': f'Bearer {key}'}
    if env.get('OPENAI_ORG_ID'):
        h['OpenAI-Organization'] = env['OPENAI_ORG_ID']
    if env.get('OPENAI_PROJECT_ID'):
        h['OpenAI-Project'] = env['OPENAI_PROJECT_ID']
    r = requests.get(MODELS_URL, headers=h, timeout=20)
    out = {
        'status': 'authenticated' if r.status_code == 200 else 'auth_failed',
        'http_status': r.status_code,
        'rate_limit_remaining_requests': r.headers.get('x-ratelimit-remaining-requests'),
        'rate_limit_remaining_tokens': r.headers.get('x-ratelimit-remaining-tokens'),
    }
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--skip-network', action='store_true')
    a = ap.parse_args()

    env = load_env(ENV)
    now = int(time.time())
    state = {
        'checked_at': now,
        'oauth_config_present': bool(env.get('OAUTH_TOKEN_ENDPOINT')),
    }

    if a.skip_network:
        state['status'] = 'refresh_needed' if env.get('OAUTH_TOKEN_ENDPOINT') else 'authenticated'
    else:
        state.update(verify_with_api_key(env))

    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2))
    print(json.dumps(state, indent=2))
