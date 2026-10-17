import json,sys,re
ids=[l.strip() for l in open(sys.argv[1]) if l.strip()]
W=int(sys.argv[2]) if len(sys.argv)>2 else 500
tk=sys.argv[3] if len(sys.argv)>3 else None
cache={}
shown=set()
for i in ids:
    t=i.split('-')[0]
    if tk and t!=tk: continue
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
        pg={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
        cache[t]=(d,pg)
    d,pg=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    p=f['page']
    s=pg.get(p,'')
    print('=====',i,'STMT:',f['statement'])
    key=f['excerpts'][-1]
    def find(s,key):
        idx=[k for k,c in enumerate(s) if not c.isspace()]
        ns=''.join(s[k] for k in idx); nk=''.join(c for c in key if not c.isspace())
        n=ns.find(nk)
        return idx[n] if n>=0 else -1
    pos=find(s,key); q=p
    if pos<0:
        s=pg.get(p+1,''); pos=find(s,key); q=p+1
    # whole-page start of header region
    a=max(0,pos-W); b=min(len(s),pos+len(key)+W//3)
    print(f'[p{q} pos{pos}]',s[a:b].replace('\n',' / '))
