#!/usr/bin/env python3
"""Merge GSC and Bing summaries into one normalized search-visibility pack summary.

Example:
  python build_search_visibility_pack.py --site https://example.com/ --range-label last_28_days --outdir C:/Users/User/.openclaw/workspace/ops/search-data/example-com
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def slugify_site(site: str) -> str:
    site = re.sub(r"^https?://", "", site).strip("/")
    return re.sub(r"[^a-zA-Z0-9.-]+", "-", site).replace(".", "-").lower()


def load_json(path: Path):
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", required=True)
    parser.add_argument("--range-label", default="last_28_days")
    parser.add_argument("--outdir", default="")
    args = parser.parse_args()

    outdir = Path(args.outdir or Path.cwd() / "ops" / "search-data" / slugify_site(args.site))
    gsc = load_json(outdir / "gsc" / "summary.json").get("gsc", {})
    bing = load_json(outdir / "bing" / "summary.json").get("bing", {})

    summary = {
        "site": args.site,
        "range": args.range_label,
        "gsc": {
            "total_clicks": gsc.get("total_clicks", 0),
            "total_impressions": gsc.get("total_impressions", 0),
            "avg_ctr": gsc.get("avg_ctr", 0),
            "avg_position": gsc.get("avg_position", 0),
            "top_pages_by_clicks": gsc.get("top_pages_by_clicks", []),
            "top_queries_by_impressions": gsc.get("top_queries_by_impressions", []),
            "low_ctr_high_impression_pages": gsc.get("low_ctr_high_impression_pages", []),
            "page2_queries": gsc.get("page2_queries", []),
        },
        "bing": {
            "total_clicks": bing.get("total_clicks", 0),
            "total_impressions": bing.get("total_impressions", 0),
            "top_pages_by_clicks": bing.get("top_pages_by_clicks", []),
            "top_queries_by_impressions": bing.get("top_queries_by_impressions", []),
            "indexation_signals": bing.get("indexation_signals", []),
            "crawl_issues": bing.get("crawl_issues", []),
        },
    }
    (outdir / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote merged summary to {outdir / 'summary.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
