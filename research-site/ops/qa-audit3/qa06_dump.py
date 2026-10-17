import json,re,sys
R='research-site/'
ids=[l.strip() for l in open(R+'ops/qa-audit3/ids_06.txt') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
cache={};seen=set()
for n,id in enumerate(ids[lo:hi],lo):
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
    print('='*20,n,id,d['company'])
    print('STMT:',f['statement']);print('FIELD:',f['field'],'| PER:',f['period'],'| ATTR:',f['attribution'],'| PG',p)
    print('EX:',f['excerpts'])
    ex=f['excerpts'][0][:10] if f['excerpts'] else ''
    i=pg.find(ex)
    print('--PAGE-- len',len(pg),'idx',i)
    key=(tk,p)
    if key in seen and len(pg)<2500: print('(same page as before)')
    else: print(pg[:1000] if len(pg)<1000 or i<0 else pg[max(0,i-250):i+600])
    seen.add(key)
