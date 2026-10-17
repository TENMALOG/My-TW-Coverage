import json,sys,os,re
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_10.txt',encoding='utf8') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
W=int(sys.argv[3]) if len(sys.argv)>3 else 700
for i in ids[a:b]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    txt=open(d['source']['text_path'],encoding='utf8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    pg=f['page']
    print('='*70);print(i,d['company'],d['legal_name'])
    print('FIELD',f['field'],'| PERIOD',f['period'],'| ATTR',f['attribution'],'| PAGE',pg)
    print('STMT',f['statement'])
    p=pages.get(pg,'')
    full=p+pages.get(pg+1,'')
    # locate anchor
    pos=-1
    for e in f['excerpts']:
        for key in (e[:25],e[-25:]):
            k=key.split('\n')[0].strip()
            if len(k)>=4:
                pos=p.find(k)
                if pos>=0:break
        if pos>=0:break
    if pos<0: pos=0
    s=max(0,pos-W); 
    print('--PAGE',pg,'len',len(p),'anchor',pos)
    print(full[max(0,pos-W//2):pos+W])
