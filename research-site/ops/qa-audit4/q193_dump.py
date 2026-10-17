import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_193.txt') if l.strip()]
cache={}
lo,hi=int(sys.argv[1]),int(sys.argv[2])
for i in ids[lo:hi]:
    tk=i.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\n\[PDF PAGE (\d+)\]\n',t)
        pg={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
        cache[tk]=(d,pg)
    d,pg=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('='*10,i,d['company'],f['field'],'| period:',f['period'],'| attr:',f['attribution'],'| page',f['page'])
    print('STMT:',f['statement'])
    p=f['page']
    txt=pg.get(p,'')
    ex=f['excerpts'][0] if f['excerpts'] else ''
    print('EXC:',' || '.join(f['excerpts'])[:700])
    # show page text compressed
    c=re.sub(r'[ \t]+',' ',txt); c=re.sub(r'\n\s*\n+','\n',c)
    W=int(sys.argv[3]) if len(sys.argv)>3 else 900
    # locate excerpt via whitespace-insensitive search on its last segment
    key=re.sub(r'\s','',ex.split('||')[-1])[:12]
    cs=''; idx=[]
    for n,ch in enumerate(c):
        if not ch.isspace(): idx.append(n); cs+=ch
    k=cs.find(key) if key else -1
    if k<0: print('PAGE(head):',c[:W])
    else:
        a=max(0,idx[k]-W//2); print('PAGE(ctx):',c[a:a+W])
