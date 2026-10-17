import json,re,sys
ids=open('research-site/ops/qa-audit4/ids_197.txt').read().split()
lo,hi=int(sys.argv[1]),int(sys.argv[2])
c={}
for i in ids[lo:hi]:
    t=i.split('-AR-')[0]
    if t not in c:
        f=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        tx=open(f['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]',tx)
        c[t]=(f,{int(pages[k]):pages[k+1] for k in range(1,len(pages)-1,2)})
    f,pg=c[t]
    x=[y for y in f['facts'] if y['id']==i][0]
    p=x['page'];txt=pg.get(p,'')
    nx=re.sub(r'\s+',' ',txt)
    key=re.sub(r'\s+',' ',x['excerpts'][0])[:12] if x['excerpts'] else ''
    m=nx.find(key)
    s=max(0,m-150) if m>=0 else 0
    print('=====',i,f['company'],'p',p,x['field'],'|',x['period'],'|',x['attribution'])
    print('STMT:',x['statement'])
    print('PAGE:',nx[s:s+430])
