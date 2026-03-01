#!/usr/bin/env python3
import argparse, json, re

def classify(text: str):
    t = text.lower()
    rules = [
        (r'\b(best|top|recommended)\b', 'best_of_roundup'),
        (r'\b(vs|versus|compared to)\b', 'head_to_head_comparison'),
        (r'\breview\b', 'in_depth_review'),
        (r'\b(how to|tutorial|step by step)\b', 'how_to_guide'),
        (r'\b(what is|explained|definition)\b', 'explainer_definition'),
        (r'\b(complete guide|ultimate guide|comprehensive)\b', 'comprehensive_guide'),
        (r'\b(\d+ ways|\d+ tips|list of)\b', 'tactical_listicle'),
        (r'\b(news|update|announced|release)\b', 'news_update'),
        (r'\b(opinion|perspective|analysis)\b', 'editorial_opinion'),
        (r'\b(case study|experiment|results)\b', 'case_study'),
    ]
    for pattern, ctype in rules:
        if re.search(pattern, t):
            return ctype
    # fallback comparison heuristic for "X or Y" phrasing
    if ' or ' in t and len(t.split()) <= 16:
        return 'head_to_head_comparison'
    return 'comprehensive_guide'

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('brief')
    args = ap.parse_args()
    print(json.dumps({'content_type': classify(args.brief)}, indent=2))
