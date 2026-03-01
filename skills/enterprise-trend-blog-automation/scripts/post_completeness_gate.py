#!/usr/bin/env python3
import argparse, json, re
if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('path')
    ap.add_argument('--min-words',type=int,default=3000)
    ap.add_argument('--visual-every-words',type=int,default=200)
    a=ap.parse_args()
    t=open(a.path,encoding='utf-8',errors='ignore').read()
    words=len(re.findall(r"\b\w+\b",re.sub('<[^>]+>',' ',t)))
    visuals=len(re.findall(r'<(table|img|figure|aside|details|div\s+class="oc-|div\s+class="prm-|ul|ol)',t,re.I))
    required=max(1,words//a.visual_every_words)
    checks={
      'word_count':words,
      'min_words_pass':words>=a.min_words,
      'visual_blocks_detected':visuals,
      'required_visual_blocks_min':required,
      'visual_density_pass':visuals>=required,
      'answer_first_present':bool(re.search(r'quick answer|answer-first',t,re.I)),
      'faq_present':bool(re.search(r'<h2[^>]*>\s*faq|frequently asked questions',t,re.I)),
      'meta_placeholders_present':all(k in t.lower() for k in ['title','meta','slug'])
    }
    checks['pass']=checks['min_words_pass'] and checks['visual_density_pass'] and checks['answer_first_present'] and checks['faq_present']
    print(json.dumps(checks,indent=2))
