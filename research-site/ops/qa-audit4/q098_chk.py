import json, re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_098.txt',encoding='utf8') if l.strip()]
c={}
n=lambda s: re.sub(r'\s+','',s)
for i in ids:
    t=i.split('-AR-')[0]
    if t not in c:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        p=re.split(r'\[PDF PAGE (\d+)\]',txt); c[t]=(d,{int(p[k]):p[k+1] for k in range(1,len(p),2)})
    d,pg=c[t]; f=next(x for x in d['facts'] if x['id']==i)
    pp=n(pg.get(f['page'],'')+pg.get(f['page']+1,''))
    miss=[e for e in f['excerpts'] if n(e) not in pp]
    nums=re.findall(r'\d[\d,]*\.?\d*',f['statement'])
    nm=[x for x in nums if x not in pg.get(f['page'],'')+pg.get(f['page']+1,'')]
    if miss or nm: print(i,'MISS',miss,'NUM',nm)
print('done')
