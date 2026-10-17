import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_19.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[a:b]:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    if tk not in cache:
        t=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        pg={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
        cache[tk]=pg
    pg=cache[tk]
    print('='*70);print(i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| page',f['page'])
    print('STMT:',f['statement']);print('EXC:',f['excerpts'])
    p=f['page']
    T=pg.get(p,'')
    pos=[T.find(e[:12]) for e in f['excerpts'] if T.find(e[:12])>=0]
    c=min(pos) if pos else 0
    print('--- PAGE',p,'around',c,'len',len(T));print(T[max(0,c-200):c+850])
    if len(T)-c<500: print('--- NEXT');print(pg.get(p+1,'')[:350])
