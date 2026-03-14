#!/usr/bin/env python3
import argparse, json, datetime

def build(topic, ctype):
    now=datetime.datetime.utcnow().strftime('%Y-%m-%d')
    return {
      'topic':topic,'content_type':ctype,'generated_at':now,
      'statistics':[],
      'expert_quotes':[],
      'case_examples':[],
      'data_points':[],
      'first_hand_experience':[],
      'rules':[
        'No fabricated statistics',
        'Date every statistic',
        'Prefer primary sources',
        'Mark estimates explicitly'
      ]
    }

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--topic',required=True)
    ap.add_argument('--content-type',default='comprehensive_guide')
    args=ap.parse_args()
    print(json.dumps(build(args.topic,args.content_type),indent=2,ensure_ascii=False))
