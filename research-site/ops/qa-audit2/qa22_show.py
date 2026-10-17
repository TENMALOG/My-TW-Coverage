import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit2/ids_2.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[a:b]:
    t=i.split('-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=d['source']['text_path']
    if p not in cache: cache[p]=open(p,encoding='utf8').read()
    txt=cache[p]
    pg=f['page']
    def page(n):
        m=re.search(r'\[PDF PAGE %d\]'%n,txt)
        if not m: return ''
        e=re.search(r'\[PDF PAGE %d\]'%(n+1),txt)
        return txt[m.end():e.start() if e else m.end()+3000]
    print('='*30,i,d['company'])
    print('STMT:',f['statement']);print('PERIOD:',f['period'],'PAGE',pg,'ATTR',f['attribution'])
    print('EXC:',f['excerpts'])
    pt=page(pg); n=pt.find(f['excerpts'][0][:20]) 
    # show window around first excerpt
    s=max(0,n-350) if n>=0 else 0
    print('PAGE:',pt[s:s+1300])
    if '表' in f['statement'] or '合計' in f['statement'] or len(pt)-s<1300:
        print('NEXT:',page(pg+1)[:500])
