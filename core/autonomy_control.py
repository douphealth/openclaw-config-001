#!/usr/bin/env python3
import argparse
import subprocess

SCRIPTS = [
    ("CEO", "/home/openclaw/.openclaw/workspace/scripts/ceo_mode_control.py"),
    ("EMAIL", "/home/openclaw/.openclaw/workspace/scripts/email_autonomy_control.py"),
    ("MASTER", "/home/openclaw/.openclaw/workspace/scripts/master_orchestrator_control.py"),
    ("TREND_BLOG", "/home/openclaw/.openclaw/workspace/scripts/trend_blog_automation_control.py"),
]


def run(script: str, mode: str):
    cp = subprocess.run(["python3", script, mode], capture_output=True, text=True)
    return cp.returncode, cp.stdout.strip() or cp.stderr.strip()


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Global autonomy control for CEO + Email + Master modes')
    ap.add_argument('mode', choices=['pause', 'resume', 'status'])
    args = ap.parse_args()

    overall_ok = True
    for label, script in SCRIPTS:
        code, out = run(script, args.mode)
        if code != 0:
            overall_ok = False
        print(f"[{label}] code={code}")
        print(out)

    if not overall_ok:
        raise SystemExit(1)
