#!/usr/bin/env python3
import argparse, json, re, statistics

def analyze(txt):
    paras=[p.strip() for p in re.split(r'
\s*
',txt) if p.strip()]
    sents=[s.strip() for s in re.split(r'(?<=[.!?])\s+',txt) if s.strip()]
    words=[re.findall(r"[A-Za-z0-9'-]+",s) for s in sents]
    lens=[len(w) for w in words if w]
    return {
      'paragraphs':len(paras),
      'sentences':len(sents),
      'avg_sentence_words': round(statistics.mean(lens),2) if lens else 0,
      'sentence_stddev': round(statistics.pstdev(lens),2) if len(lens)>1 else 0,
      'long_paragraphs_gt4_sentences': sum(1 for p in paras if len(re.split(r'(?<=[.!?])\s+',p.strip()))>4),
      'recommendations': [
        'Target avg sentence length 15-20 words',
        'Break paragraphs >4 sentences',
        'Insert structural breaks every 300-500 words'
      ]
    }

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('path'); a=ap.parse_args()
    txt=open(a.path,'r',encoding='utf-8',errors='ignore').read()
    print(json.dumps(analyze(txt),indent=2))
