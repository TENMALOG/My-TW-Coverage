import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_060.txt') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2]); ctx=int(sys.argv[3]) if len(sys.argv)>3 else 3
cache={}
for i in ids[lo:hi]:
    tk=i.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]',t)
        cache[tk]=(d,{int(pages[k]):pages[k+1] for k in range(1,len(pages),2)})
    d,pg=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    p=f['page']
    L=[l for l in pg.get(p,'??').split('\n') if l.strip()]
    keys=[]
    for e in f['excerpts']:
        for part in e.split('\n'):
            part=re.sub(r'\s','',part)
            if len(part)>=5: keys.append(part[:6])
    hit=set()
    for n,l in enumerate(L):
        ls=re.sub(r'\s','',l)
        if any(k in ls for k in keys): hit.update(range(max(0,n-ctx),n+ctx+1))
    print('\n'.join(L[n] for n in sorted(hit) if n<len(L)) if hit else '(NOHIT)\n'+'\n'.join(L[:20]))
