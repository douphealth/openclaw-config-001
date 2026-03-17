#!/usr/bin/env python3
"""Run the search-visibility pipeline for one or many sites.

This is an orchestration wrapper around:
- gsc_pack.py
- bing_webmaster_pack.py
- build_search_visibility_pack.py

Examples:
  python run_search_visibility_pack.py --manifest C:/Users/User/.openclaw/workspace/.secrets/search/sites.json --start-date 2026-02-18 --end-date 2026-03-17
  python run_search_visibility_pack.py --site https://example.com/ --gsc-property https://example.com/ --bing-mode import --bing-queries-file C:/exports/q.csv --bing-pages-file C:/exports/p.csv --start-date 2026-02-18 --end-date 2026-03-17
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List


SCRIPT_DIR = Path(__file__).resolve().parent
GSC_SCRIPT = SCRIPT_DIR / "gsc_pack.py"
BING_SCRIPT = SCRIPT_DIR / "bing_webmaster_pack.py"
MERGE_SCRIPT = SCRIPT_DIR / "build_search_visibility_pack.py"
DEFAULT_MANIFEST = Path("C:/Users/User/.openclaw/workspace/.secrets/search/sites.json")
DEFAULT_OUTROOT = Path("C:/Users/User/.openclaw/workspace/ops/search-data")


def run(cmd: List[str]) -> None:
    print("RUN:", " ".join(cmd))
    result = subprocess.run(cmd)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def load_manifest(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def site_slug(site: Dict[str, Any]) -> str:
    return site.get("slug") or site["siteUrl"].replace("https://", "").replace("http://", "").strip("/").replace(".", "-")


def run_site(site: Dict[str, Any], start_date: str, end_date: str, service_account: str, bing_api_key: str, outroot: Path) -> None:
    slug = site_slug(site)
    outdir = outroot / slug
    outdir.mkdir(parents=True, exist_ok=True)

    gsc_property = site.get("gscProperty") or site.get("siteUrl")
    if gsc_property and service_account:
        run([
            sys.executable,
            str(GSC_SCRIPT),
            "--site", gsc_property,
            "--start-date", start_date,
            "--end-date", end_date,
            "--service-account", service_account,
            "--outdir", str(outdir),
        ])

    bing_mode = (site.get("bingMode") or "").lower().strip()
    bing_site = site.get("bingSiteUrl") or site.get("siteUrl")
    if bing_mode == "api" and bing_api_key:
        method = site.get("bingMethod") or "GetRankAndTrafficStats"
        params_json = json.dumps(site.get("bingParams") or {"siteUrl": bing_site})
        run([
            sys.executable,
            str(BING_SCRIPT),
            "api",
            "--site", bing_site,
            "--method", method,
            "--apikey", bing_api_key,
            "--params-json", params_json,
            "--start-date", start_date,
            "--end-date", end_date,
            "--outdir", str(outdir),
        ])
    elif bing_mode == "import":
        cmd = [
            sys.executable,
            str(BING_SCRIPT),
            "import",
            "--site", bing_site,
            "--start-date", start_date,
            "--end-date", end_date,
            "--outdir", str(outdir),
        ]
        if site.get("bingQueriesFile"):
            cmd += ["--queries-file", site["bingQueriesFile"]]
        if site.get("bingPagesFile"):
            cmd += ["--pages-file", site["bingPagesFile"]]
        if site.get("bingPageQueryFile"):
            cmd += ["--page-query-file", site["bingPageQueryFile"]]
        if site.get("bingSitemapsFile"):
            cmd += ["--sitemaps-file", site["bingSitemapsFile"]]
        run(cmd)

    run([
        sys.executable,
        str(MERGE_SCRIPT),
        "--site", site.get("siteUrl"),
        "--range-label", f"{start_date}_to_{end_date}",
        "--outdir", str(outdir),
    ])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    parser.add_argument("--site", default="")
    parser.add_argument("--gsc-property", default="")
    parser.add_argument("--bing-mode", default="")
    parser.add_argument("--bing-queries-file", default="")
    parser.add_argument("--bing-pages-file", default="")
    parser.add_argument("--bing-page-query-file", default="")
    parser.add_argument("--bing-sitemaps-file", default="")
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--service-account", default=os.getenv("GSC_SERVICE_ACCOUNT_JSON", ""))
    parser.add_argument("--bing-api-key", default=os.getenv("BING_WEBMASTER_API_KEY", ""))
    parser.add_argument("--outroot", default=str(DEFAULT_OUTROOT))
    args = parser.parse_args()

    outroot = Path(args.outroot)
    if args.site:
        site = {
            "siteUrl": args.site,
            "gscProperty": args.gsc_property or args.site,
            "bingSiteUrl": args.site,
            "bingMode": args.bing_mode,
            "bingQueriesFile": args.bing_queries_file,
            "bingPagesFile": args.bing_pages_file,
            "bingPageQueryFile": args.bing_page_query_file,
            "bingSitemapsFile": args.bing_sitemaps_file,
        }
        run_site(site, args.start_date, args.end_date, args.service_account, args.bing_api_key, outroot)
        return 0

    manifest_path = Path(args.manifest)
    if not manifest_path.exists():
        print(f"Manifest not found: {manifest_path}", file=sys.stderr)
        return 2
    manifest = load_manifest(manifest_path)
    sites = [s for s in manifest.get("sites", []) if s.get("enabled", True)]
    if not sites:
        print("No enabled sites in manifest", file=sys.stderr)
        return 2
    for site in sites:
        run_site(site, args.start_date, args.end_date, args.service_account, args.bing_api_key, outroot)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
