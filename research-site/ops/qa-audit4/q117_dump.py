import json,re,sys
R=''
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_117.txt') if l.strip()]
cache={}
a,b=int(sys.argv[1]),int(sys.argv[2])
for i in ids[a:b]:
    tk=i.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(R+f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        t=open(R+d['source']['text_path'],encoding='utf8').read()
        pg=re.split(r'\n\[PDF PAGE (\d+)\]\n',t)
        pages={int(pg[k]):pg[k+1] for k in range(1,len(pg),2)}
        cache[tk]=(d,pages)
    d,pages=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('='*30,i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    if '--page' in sys.argv:
        p=f['page']
        for q in (p,p+1)[:1 if '--one' in sys.argv else 2]:
            print(f'--- page {q}'); print(re.sub(r'\n\s*\n+','\n',pages.get(q,''))[:3500])
