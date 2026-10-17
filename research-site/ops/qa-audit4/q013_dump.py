import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_013.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2]); L=int(sys.argv[3]) if len(sys.argv)>3 else 2500
cache={}
for i in ids[a:b]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=d['source']['text_path']
    if p not in cache:
        raw=open(p,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',raw)
        cache[p]={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    pg=cache[p]; n=f['page']
    print('='*80);print(i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| p',n)
    print('STMT:',f['statement']);print('EXC:',f['excerpts'])
    txt=re.sub(r'[ \t]+',' ',pg.get(n,''))
    print('--PAGE--')
    if L>=0: print(txt[:L])
    else:
        # window around first excerpt line found
        pos=-1
        for e in f['excerpts']:
            k=re.sub(r'\s+','',e)
            m=re.search(r'\s*'.join(map(re.escape,k[:8])),txt)
            if m: pos=m.start();break
        print(txt[max(0,pos-500):pos+1200] if pos>=0 else txt[:1500])
