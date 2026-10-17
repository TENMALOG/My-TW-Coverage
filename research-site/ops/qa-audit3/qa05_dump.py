import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_05.txt') if l.strip()]
start,end=int(sys.argv[1]),int(sys.argv[2])
W=int(sys.argv[3]) if len(sys.argv)>3 else 700
cache={}
for i in ids[start:end]:
    t=i.split('-AR-')[0]
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
        pm={int(pages[k]):pages[k+1] for k in range(1,len(pages)-1,2)}
        cache[t]=(d,pm)
    d,pm=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('='*60);print(i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('S:',f['statement']);print('E:',f['excerpts'])
    s=pm.get(f['page'],'')
    s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
    flat=s.replace(' ','')
    # find first excerpt position in s (spaces removed mapping)
    idx=[];pos=[]
    for n,c in enumerate(s):
        if c!=' ': pos.append(n)
    a=b=None
    for e in f['excerpts']:
        k=flat.find(re.sub(r'\s+','',e)[:20])
        if k>=0:
            a=pos[k] if a is None else min(a,pos[k]); b=pos[min(k+len(e),len(pos)-1)] if b is None else max(b,pos[min(k+len(e),len(pos)-1)])
    if a is None: print('[excerpt not located] page head:');print(s[:2*W])
    else: print('CTX:',s[max(0,a-W):b+W])
