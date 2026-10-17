import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_135.txt',encoding='utf8') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[lo:hi]:
    tk=i.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        pg={int(m.group(1)):m.group(2) for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)',t,re.S)}
        cache[tk]=(d,pg)
    d,pg=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('='*70);print(i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STATEMENT:',f['statement']);print('EXCERPTS:',f['excerpts'])
    p=f['page']
    for q in (p,p+1):
        txt=re.sub(r'[ \t]+',' ',pg.get(q,''));txt=re.sub(r'\n\s*\n+','\n',txt)
        print(f'--- page {q} ---');print(txt[:1800 if q==p else 500])
