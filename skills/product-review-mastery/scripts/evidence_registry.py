#!/usr/bin/env python3
import argparse, json
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--product',required=True);a=ap.parse_args()
    print(json.dumps({'product':a.product,'sources':[],'benchmarks':[],'quotes':[],'limitations':[]},indent=2))
