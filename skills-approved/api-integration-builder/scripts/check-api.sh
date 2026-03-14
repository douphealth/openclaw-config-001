#!/usr/bin/env bash
# check-api.sh — Test API endpoint connectivity, auth, and rate limits
# Usage: ./check-api.sh <URL> [METHOD] [AUTH_HEADER]
# Examples:
#   ./check-api.sh https://api.example.com/v1/status
#   ./check-api.sh https://api.example.com/v1/users GET "Bearer sk-abc123"
#   ./check-api.sh https://api.example.com/v1/data POST "Bearer sk-abc123"

set -euo pipefail

URL="${1:?Usage: check-api.sh <URL> [METHOD] [AUTH_HEADER]}"
METHOD="${2:-GET}"
AUTH="${3:-}"

TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT

CURL_ARGS=(-s -w "\n%{http_code}\n%{time_total}" -o "$TMPFILE" -X "$METHOD")
[[ -n "$AUTH" ]] && CURL_ARGS+=(-H "Authorization: $AUTH")
CURL_ARGS+=(-H "Accept: application/json" --max-time 30)

echo "=== API Check: $METHOD $URL ==="
echo ""

RESPONSE=$(curl "${CURL_ARGS[@]}" "$URL" 2>&1 || echo "CURL_ERROR")

HTTP_CODE=$(echo "$RESPONSE" | tail -2 | head -1)
TIME=$(echo "$RESPONSE" | tail -1)

if [[ "$RESPONSE" == "CURL_ERROR" ]]; then
    echo "❌ Connection failed (network error or timeout)"
    exit 1
fi

echo "Status: $HTTP_CODE"
echo "Time:   ${TIME}s"
echo ""

# Show rate limit headers if present
echo "--- Rate Limit Headers ---"
curl -sI -X "$METHOD" --max-time 10 \
    ${AUTH:+-H "Authorization: $AUTH"} \
    "$URL" 2>/dev/null | grep -iE 'x-rate|retry-after|ratelimit' || echo "(none found)"
echo ""

# Show response body (truncated)
echo "--- Response Body (first 500 chars) ---"
head -c 500 "$TMPFILE"
echo ""
echo ""

# Interpret result
case "$HTTP_CODE" in
    2*) echo "✅ OK" ;;
    401) echo "❌ Unauthorized — check API key or token" ;;
    403) echo "❌ Forbidden — valid auth but insufficient permissions" ;;
    404) echo "❌ Not Found — check endpoint URL" ;;
    429) echo "⚠️  Rate limited — check Retry-After header above" ;;
    5*) echo "❌ Server error ($HTTP_CODE) — retry later" ;;
    *)  echo "⚠️  Unexpected status code: $HTTP_CODE" ;;
esac
