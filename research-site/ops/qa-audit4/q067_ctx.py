import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_067.txt') if l.strip()]
want=sys.argv[1]; W=int(sys.argv[2]) if len(sys.argv)>2 else 500
only=set(sys.argv[3:])
for i in ids:
    tk=i.split('-AR-')[0]
    if tk!=want or (only and i not in only): continue
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf-8'))
    t=open(d['source']['text_path'],encoding='utf-8').read()
    pg=dict((int(m.group(1)),m.start()) for m in re.finditer(r'\[PDF PAGE (\d+)\]',t))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=f['page']; s=pg[p]; e=pg.get(p+2,len(t))
    seg=t[s:e]
    # normalized with index map
    idx=[];norm=[]
    for k,c in enumerate(seg):
        if not c.isspace(): idx.append(k);norm.append(c)
    n=''.join(norm)
    print('=====',i,f['field'],f['period'],'|',f['attribution'],'| p',p)
    print('STMT:',f['statement'])
    ex=[re.sub(r'\s+','',x) for x in f['excerpts']]
    shown=False
    for x in ex[-1:]+ex[:1]:
        j=n.find(x)
        if j>=0:
            a=idx[max(0,j-W//2)];b=idx[min(len(idx)-1,j+len(x)+W)]
            print('CTX:',re.sub(r'[ \t]+',' ',re.sub(r'\n\s*\n+','\n',seg[a:b])));shown=True;break
    if not shown: print('NOT FOUND in 2 pages')
