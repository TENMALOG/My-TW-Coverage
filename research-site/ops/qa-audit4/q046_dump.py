import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_046.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[a:b]:
    t=i.split('-AR-')[0]
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
        P={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
        cache[t]=(d,{f['id']:f for f in d['facts']},P)
    d,fm,P=cache[t]
    f=fm.get(i)
    print('='*20,i,d['company'])
    if not f:
        print('MISSING'); continue
    print({k:v for k,v in f.items() if k not in('verification','id')})
    pg=f.get('page')
    p=int(pg[0]) if isinstance(pg,list) else int(pg)
    ex=f.get('excerpts') or []
    pt=P.get(p,'')
    lines=pt.split('\n')
    hit=[k for k,l in enumerate(lines) if any(e.replace(' ','')[:10] and e.replace(' ','')[:10] in l.replace(' ','') for e in ex if e.strip())]
    lo=max(0,(min(hit) if hit else 0)-9)
    hi=(max(hit)+4) if hit else 30
    print('--PAGE',p)
    print('\n'.join(lines[lo:hi]))
