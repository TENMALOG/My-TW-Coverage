import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_26.txt') if l.strip()]
cache={}
a,b=int(sys.argv[1]),int(sys.argv[2])
for i in ids[a:b]:
    tk=i.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]\n',t)
        pg={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
        cache[tk]=(d,pg)
    d,pg=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',' // '.join(f['excerpts']))
    p=f['page']; txt=pg.get(p,'')
    # window around first excerpt token
    key=None
    for e in f['excerpts']:
        k=e[:12]
        j=txt.find(k)
        if j>=0: key=j;break
    if key is None: seg=txt[:900]
    else: seg=txt[max(0,key-250):key+500]
    print('PAGE:',seg)
