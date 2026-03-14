#!/usr/bin/env python3
import os,subprocess,sys
base=os.path.dirname(__file__)
target=os.path.join(base,'codex_auth_verify.py')
raise SystemExit(subprocess.call(['python3',target,*sys.argv[1:]]))
