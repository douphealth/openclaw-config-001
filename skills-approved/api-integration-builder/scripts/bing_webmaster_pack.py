#!/usr/bin/env python3
"""Build a Bing Webmaster search-visibility pack.

Two modes:
1) api    -> call Bing Webmaster JSON endpoints and save raw results (+ basic normalized outputs when possible)
2) import -> normalize exported CSV/JSON files from Bing Webmaster Tools into the shared pack structure

Examples:
  python bing_webmaster_pack.py api --site https://example.com/ --method GetRankAndTrafficStats --outdir C:/.../ops/search-data/example-com
  python bing_webmaster_pack.py import --site https://example.com/ --queries-file queries.csv --pages-file pages.csv --outdir C:/.../ops/search-data/example-com
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List
from urllib.parse import urlencode
from urllib.request import urlopen

BASE = "https://ssl.bing.com/webmaster/api.svc/json"


def slugify_site(site: str) -> str:
    site = re.sub(r"^https?://", "", site).strip("/")
    return re.sub(r"[^a-zA-Z0-9.-]+", "-", site).replace(".", "-").lower()


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_json(path: Path, data) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def write_csv(path: Path, rows: List[Dict]) -> None:
    ensure_dir(path.parent)
    fieldnames = [
        "source", "site", "date_start", "date_end", "page", "query", "country", "device",
        "clicks", "impressions", "ctr", "position", "notes",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def api_call(method: str, apikey: str, params: Dict[str, str]) -> Dict:
    query = urlencode({"apikey": apikey, **params})
    url = f"{BASE}/{method}?{query}"
    with urlopen(url) as resp:
        return json.loads(resp.read().decode("utf-8"))


def normalize_import_rows(source: str, site: str, date_start: str, date_end: str, rows: List[Dict], kind: str) -> List[Dict]:
    normalized = []
    for row in rows:
        lower = {str(k).strip().lower(): v for k, v in row.items()}
        page = lower.get("page") or lower.get("url") or lower.get("page url") or lower.get("top page") or ""
        query = lower.get("query") or lower.get("keyword") or lower.get("search query") or ""
        clicks = lower.get("clicks") or lower.get("click") or 0
        impressions = lower.get("impressions") or lower.get("impression") or 0
        ctr = lower.get("ctr") or lower.get("click through rate") or 0
        position = lower.get("position") or lower.get("avg position") or lower.get("average position") or 0
        normalized.append({
            "source": source,
            "site": site,
            "date_start": date_start,
            "date_end": date_end,
            "page": page if kind != "queries" else "",
            "query": query if kind != "pages" else "",
            "country": lower.get("country", ""),
            "device": lower.get("device", ""),
            "clicks": clicks,
            "impressions": impressions,
            "ctr": ctr,
            "position": position,
            "notes": "imported from Bing Webmaster export",
        })
    return normalized


def load_table(path: Path) -> List[Dict]:
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            for key in ("rows", "data", "items", "result"):
                if isinstance(data.get(key), list):
                    return data[key]
            return [data]
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def summarize(rows: List[Dict]) -> Dict:
    total_clicks = sum(float(r.get("clicks", 0) or 0) for r in rows)
    total_impressions = sum(float(r.get("impressions", 0) or 0) for r in rows)
    top_pages_by_clicks = sorted(rows, key=lambda r: float(r.get("clicks", 0) or 0), reverse=True)[:20]
    top_queries_by_impressions = sorted(rows, key=lambda r: float(r.get("impressions", 0) or 0), reverse=True)[:20]
    return {
        "total_clicks": total_clicks,
        "total_impressions": total_impressions,
        "top_pages_by_clicks": top_pages_by_clicks,
        "top_queries_by_impressions": top_queries_by_impressions,
    }


def run_api_mode(args) -> int:
    if not args.apikey:
        print("Missing --apikey or BING_WEBMASTER_API_KEY", file=sys.stderr)
        return 2
    outdir = Path(args.outdir or Path.cwd() / "ops" / "search-data" / slugify_site(args.site))
    bing_dir = outdir / "bing"
    raw_dir = bing_dir / "raw"
    ensure_dir(raw_dir)

    params = {"siteUrl": args.site}
    if args.params_json:
        params.update(json.loads(args.params_json))
    data = api_call(args.method, args.apikey, params)
    write_json(raw_dir / f"{args.method}.json", data)

    summary = {
        "site": args.site,
        "range": {"start": args.start_date, "end": args.end_date},
        "bing": {
            "method": args.method,
            "note": "Raw Bing API response captured. Normalize further when method-specific schemas are confirmed.",
        },
    }
    write_json(bing_dir / "summary.json", summary)
    print(f"Wrote raw Bing API pack to {bing_dir}")
    return 0


def run_import_mode(args) -> int:
    outdir = Path(args.outdir or Path.cwd() / "ops" / "search-data" / slugify_site(args.site))
    bing_dir = outdir / "bing"
    ensure_dir(bing_dir)

    all_rows: List[Dict] = []
    if args.queries_file:
        qrows = normalize_import_rows("bing", args.site, args.start_date, args.end_date, load_table(Path(args.queries_file)), "queries")
        write_csv(bing_dir / "bing-queries.csv", qrows)
        all_rows.extend(qrows)
    if args.pages_file:
        prows = normalize_import_rows("bing", args.site, args.start_date, args.end_date, load_table(Path(args.pages_file)), "pages")
        write_csv(bing_dir / "bing-pages.csv", prows)
        all_rows.extend(prows)
    if args.page_query_file:
        pqrows = normalize_import_rows("bing", args.site, args.start_date, args.end_date, load_table(Path(args.page_query_file)), "page_query")
        write_csv(bing_dir / "bing-page-query.csv", pqrows)
        all_rows.extend(pqrows)
    if args.sitemaps_file:
        write_json(bing_dir / "sitemaps.json", load_table(Path(args.sitemaps_file)))

    summary = {
        "site": args.site,
        "range": {"start": args.start_date, "end": args.end_date},
        "bing": summarize(all_rows),
    }
    write_json(bing_dir / "summary.json", summary)
    print(f"Wrote normalized Bing import pack to {bing_dir}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="mode", required=True)

    api = sub.add_parser("api")
    api.add_argument("--site", required=True)
    api.add_argument("--method", required=True, help="e.g. GetRankAndTrafficStats, GetQueryStats")
    api.add_argument("--apikey", default=os.getenv("BING_WEBMASTER_API_KEY", ""))
    api.add_argument("--params-json", default="{}", help='Extra params JSON, e.g. {"siteUrl":"https://example.com/"}')
    api.add_argument("--start-date", default="")
    api.add_argument("--end-date", default="")
    api.add_argument("--outdir", default="")

    imp = sub.add_parser("import")
    imp.add_argument("--site", required=True)
    imp.add_argument("--queries-file", default="")
    imp.add_argument("--pages-file", default="")
    imp.add_argument("--page-query-file", default="")
    imp.add_argument("--sitemaps-file", default="")
    imp.add_argument("--start-date", required=True)
    imp.add_argument("--end-date", required=True)
    imp.add_argument("--outdir", default="")

    args = parser.parse_args()
    if args.mode == "api":
        return run_api_mode(args)
    return run_import_mode(args)


if __name__ == "__main__":
    raise SystemExit(main())
