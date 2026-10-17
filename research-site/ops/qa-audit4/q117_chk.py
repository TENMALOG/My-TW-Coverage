import json,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_117.txt') if l.strip()]
cache={}
n=lambda s:re.sub(r'\s+','',s)
for i in ids:
    tk=i.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        pg=re.split(r'\n\[PDF PAGE (\d+)\]\n',t)
        cache[tk]=(d,{int(pg[k]):pg[k+1] for k in range(1,len(pg),2)})
    d,pages=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    p=f['page']; txt=n(pages.get(p,''))+n(pages.get(p+1,''))
    miss=[e for e in f['excerpts'] if n(e) not in txt]
    nums=re.findall(r'\d[\d,]*\.?\d*',f['statement'])
    nm=[x for x in nums if x.replace(',','') not in txt.replace(',','')]
    if miss or nm: print(i,'MISS',miss,'NUMS',nm)
print('done')
