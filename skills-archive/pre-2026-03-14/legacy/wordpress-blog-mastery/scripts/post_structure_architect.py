#!/usr/bin/env python3
import argparse, json

ARCH={
 'default':['Hook','Answer-first block','Context + methodology','Core section 1','Core section 2','Core section 3','Synthesis/Verdict','Action steps','FAQ','Trust footer'],
 'how_to_guide':['Hook','Answer-first','Prerequisites','Quick steps summary','Detailed step modules','Verification','Troubleshooting','Next steps','FAQ','Trust footer'],
 'best_of_roundup':['Hook','Answer-first','Quick picks table','Evaluation criteria','Item reviews','Comparison matrix','Verdict by use-case','FAQ','Trust footer']
}

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--content-type',default='default'); ap.add_argument('--word-count',type=int,default=2200)
    a=ap.parse_args()
    key=a.content_type if a.content_type in ARCH else 'default'
    sections=ARCH[key]
    checkpoints=[
      {'scroll':'0-20%','goal':'Hook + answer delivered'},
      {'scroll':'20-45%','goal':'Core value with first proof artifact'},
      {'scroll':'45-70%','goal':'Depth + comparison/step clarity'},
      {'scroll':'70-90%','goal':'Decision support + action path'},
      {'scroll':'90-100%','goal':'FAQ + trust close'}
    ]
    print(json.dumps({'content_type':a.content_type,'target_words':a.word_count,'sections':sections,'scroll_checkpoints':checkpoints},indent=2))
