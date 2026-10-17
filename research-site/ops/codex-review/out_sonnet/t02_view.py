import json,sys,re
ids=[l.strip() for l in open(sys.argv[1]) if l.strip()]
tk=sys.argv[2]
B=int(sys.argv[3]) if len(sys.argv)>3 else 350
cache={}
def find(s,key):
    idx=[k for k,c in enumerate(s) if not c.isspace()]
    ns=''.join(s[k] for k in idx); nk=''.join(c for c in key if not c.isspace())
    n=ns.find(nk)
    return (idx[n], idx[n+len(nk)-1]+1) if n>=0 else None
for i in ids:
    t=i.split('-')[0]
    if t!=tk: continue
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
        pg={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
        cache[t]=(d,pg)
        print('#####',t,d['company'])
    d,pg=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    p=f['page']
    print('=====',i,f['field'],'|',f['statement'],'|',f['period'],'|',f['attribution'],'| p',p)
    s=pg.get(p,'')
    print('EXC:',' // '.join(f['excerpts']))
    a=find(s,f['excerpts'][0])
    if a is None: print('FIRST EXC NOT ON PAGE'); continue
    # last excerpt on p or p+1
    last=f['excerpts'][-1]; b=find(s,last); extra=''
    if b is None:
        s2=pg.get(p+1,''); b2=find(s2,last)
        if b2: extra='[p+1] '+s2[max(0,b2[0]-200):b2[1]+200]
        b=a
    seg=s[max(0,a[0]-B):min(len(s),max(a[1],b[1])+250)]
    print('CTX:',re.sub(r'\s*\n\s*',' / ',seg)); 
    if extra: print(re.sub(r'\s*\n\s*',' / ',extra))
