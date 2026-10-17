import json,re,sys
R='research-site/'
ids=[l.strip() for l in open(R+'ops/qa-audit3/ids_07.txt') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
cache={}
for id in ids[lo:hi]:
    tk=id.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(R+f'data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        cache[tk]=(d,t)
    d,t=cache[tk]
    f=[x for x in d['facts'] if x['id']==id][0]
    p=f['page']
    m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\]|\Z)'%(p,p+1),t,re.S)
    pg=m.group(1) if m else 'NOPAGE'
    print('='*30,id,d['company'])
    print('STATEMENT:',f['statement']);print('FIELD:',f['field'],'| PERIOD:',f['period'],'| ATTR:',f['attribution'],'| PAGE',p)
    print('EXCERPTS:',f['excerpts'])
    # print page region around first excerpt
    ex=f['excerpts'][0][:12] if f['excerpts'] else ''
    i=pg.find(ex)
    print('PAGELEN',len(pg),'excerpt idx',i)
    print('--PAGE--');print(pg[:1800] if i<0 else pg[max(0,i-500):i+1100])
