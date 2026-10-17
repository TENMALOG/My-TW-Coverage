import json,sys,re
ids=[l.strip() for l in open(sys.argv[1]) if l.strip()]
W=int(sys.argv[2]) if len(sys.argv)>2 else 350
cache={}
for i in ids:
    t=i.split('-')[0]
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
        pg={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
        cache[t]=(d,pg)
    d,pg=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],'| p',f['page'],'|',f['period'],'|',f['attribution'])
    print('STMT:',f['statement'])
    p=f['page']
    s=pg.get(p,'')+'\n[[NEXT]]'+pg.get(p+1,'')
    ex=f['excerpts']
    def find(e):
        k=s.find(e)
        if k<0:
            k=s.find(re.sub(r'\s+','',e)[:6])
        return k
    a=find(ex[0]); 
    b=max(find(e) for e in ex)+len(ex[-1])
    lo=max(0,a-W//2); hi=min(len(s),max(b,a)+W)
    print('CTX:',re.sub(r'\n+',' ¶ ',s[lo:hi]))
