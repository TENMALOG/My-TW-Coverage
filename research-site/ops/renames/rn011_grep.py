import json,sys,re
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
t=sys.argv[1];pat=re.compile(sys.argv[2]);n=int(sys.argv[3]) if len(sys.argv)>3 else 150
f=json.load(open(f"research-site/data/company-facts/{t}.json",encoding='utf-8'))
pt=page_texts(open(f['source']['text_path'],encoding='utf-8').read())
for p,x in sorted(pt.items()):
    for m in pat.finditer(x):
        print(f'p{p}:',x[max(0,m.start()-n):m.end()+n].replace('\n',' '));
