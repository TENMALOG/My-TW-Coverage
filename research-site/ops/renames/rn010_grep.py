import json,sys,re
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
t=sys.argv[1]
f=json.load(open(f"research-site/data/company-facts/{t}.json",encoding='utf-8'))
pt=page_texts(open(f['source']['text_path'],encoding='utf-8').read())
r=re.compile(sys.argv[2])
for p,x in sorted(pt.items()):
    for m in r.finditer(x):
        print('p',p,':',x[max(0,m.start()-120):m.end()+160].replace('\n',' '))
