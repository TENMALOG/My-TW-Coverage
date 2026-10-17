import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_136.txt') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
cache={}
def norm(s): return re.sub(r'\s+','',s)
for i in ids[lo:hi]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    if t not in cache:
        txt=open(d['source']['text_path'],encoding='utf8').read()
        cache[t]={int(m.group(1)):b for m,b in zip(re.finditer(r'\[PDF PAGE (\d+)\]',txt),re.split(r'\[PDF PAGE \d+\]',txt)[1:])}
    p=f['page']
    print('='*60);print(i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| p',p)
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    for q in (p-1,p,p+1):
        pg=cache[t].get(q)
        if pg is None: continue
        n=norm(pg)
        # find first excerpt key
        hit=-1
        for e in f['excerpts']:
            k=n.find(norm(e)[:10])
            if k>=0: hit=k;break
        if hit>=0 or q==p:
            if hit<0: hit=0
            print(f'--PAGE {q} (hit={hit})--');print(n[max(0,hit-150):hit+650])
