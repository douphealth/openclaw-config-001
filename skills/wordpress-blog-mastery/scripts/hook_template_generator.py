#!/usr/bin/env python3
import argparse, json
TEMPLATES={
 'how_to_guide':'You are trying to {goal}, but typical advice misses the real bottleneck: {bottleneck}. In this guide, you will use {method} to get {outcome}.',
 'head_to_head_comparison':'You narrowed it to {a} vs {b}. Most comparisons are outdated or biased. This one uses {method} so you can choose based on {decision_axis}.',
 'in_depth_review':'After {duration} using {product} in {context}, here is the straight verdict: {verdict}. Here is who should buy it and who should skip it.',
 'best_of_roundup':'If you are choosing among {category}, skip the noise. We tested/evaluated by {criteria} and found the best options for {use_cases}.'
}
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--type',default='how_to_guide'); ap.add_argument('--vars',default='{}')
    a=ap.parse_args(); v=json.loads(a.vars)
    t=TEMPLATES.get(a.type,TEMPLATES['how_to_guide'])
    print(t.format(**{k:str(v.get(k,'[...]')) for k in ['goal','bottleneck','method','outcome','a','b','decision_axis','duration','product','context','verdict','category','criteria','use_cases']}))
