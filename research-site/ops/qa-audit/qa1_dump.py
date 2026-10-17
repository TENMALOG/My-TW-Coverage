import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit/ids_1.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[a:b]:
    t=i.split('-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    tp=d['source']['text_path']
    if tp not in cache: cache[tp]=open(tp,encoding='utf8').read()
    txt=cache[tp]
    pg=f['page']
    def page(n):
        m=re.search(r'\[PDF PAGE %d\]'%n,txt)
        if not m: return ''
        e=re.search(r'\[PDF PAGE \d+\]',txt[m.end():])
        return txt[m.end():m.end()+(e.start() if e else 3000)]
    print('='*30,i,d['company'],f['field'],'| attr:',f['attribution'],'| period:',f['period'],'| page',pg)
    print('STATEMENT:',f['statement'])
    print('EXCERPTS:',' / '.join(f['excerpts']))
    p=page(pg)
    # show a window around first excerpt
    k=p.find(f['excerpts'][0][:20]); k=max(0,k-250)
    print('PAGE:',p[k:k+1500].replace('\n',' | '))
    p2=page(pg+1)
    print('NEXT:',p2[:350].replace('\n',' | '))
