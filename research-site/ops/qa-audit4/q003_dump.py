import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_003.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[a:b]:
    tk=i.split('-AR-')[0]
    d=cache.get(tk) or json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    cache[tk]=d
    f=[x for x in d['facts'] if x['id']==i][0]
    t=open(d['source']['text_path'],encoding='utf8').read()
    pg=f['page']
    def page(n):
        m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\]|\Z)'%(n,n+1),t,re.S)
        return m.group(1) if m else ''
    print('=====',i,d['company'],f['field'],f['period'],'|',f['attribution'],'p',pg)
    print('STMT:',f['statement']); print('EXC:',f['excerpts'])
    print('--PAGE--'); print(page(pg)[:2200])
    if len(sys.argv)>3: print('--NEXT--'); print(page(pg+1)[:1200])
