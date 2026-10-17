import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
ids=[l.strip() for l in open(sys.argv[1]) if l.strip()]
a=int(sys.argv[2]); b=int(sys.argv[3]); W=int(sys.argv[4]) if len(sys.argv)>4 else 500
cache={}; seen={}
for i in ids[a:b]:
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
    print('EXC:',' // '.join(f['excerpts']))
    s=pg.get(f['page'],'')
    flat=re.sub(r'\s+',' ',s)
    ex=re.sub(r'\s+',' ',f['excerpts'][0])
    k=flat.find(ex[:30])
    if k<0: k=0
    key=(t,f['page'])
    rng=seen.get(key)
    lo,hi=max(0,k-W),k+W
    if rng and rng[0]<=k and k+len(ex)<=rng[1]:
        print('CTX: (same as above)')
    else:
        a2=lo; b2=hi
        print('CTX:',flat[a2:b2]); seen[key]=(a2,b2)
