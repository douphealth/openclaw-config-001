#!/usr/bin/env python3
import argparse,json
REQ={
 'best_of_roundup':[1,2,3,4,6,7,9,10,12,13,14],
 'head_to_head_comparison':[1,2,4,6,7,9,10,12,13,14],
 'in_depth_review':[1,2,6,9,10,12,13,14],
 'how_to_guide':[1,2,4,8,9,13,14],
 'explainer_definition':[1,2,4,9,13,14],
 'comprehensive_guide':[1,2,4,5,9,13,14],
 'tactical_listicle':[1,2,9,13,14],
 'case_study':[1,2,11,9,13,14]
}
OPT={
 'best_of_roundup':[5,11,16],'head_to_head_comparison':[3,5,11],'in_depth_review':[4,5,7,11,16],'how_to_guide':[5,15,16],'explainer_definition':[5,11,16],'comprehensive_guide':[7,8,11,15,16],'tactical_listicle':[4,5],'case_study':[4,5,16]
}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--content-type',required=True);a=ap.parse_args();k=a.content_type
 print(json.dumps({'content_type':k,'required_components':REQ.get(k,[]),'optional_components':OPT.get(k,[])},indent=2))
