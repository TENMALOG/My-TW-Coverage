import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_135.txt',encoding='utf8') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
cache={}
def win(txt,exc,W=450):
    chars=[];idx=[]
    for k,c in enumerate(txt):
        if not c.isspace(): chars.append(c);idx.append(k)
    s=''.join(chars)
    pos=None
    for e in exc:
        e2=re.sub(r'\s','',e)
        for L in (len(e2),12,6):
            j=s.find(e2[:L])
            if j>=0: pos=idx[j];break
        if pos is not None: break
    if pos is None: return None
    a=max(0,pos-W//3);b=pos+W*2
    return re.sub(r'\s*\n\s*',' / ',txt[a:b])
for i in ids[lo:hi]:
    tk=i.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        pg={int(m.group(1)):m.group(2) for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)',t,re.S)}
        cache[tk]=(d,pg)
    d,pg=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('='*50);print(i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('S:',f['statement']);print('E:',f['excerpts'])
    p=f['page']
    w=win(pg.get(p,''),f['excerpts'])
    print('PAGE:',w if w else '[NOT FOUND] '+re.sub(r'\s+',' ',pg.get(p,''))[:900])
    if w is None or len(f['excerpts'])>1:
        w2=win(pg.get(p+1,''),f['excerpts'][-1:],400)
        if w2: print('NEXT:',w2[:600])
