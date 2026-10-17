import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_030.txt') if l.strip()]
start,end=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[start:end]:
    t=i.split('-AR-')[0]
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
        pm={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
        cache[t]=(d,pm)
    d,pm=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('='*30,i,d['company'])
    print('STATEMENT:',f['statement']);print('field',f['field'],'period',f.get('period'),'attr',f.get('attribution'),'page',f['page'])
    print('EXCERPTS:',f['excerpts'])
    p=f['page']
    pg=pm.get(p,'')+pm.get(p+1,'')
    sq=lambda x:re.sub(r'\s+','',x)
    for ex in sorted(f["excerpts"],key=len)[-1:]:
        k=ex.replace(' ','')[:12]
        # find via squeezed index mapping
        idx=[m.start() for m in re.finditer('.',pg,re.S)]
        flat=''.join(c for c in pg if not c.isspace()); pos=[j for j,c in enumerate(pg) if not c.isspace()]
        n=flat.find(k)
        if n<0: print('  [excerpt not found]'); continue
        a=pos[n]
        print('--- CONTEXT:');print(pg[max(0,a-80):a+380])
