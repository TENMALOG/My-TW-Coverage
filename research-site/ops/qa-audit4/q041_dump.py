import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_041.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[a:b]:
    tk=i.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
        cache[tk]=(d,pages)
    d,pages=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    pg=pages.get(f['page'],'')+' [[NEXT]] '+pages.get(f['page']+1,'')[:600]
    ex=f['excerpts'][0] if f['excerpts'] else ''
    k=pg.find(ex[:12]); k=max(k,0)
    print('CTX:',pg[max(0,k-250):k+800])
