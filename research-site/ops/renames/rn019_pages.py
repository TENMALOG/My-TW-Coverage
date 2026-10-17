import sys, json
sys.path.insert(0, 'research-site/scripts/annual')
from slice_annual import page_texts
t, ps = sys.argv[1], [int(x) for x in sys.argv[2:]]
d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf-8'))
tp = d['source']['text_path']
import os
text = open(tp if os.path.exists(tp) else os.path.join('.', tp), encoding='utf-8').read()
pt = page_texts(text)
for p in ps:
    print('=== PAGE', p); print(pt.get(p, '')[:3500])
