import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_139.txt') if l.strip()]
cache={}
def load(t):
    if t in cache: return cache[t]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    txt=open(d['source']['text_path'],encoding='utf8').read()
    sp=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pages={int(sp[k]):sp[k+1] for k in range(1,len(sp)-1,2)}
    cache[t]=(d,pages);return cache[t]
want=sys.argv[1:]
for i in ids:
    if want and i not in want: continue
    t=i.split('-AR-')[0]
    d,pages=load(t)
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],len(pages),'pages')
    print('STMT:',f['statement']);print('FIELD:',f['field'],'PERIOD:',f['period'],'ATTR:',f['attribution'],'PAGE:',f['page'])
    print('EXC:',f['excerpts'])
    p=f['page']
    for q in (p,):
        s=re.sub(r'[ \t]+',' ',pages.get(q,'??'))
        s=re.sub(r'\n\s*\n+','\n',s)
        print('--PAGE',q,'--');print(s[:3500])
