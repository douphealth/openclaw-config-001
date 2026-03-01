#!/usr/bin/env python3
import argparse, json

if __name__ == '__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--keyword-data-json',required=True); ap.add_argument('--blog-json',required=True)
    a=ap.parse_args(); kw=json.loads(a.keyword_data_json); blog=json.loads(a.blog_json)
    k=kw.get('final_keyword') or kw.get('keyword') or 'keyword'
    u=blog.get('url','')
    bundle={
      'facebook': {'post_text': f"{k}: practical breakdown from our latest guide. What has worked best for you so far?", 'first_comment': f"Read full guide: {u}", 'hashtags':['#growth','#strategy','#marketing']},
      'instagram': {'caption': f"{k} in 7 practical slides. Save this for later. Link in bio.", 'slides':7},
      'gmb': {'post_text': f"New update on {k}: actionable guidance for local operators. Learn more on our site.", 'cta_type':'LEARN_MORE','cta_url':u},
      'pinterest': {'pin_title': f"{k}: Complete Practical Guide", 'pin_description': f"Actionable tips for {k}. Read full guide.", 'destination_link':u}
    }
    print(json.dumps({'platforms':bundle,'metadata':{'keyword':k,'blog_url':u}},indent=2))
