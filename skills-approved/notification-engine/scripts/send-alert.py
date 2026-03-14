#!/usr/bin/env python3
"""send-alert.py — Send notifications via Telegram or Brevo email.
Usage:
  python3 send-alert.py --severity warn --title "Alert" --body "Details" --channel telegram
  python3 send-alert.py --severity critical --title "Down" --body "503" --channel telegram --channel email

Requires env vars (from .secrets/notification.env or shell):
  TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
  BREVO_API_KEY, BREVO_ALERT_EMAIL
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone

SEVERITY_ICONS = {"info": "ℹ️", "warn": "⚠️", "critical": "🚨"}

def send_telegram(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = json.dumps({"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}).encode()
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status == 200, resp.read().decode()[:200]
    except Exception as e:
        return False, str(e)

def send_brevo_email(api_key, to_email, subject, body):
    url = "https://api.brevo.com/v3/smtp/email"
    payload = json.dumps({
        "sender": {"name": "Alert System", "email": "alerts@openclaw.local"},
        "to": [{"email": to_email}],
        "subject": subject,
        "htmlContent": f"<pre>{body}</pre>"
    }).encode()
    req = urllib.request.Request(url, data=payload, headers={
        "Content-Type": "application/json",
        "api-key": api_key
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status in (200, 201), resp.read().decode()[:200]
    except Exception as e:
        return False, str(e)

def log_alert(severity, title, channels, results):
    os.makedirs("ops/alerts", exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    time_str = datetime.now(timezone.utc).strftime("%H:%M:%S")
    delivered = ",".join(f"{ch}={'ok' if ok else 'FAIL'}" for ch, ok in results.items())
    line = f"[{time_str}] {severity.upper():8s} | {title} | channels: {','.join(channels)} | {delivered}\n"
    with open(f"ops/alerts/{ts}.log", "a") as f:
        f.write(line)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--severity", choices=["info", "warn", "critical"], required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--body", required=True)
    parser.add_argument("--channel", action="append", default=[], choices=["telegram", "email", "discord", "webhook"])
    args = parser.parse_args()

    icon = SEVERITY_ICONS[args.severity]
    message = f"{icon} *{args.severity.upper()}*\n*{args.title}*\n\n{args.body}"
    print(f"Sending: {args.title} [{args.severity}] to {args.channel}")

    results = {}

    for ch in args.channel:
        if ch == "telegram":
            token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
            chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")
            if not token or not chat_id:
                results["telegram"] = False
                print("  ❌ telegram: missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID")
                continue
            ok, detail = send_telegram(token, chat_id, message)
            results["telegram"] = ok
            print(f"  {'✅' if ok else '❌'} telegram: {detail[:100]}")

        elif ch == "email":
            key = os.environ.get("BREVO_API_KEY", "")
            email = os.environ.get("BREVO_ALERT_EMAIL", "")
            if not key or not email:
                results["email"] = False
                print("  ❌ email: missing BREVO_API_KEY or BREVO_ALERT_EMAIL")
                continue
            ok, detail = send_brevo_email(key, email, f"{icon} {args.title}", message)
            results["email"] = ok
            print(f"  {'✅' if ok else '❌'} email: {detail[:100]}")

        elif ch == "discord":
            webhook = os.environ.get("DISCORD_WEBHOOK_URL", "")
            if not webhook:
                results["discord"] = False
                print("  ❌ discord: missing DISCORD_WEBHOOK_URL")
                continue
            payload = json.dumps({"content": message.replace("*", "**")}).encode()
            req = urllib.request.Request(webhook, data=payload, headers={"Content-Type": "application/json"})
            try:
                with urllib.request.urlopen(req, timeout=15) as resp:
                    ok = resp.status in (200, 204)
                    results["discord"] = ok
                    print(f"  {'✅' if ok else '❌'} discord: HTTP {resp.status}")
            except Exception as e:
                results["discord"] = False
                print(f"  ❌ discord: {e}")

        elif ch == "webhook":
            wh_url = os.environ.get("ALERT_WEBHOOK_URL", "")
            if not wh_url:
                results["webhook"] = False
                print("  ❌ webhook: missing ALERT_WEBHOOK_URL")
                continue
            payload = json.dumps({"severity": args.severity, "title": args.title, "body": args.body}).encode()
            req = urllib.request.Request(wh_url, data=payload, headers={"Content-Type": "application/json"})
            try:
                with urllib.request.urlopen(req, timeout=15) as resp:
                    ok = resp.status < 400
                    results["webhook"] = ok
                    print(f"  {'✅' if ok else '❌'} webhook: HTTP {resp.status}")
            except Exception as e:
                results["webhook"] = False
                print(f"  ❌ webhook: {e}")

    log_alert(args.severity, args.title, args.channel, results)

    all_ok = all(results.values())
    print(f"\n{'✅ All delivered' if all_ok else '⚠️ Some channels failed'}")
    sys.exit(0 if all_ok else 1)

if __name__ == "__main__":
    main()
