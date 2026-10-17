import json,sys,re
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
t=sys.argv[1]
f=json.load(open(f"research-site/data/company-facts/{t}.json",encoding='utf-8'))
pt=page_texts(open(f['source']['text_path'],encoding='utf-8').read())
for p in sys.argv[2:]:
    a,_,b=p.partition(':')
    print('--- p',a); x=pt.get(int(a),'')
    if b:
        i=x.find(b); x=x[max(0,i-300):i+500]
    print(x[:1500])
