#!/usr/bin/env python3
import argparse, json

def route(c:int):
    if c>=8: return 'codex-5.3'
    if c>=4: return 'codex-5.3-mini'
    return 'gpt-4o-mini'

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--task',required=True); ap.add_argument('--complexity',type=int,default=5); ap.add_argument('--max-context-chars',type=int,default=12000)
    a=ap.parse_args()
    m=route(a.complexity)
    print(json.dumps({'model':m,'max_context_chars':a.max_context_chars,'retry_policy':[{'attempt':1,'delay_s':0},{'attempt':2,'delay_s':1.5},{'attempt':3,'delay_s':3.0}], 'fallback_model':'codex-5.3-mini' if m=='codex-5.3' else 'gpt-4o-mini'},indent=2))
