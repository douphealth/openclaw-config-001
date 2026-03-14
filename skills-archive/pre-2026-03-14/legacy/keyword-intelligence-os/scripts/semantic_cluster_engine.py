#!/usr/bin/env python3
"""
Lightweight semantic clustering + entity extraction for keyword batches.
Input: JSON list of keyword strings OR newline text file.
Output: JSON clusters with centroid, members, semantic tokens, entity candidates.
"""
import argparse, json, re
from collections import Counter, defaultdict
from pathlib import Path

STOP = {
    'the','a','an','and','or','to','for','of','in','on','with','without','vs','best','how','what','is','are','guide','2026'
}


def tokenize(s):
    return [t for t in re.findall(r"[a-z0-9]+", s.lower()) if t not in STOP and len(t) > 2]


def jaccard(a, b):
    if not a and not b:
        return 1.0
    u = len(a | b)
    return (len(a & b) / u) if u else 0.0


def load_keywords(path):
    txt = Path(path).read_text(errors='ignore').strip()
    if not txt:
        return []
    if txt.startswith('['):
        arr = json.loads(txt)
        return [str(x).strip() for x in arr if str(x).strip()]
    return [x.strip() for x in txt.splitlines() if x.strip()]


def cluster(keywords, threshold=0.35):
    items = [{'kw': k, 'tokens': set(tokenize(k))} for k in keywords]
    clusters = []

    for item in items:
        assigned = False
        for c in clusters:
            sim = jaccard(item['tokens'], c['token_union'])
            if sim >= threshold:
                c['members'].append(item['kw'])
                c['token_union'] |= item['tokens']
                assigned = True
                break
        if not assigned:
            clusters.append({'members': [item['kw']], 'token_union': set(item['tokens'])})

    out = []
    for i, c in enumerate(clusters, start=1):
        token_counts = Counter()
        for m in c['members']:
            token_counts.update(tokenize(m))
        top_tokens = [t for t, _ in token_counts.most_common(8)]
        centroid = ' '.join(top_tokens[:4]) if top_tokens else c['members'][0]
        out.append({
            'cluster_id': i,
            'centroid': centroid,
            'size': len(c['members']),
            'members': c['members'],
            'semantic_tokens': top_tokens,
            'entity_candidates': [t for t in top_tokens if len(t) >= 4][:6]
        })

    out.sort(key=lambda x: x['size'], reverse=True)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True, help='Path to txt (one keyword per line) or JSON array')
    ap.add_argument('--output', required=True, help='Output JSON path')
    ap.add_argument('--threshold', type=float, default=0.35)
    args = ap.parse_args()

    kws = load_keywords(args.input)
    clusters = cluster(kws, threshold=args.threshold)
    result = {
        'keywords_total': len(kws),
        'clusters_total': len(clusters),
        'threshold': args.threshold,
        'clusters': clusters,
    }
    Path(args.output).write_text(json.dumps(result, indent=2))
    print(args.output)


if __name__ == '__main__':
    main()
