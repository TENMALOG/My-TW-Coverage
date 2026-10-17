import json,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_034.txt') if l.strip()]
n=lambda x:re.sub(r'\s+','',x)
c={}
for i in ids:
    t=i.split('-AR-')[0]
    if t not in c:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        p=re.split(r'\n\[PDF PAGE (\d+)\]\n',txt)
        c[t]=(d,{int(p[k]):n(p[k+1]) for k in range(1,len(p)-1,2)})
    d,pg=c[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    miss=[e for e in f['excerpts'] if n(e) not in pg.get(f['page'],'')]
    if miss: print(i,f['page'],miss)
