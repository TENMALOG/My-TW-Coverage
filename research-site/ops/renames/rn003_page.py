import sys, json, re
sys.path.insert(0, 'research-site/scripts/annual')
from slice_annual import page_texts
t, pages, kw = sys.argv[1], sys.argv[2], sys.argv[3:]
f = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf-8'))
txt = open(f['source']['text_path'], encoding='utf-8').read()
pt = page_texts(txt)
for p in pages.split(','):
    if p == 'grep':
        for k in kw:
            for n, s in pt.items():
                for m in re.finditer(k, s):
                    print(n, s[max(0, m.start()-80):m.end()+120].replace('\n', ' '))
    else:
        print('--- page', p); print(pt[int(p)][:3000])
