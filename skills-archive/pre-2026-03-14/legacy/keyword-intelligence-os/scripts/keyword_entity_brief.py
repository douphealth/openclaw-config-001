#!/usr/bin/env python3
"""
Build deterministic keyword/entity briefs from CSV input.

Input CSV required columns:
- url
- keyword
- intent
- funnel
- entities   (pipe-separated)
- secondary  (pipe-separated, optional)
- questions  (pipe-separated, optional)

Usage:
  python3 keyword_entity_brief.py --in input.csv --out brief.md
"""

import argparse
import csv
from collections import defaultdict


def norm_list(v: str):
    if not v:
        return []
    return [x.strip() for x in v.split("|") if x.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--out", dest="out", required=True)
    args = ap.parse_args()

    rows = []
    with open(args.inp, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        required = {"url", "keyword", "intent", "funnel", "entities"}
        missing = required - set(r.fieldnames or [])
        if missing:
            raise SystemExit(f"Missing required columns: {', '.join(sorted(missing))}")
        for row in r:
            rows.append({
                "url": row.get("url", "").strip(),
                "keyword": row.get("keyword", "").strip(),
                "intent": row.get("intent", "").strip(),
                "funnel": row.get("funnel", "").strip(),
                "entities": norm_list(row.get("entities", "")),
                "secondary": norm_list(row.get("secondary", "")),
                "questions": norm_list(row.get("questions", "")),
            })

    by_intent = defaultdict(list)
    for row in rows:
        by_intent[row["intent"]].append(row)

    lines = []
    lines.append("# Keyword & Entity Brief\n")
    lines.append(f"Total URLs: {len(rows)}\n")

    for intent in sorted(by_intent.keys()):
        lines.append(f"\n## Intent: {intent}\n")
        for i, row in enumerate(by_intent[intent], 1):
            lines.append(f"### {i}. {row['url']}")
            lines.append(f"- Primary: {row['keyword']}")
            lines.append(f"- Funnel: {row['funnel']}")
            lines.append(f"- Entities: {', '.join(row['entities']) if row['entities'] else '(none)'}")
            lines.append(f"- Secondary: {', '.join(row['secondary']) if row['secondary'] else '(none)'}")
            lines.append(f"- Questions: {', '.join(row['questions']) if row['questions'] else '(none)'}")
            lines.append("")

    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")


if __name__ == "__main__":
    main()
