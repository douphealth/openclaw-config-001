#!/usr/bin/env python3
import argparse, json

if __name__ == '__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--bundle-json',required=True)
    a=ap.parse_args(); b=json.loads(a.bundle_json)
    issues=[]
    p=b.get('platforms',{})
    if 'facebook' not in p: issues.append('missing_facebook')
    if 'instagram' not in p: issues.append('missing_instagram')
    if 'gmb' not in p: issues.append('missing_gmb')
    if 'pinterest' not in p: issues.append('missing_pinterest')
    if p.get('facebook',{}).get('first_comment','').strip()=='' : issues.append('facebook_first_comment_missing')
    if p.get('gmb',{}).get('cta_url','').strip()=='' : issues.append('gmb_cta_url_missing')
    print(json.dumps({'pass':len(issues)==0,'issues':issues},indent=2))
