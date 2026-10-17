import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_012.txt',encoding='utf8') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[a:b]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    tp=d['source']['text_path']
    if tp not in cache:
        txt=open(tp,encoding='utf8').read()
        pm={}
        parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
        for k in range(1,len(parts),2): pm[int(parts[k])]=parts[k+1]
        cache[tp]=pm
    pm=cache[tp]
    p=f['page']
    print('='*60);print(i,d['company'],'|',f['field'],'|',f['period'],'|',f['attribution'],'| p',p)
    print('STMT:',f['statement'])
    pg=pm.get(p,'')
    ex=f['excerpts']
    pos=[pg.find(e) for e in ex]
    pos=[x for x in pos if x>=0]
    if not pos:
        print('EXCERPT NOT ON PAGE', ex); print(pg[:600]); continue
    lo=max(0,min(pos)-300); hi=min(len(pg),max(pos)+300)
    print('CTX:',pg[lo:hi])
