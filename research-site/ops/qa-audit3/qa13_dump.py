import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_13.txt') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
cache={}
for id in ids[lo:hi]:
    tk=id.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==id][0]
    tp=d['source']['text_path']
    if tp not in cache:
        t=open(tp,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        cache[tp]={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    pg=cache[tp]
    print('='*60);print(id,d['company'],'|',f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement']);print('EXC:',f['excerpts'])
    p=f['page']; txt=pg.get(p,'')
    key=None
    for e in f['excerpts']:
        for k in (e[:12],e[:6]):
            if k in txt: key=txt.index(k);break
        if key is not None:break
    a=max(0,(key or 0)-80)
    print('--PAGE',p,'' if key is not None else '(excerpt not found)');print(txt[a:a+520])
    pass
