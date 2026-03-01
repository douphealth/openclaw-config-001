#!/usr/bin/env python3
import re, sys
from pathlib import Path

if len(sys.argv) < 2:
    print('usage: quality_gate.py <markdown-file>')
    sys.exit(2)

text = Path(sys.argv[1]).read_text(errors='ignore')
low = text.lower()

checks = {}
for sec in [
    'a)', 'b)', 'c)', 'd)', 'e)', 'f)', 'g)', 'h)', 'i)', 'j)', 'k)', 'l)', 'm)'
]:
    checks[f'section_{sec}'] = sec in low

checks['has_last_reviewed'] = 'last reviewed' in low
checks['has_affiliate_disclosure'] = 'affiliate disclosure' in low
checks['has_editorial_standard'] = 'editorial standard' in low
checks['has_first_person'] = any(x in low for x in [' i ', "i've", 'my experience', 'we tested', 'in my own'])
checks['faq_count_gte_6'] = len(re.findall(r'^###\s+', text, re.M)) >= 6
checks['has_table'] = ('|' in text and re.search(r'^\|', text, re.M) is not None)
word_count = len(re.findall(r'\b\w+\b', text))
checks['word_count_gte_2500'] = word_count >= 2500
checks['word_count_gte_3500_for_best_posts'] = (('best ' not in low and ' top ' not in low and ' vs ' not in low) or word_count >= 3500)
checks['no_placeholder_operational_plan_block'] = 'this section translates the target query into an operational plan' not in low
checks['no_obvious_template_fillers'] = all(x not in low for x in ['top option #1: evaluation summary','top option #2: evaluation summary','top option #3: evaluation summary'])
checks['no_in_body_h1'] = '<h1' not in low
checks['has_premium_brief'] = ('premium brief' in low and 'what matters most' in low)
checks['citations_count_gte_8'] = (len(re.findall(r'\[[0-9]+\]', text)) >= 8) or (len(re.findall(r'https?://', text)) >= 8)
checks['internal_links_gte_5'] = len(re.findall(r'https?://[^\s\)\]>]+', text)) >= 5
checks['has_visual_modules'] = sum(1 for k in ['quick answer','comparison table','checklist','faq','premium brief','callout','pros','cons'] if k in low) >= 4

failed = [k for k,v in checks.items() if not v]
for k,v in checks.items():
    print(f'{k}: {"PASS" if v else "FAIL"}')

if failed:
    print('\nQUALITY GATE: FAIL')
    sys.exit(1)
print('\nQUALITY GATE: PASS')
