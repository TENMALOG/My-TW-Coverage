import sys, json, re, os
sys.path.insert(0, 'research-site/scripts/annual')
from slice_annual import page_texts
t, pat = sys.argv[1], sys.argv[2]
d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf-8'))
text = open(d['source']['text_path'], encoding='utf-8').read()
for p, s in page_texts(text).items():
    for m in re.finditer(pat, s):
        print(p, '|', s[max(0,m.start()-100):m.end()+150].replace('\n',' '))
