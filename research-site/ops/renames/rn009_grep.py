import json,sys,re
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
tk=sys.argv[1]; pat=re.compile(sys.argv[2])
f=json.load(open(f"research-site/data/company-facts/{tk}.json",encoding='utf-8'))
pt=page_texts(open(f['source']['text_path'],encoding='utf-8').read())
for p,t in sorted(pt.items()):
    for m in pat.finditer(t):
        s=max(0,m.start()-150);print(f'p{p}:',t[s:m.end()+250].replace('\n',' '));print()
