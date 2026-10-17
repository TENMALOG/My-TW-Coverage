import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_025.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[a:b]:
    t=i.split('-AR-')[0]
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]\n',txt)
        pg={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
        cache[t]=(d,pg)
    d,pg=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],'| field',f['field'],'| period',f['period'],'| attr',f['attribution'],'| page',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    p=pg.get(f['page'],'')
    pos=-1
    for e in f['excerpts']:
        k=e.replace(' ','')[:12]
        m=p.replace(' ','').find(k)
    # window by raw search of first 8 chars of excerpt ignoring spaces
    s=p
    if len(p)>1000:
        ex=f['excerpts'][0][:8]
        j=p.find(ex)
        if j<0: j=0
        s=p[max(0,j-100):j+330]
    print('PAGE:',s)
    n=pg.get(f['page']+1,'')
    print('NEXT:',n[:0])
