import json,sys,re
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
jobs={j['id']:j for j in json.load(open('research-site/ops/renames/jobs/rn_007.json',encoding='utf-8'))}
tid=sys.argv[1]; pat=re.compile(sys.argv[2]); w=int(sys.argv[3]) if len(sys.argv)>3 else 150
f=json.load(open(f"research-site/data/company-facts/{tid}.json",encoding='utf-8'))
pt=page_texts(open(f['source']['text_path'],encoding='utf-8').read())
print('hit pages',[h['page'] for h in jobs[tid]['hits']])
for p,t in pt.items():
    for m in pat.finditer(t):
        print(f'p{p}:',t[max(0,m.start()-w):m.end()+w].replace('\n',' '));print()
