#!/usr/bin/env python3
import os,subprocess,sys
base=os.path.dirname(__file__)
target=os.path.join(base,'codex_usage_report.py')
raise SystemExit(subprocess.call(['python3',target,*sys.argv[1:]]))
