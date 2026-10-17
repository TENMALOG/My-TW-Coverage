import json,re,sys
R='research-site'
ids=[l.strip() for l in open(f'{R}/ops/qa-audit4/ids_022.txt',encoding='utf8') if l.strip()]
cache={}
def pages(t):
    if t not in cache:
        txt=open(t,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
        cache[t]={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    return cache[t]
def norm(s): return re.sub(r'\s+','',s)
files={}
lo,hi=int(sys.argv[1]),int(sys.argv[2])
W=int(sys.argv[3]) if len(sys.argv)>3 else 1400
for i in ids[lo:hi]:
    tk=i.split('-AR-')[0]
    if tk not in files: files[tk]=json.load(open(f'{R}/data/company-facts/{tk}.json',encoding='utf8'))
    d=files[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=pages(d['source']['text_path'])
    p=f['page']
    print('='*20,i,d['company'],f['field'],f['period'],'|',f['attribution'],'| p',p)
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    cur=norm(pg.get(p,''))
    full=cur+'<<NEXT>>'+norm(pg.get(p+1,''))
    pos=-1
    for k in f['excerpts']:
        k2=norm(k)
        if len(k2)>=6:
            pos=full.find(k2[:10])
            if pos>=0: break
    a=max(0,pos-120) if pos>=0 else 0
    print('CTX:',full[a:a+W])
