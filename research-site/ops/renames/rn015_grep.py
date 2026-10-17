import json,sys,re
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
jobs={j['id']:j for j in json.load(open('research-site/ops/renames/jobs/rn_015.json',encoding='utf-8'))}
pat=re.compile(sys.argv[2])
for t in sys.argv[1].split(','):
    f=json.load(open(f"research-site/data/company-facts/{t}.json",encoding='utf-8'))
    pt=page_texts(open(f['source']['text_path'],encoding='utf-8').read())
    print('=====',t,jobs[t]['company'],jobs[t]['legal_name'],[h['page'] for h in jobs[t]['hits']])
    n=0
    for p,x in sorted(pt.items()):
        for m in pat.finditer(x):
            s=max(0,m.start()-120);print(f'  p{p}:',x[s:m.end()+200].replace('\n',' '));n+=1
            if n>8:break
        if n>8:break
