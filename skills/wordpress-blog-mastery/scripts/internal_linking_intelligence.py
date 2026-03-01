#!/usr/bin/env python3
import argparse
import json

BASE_LINK_TARGETS = {
    'best_of_roundup': (8, 14),
    'head_to_head_comparison': (6, 10),
    'in_depth_review': (5, 9),
    'how_to_guide': (6, 12),
    'explainer_definition': (4, 8),
    'comprehensive_guide': (10, 18),
    'tactical_listicle': (6, 10),
    'news_update': (3, 6),
    'editorial_opinion': (4, 7),
    'case_study': (5, 9),
}


def size_guideline(word_count: int):
    if word_count < 1500:
        return {'out': [4, 6], 'in': [2, 3]}
    if word_count < 3000:
        return {'out': [6, 10], 'in': [3, 5]}
    if word_count < 5000:
        return {'out': [10, 15], 'in': [5, 8]}
    return {'out': [15, 20], 'in': [8, 12]}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--content-type', default='comprehensive_guide')
    ap.add_argument('--word-count', type=int, default=2200)
    ap.add_argument('--post-url', default='')
    ap.add_argument('--primary-keyword', default='')
    ap.add_argument('--cluster', default='')
    ap.add_argument('--hub-page', default='')
    ap.add_argument('--intent-type', default='informational')
    ap.add_argument('--targets-json', default='[]', help='JSON list of {url,title,cluster,role}')
    args = ap.parse_args()

    targets = json.loads(args.targets_json)
    by_type = BASE_LINK_TARGETS.get(args.content_type, (5, 10))
    by_size = size_guideline(args.word_count)

    out_lo = max(by_type[0], by_size['out'][0])
    out_hi = min(by_type[1], by_size['out'][1]) if by_type[1] >= by_size['out'][0] else by_type[1]

    hubs = [t for t in targets if t.get('role') == 'hub']
    siblings = [t for t in targets if t.get('role') in ('sibling', 'spoke')]
    adjacent = [t for t in targets if t.get('role') == 'adjacent']
    money = [t for t in targets if t.get('role') == 'money']

    plan = {
        'internal_link_map': {
            'this_post': {
                'url': args.post_url,
                'primary_keyword': args.primary_keyword,
                'cluster': args.cluster,
                'hub_page': args.hub_page,
                'intent_type': args.intent_type,
            },
            'links_OUT_from_this_post': {
                'to_hub': {
                    'target_url': hubs[0]['url'] if hubs else args.hub_page,
                    'anchor_text': '',
                    'placement': 'intro or first relevant section',
                    'rationale': 'Reinforces cluster relationship',
                },
                'to_siblings': siblings[:6],
                'to_adjacent_clusters': adjacent[:4],
                'to_money_pages': money[:4],
            },
            'links_IN_to_this_post': [],
        },
        'quantity_guidelines': {
            'post_length_words': args.word_count,
            'internal_links_out_target': [max(3, out_lo), max(3, out_hi)],
            'internal_links_in_to_add_target': by_size['in'],
            'hard_limits': {
                'max_internal_links_per_150_words': 1,
                'min_internal_links_per_post': 3,
                'max_repeats_per_target_url': 2,
                'max_links_per_paragraph': 3,
            },
        },
        'placement_map': [
            {'section': 'intro/context', 'count': 1, 'rule': 'one strategic hub link max'},
            {'section': 'core section bodies', 'count': '3-8', 'rule': 'intent-matched depth links only'},
            {'section': 'action/next steps', 'count': '2-4', 'rule': 'journey-forward links only'},
            {'section': 'faq', 'count': '0-2', 'rule': 'only where deeper follow-up is needed'},
        ],
        'anchor_text_rules': {
            'optimal_length_words': [3, 8],
            'exact_match_max_ratio': 0.25,
            'required_properties': ['descriptive', 'contextual', 'expectation-matched', 'semantic-variant aware'],
            'disallowed': ['click here', 'read more', 'here', 'naked URLs'],
        },
        'anti_over_optimization_checks': [
            'No forced exact-match repetition',
            'No irrelevant links inserted for quota',
            'No duplicate anchor text to different URLs in same post',
        ],
    }

    print(json.dumps(plan, indent=2, ensure_ascii=False))
