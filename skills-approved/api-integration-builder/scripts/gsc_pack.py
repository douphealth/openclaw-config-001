#!/usr/bin/env python3
"""Build a Google Search Console search-visibility pack.

Outputs normalized CSV/JSON files under ops/search-data/<site-slug>/gsc/.

Requirements:
  pip install google-api-python-client google-auth google-auth-httplib2 google-auth-oauthlib

Auth:
  - service account JSON via --service-account or GSC_SERVICE_ACCOUNT_JSON
  - the service account must have access to the target Search Console property

Example:
  python gsc_pack.py --site https://example.com/ --start-date 2026-02-18 --end-date 2026-03-17 --outdir C:/Users/User/.openclaw/workspace/ops/search-data/example-com
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, Iterable, List


def slugify_site(site: str) -> str:
    site = site.replace("sc-domain:", "")
    site = re.sub(r"^https?://", "", site).strip("/")
    return re.sub(r"[^a-zA-Z0-9.-]+", "-", site).replace(".", "-").lower()


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def import_google_libs():
    try:
        from google.oauth2 import service_account  # type: ignore
        from googleapiclient.discovery import build  # type: ignore
        return service_account, build
    except Exception as exc:  # pragma: no cover
        print(
            "Missing Google API dependencies. Install with:\n"
            "  pip install google-api-python-client google-auth google-auth-httplib2 google-auth-oauthlib\n"
            f"Original error: {exc}",
            file=sys.stderr,
        )
        sys.exit(2)


def get_service(service_account_path: str):
    service_account, build = import_google_libs()
    scopes = ["https://www.googleapis.com/auth/webmasters.readonly"]
    creds = service_account.Credentials.from_service_account_file(service_account_path, scopes=scopes)
    return build("searchconsole", "v1", credentials=creds, cache_discovery=False)


def fetch_rows(service, site: str, body: Dict) -> List[Dict]:
    rows: List[Dict] = []
    start_row = 0
    row_limit = body.get("rowLimit", 25000)
    while True:
        request_body = dict(body)
        request_body["startRow"] = start_row
        request_body["rowLimit"] = row_limit
        resp = service.searchanalytics().query(siteUrl=site, body=request_body).execute()
        batch = resp.get("rows", [])
        if not batch:
            break
        rows.extend(batch)
        if len(batch) < row_limit:
            break
        start_row += row_limit
    return rows


def normalize_rows(source: str, site: str, start_date: str, end_date: str, rows: Iterable[Dict], dimensions: List[str]) -> List[Dict]:
    normalized = []
    for row in rows:
        keys = row.get("keys", [])
        data = {
            "source": source,
            "site": site,
            "date_start": start_date,
            "date_end": end_date,
            "page": "",
            "query": "",
            "country": "",
            "device": "",
            "clicks": row.get("clicks", 0),
            "impressions": row.get("impressions", 0),
            "ctr": row.get("ctr", 0),
            "position": row.get("position", 0),
            "notes": "",
        }
        for idx, dim in enumerate(dimensions):
            if idx < len(keys):
                data[dim] = keys[idx]
        normalized.append(data)
    return normalized


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


def write_json(path: Path, data) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def summarize(page_rows: List[Dict], query_rows: List[Dict]) -> Dict:
    total_clicks = sum(float(r.get("clicks", 0) or 0) for r in page_rows)
    total_impressions = sum(float(r.get("impressions", 0) or 0) for r in page_rows)
    avg_ctr = (total_clicks / total_impressions) if total_impressions else 0.0
    weighted_position_num = sum((float(r.get("position", 0) or 0) * float(r.get("impressions", 0) or 0)) for r in page_rows)
    avg_position = (weighted_position_num / total_impressions) if total_impressions else 0.0

    top_pages_by_clicks = sorted(page_rows, key=lambda r: float(r.get("clicks", 0) or 0), reverse=True)[:20]
    top_queries_by_impressions = sorted(query_rows, key=lambda r: float(r.get("impressions", 0) or 0), reverse=True)[:20]
    low_ctr_high_impression_pages = [
        r for r in sorted(page_rows, key=lambda r: float(r.get("impressions", 0) or 0), reverse=True)
        if float(r.get("impressions", 0) or 0) >= 100 and float(r.get("ctr", 0) or 0) < 0.03
    ][:20]
    page2_queries = [
        r for r in sorted(query_rows, key=lambda r: float(r.get("impressions", 0) or 0), reverse=True)
        if 4 <= float(r.get("position", 999) or 999) <= 15
    ][:50]

    return {
        "total_clicks": total_clicks,
        "total_impressions": total_impressions,
        "avg_ctr": avg_ctr,
        "avg_position": avg_position,
        "top_pages_by_clicks": top_pages_by_clicks,
        "top_queries_by_impressions": top_queries_by_impressions,
        "low_ctr_high_impression_pages": low_ctr_high_impression_pages,
        "page2_queries": page2_queries,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", required=True, help="Search Console property URL, e.g. https://example.com/ or sc-domain:example.com")
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--outdir", default="")
    parser.add_argument("--service-account", default=os.getenv("GSC_SERVICE_ACCOUNT_JSON", ""))
    parser.add_argument("--data-state", default="final", choices=["final", "all", "hourly_all"])
    args = parser.parse_args()

    if not args.service_account:
        print("Missing service account path. Pass --service-account or set GSC_SERVICE_ACCOUNT_JSON", file=sys.stderr)
        return 2

    outdir = Path(args.outdir or Path.cwd() / "ops" / "search-data" / slugify_site(args.site))
    gsc_dir = outdir / "gsc"
    raw_dir = gsc_dir / "raw"
    ensure_dir(raw_dir)

    service = get_service(args.service_account)

    jobs = {
        "gsc-pages.csv": ["page"],
        "gsc-queries.csv": ["query"],
        "gsc-page-query.csv": ["page", "query"],
        "gsc-page-device.csv": ["page", "device"],
        "gsc-page-country.csv": ["page", "country"],
    }

    outputs = {}
    for filename, dimensions in jobs.items():
        body = {
            "startDate": args.start_date,
            "endDate": args.end_date,
            "dimensions": dimensions,
            "dataState": args.data_state,
        }
        rows = fetch_rows(service, args.site, body)
        normalized = normalize_rows("gsc", args.site, args.start_date, args.end_date, rows, dimensions)
        write_csv(gsc_dir / filename, normalized)
        write_json(raw_dir / f"{filename}.json", rows)
        outputs[filename] = normalized

    try:
        sitemaps = service.sitemaps().list(siteUrl=args.site).execute()
    except Exception as exc:
        sitemaps = {"warning": f"Failed to fetch sitemaps: {exc}"}
    write_json(gsc_dir / "sitemaps.json", sitemaps)

    summary = {
        "site": args.site,
        "range": {"start": args.start_date, "end": args.end_date},
        "gsc": summarize(outputs.get("gsc-pages.csv", []), outputs.get("gsc-queries.csv", [])),
    }
    write_json(gsc_dir / "summary.json", summary)
    print(f"Wrote GSC pack to {gsc_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
