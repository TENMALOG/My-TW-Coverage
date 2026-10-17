import json,sys,re
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
t=sys.argv[1];p=int(sys.argv[2]);kw=sys.argv[3]
f=json.load(open(f"research-site/data/company-facts/{t}.json",encoding='utf-8'))
pt=page_texts(open(f['source']['text_path'],encoding='utf-8').read())
for pg in ([p] if p else pt):
    x=pt.get(pg,'')
    for m in re.finditer(kw,x):
        s=max(0,m.start()-150);print(f'p{pg}:',x[s:m.end()+250].replace('\n',' '));print()
