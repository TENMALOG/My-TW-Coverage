import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_079.txt') if l.strip()]
start,end=int(sys.argv[1]),int(sys.argv[2])
cache={}
def clean(x): return re.sub(r'\n\s*\n+','\n',x)
for i in ids[start:end]:
    tk=i.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
        cache[tk]=(d,pages)
    d,pages=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('='*70);print(i,d['company'],'|',f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement']);print('EXC:',f['excerpts'])
    p=f['page']
    full=clean(pages.get(p,'MISSING'))+'\n<<NEXT>>\n'+clean(pages.get(p+1,''))
    comp='';mp=[]
    for k,ch in enumerate(full):
        if not ch.isspace(): comp+=ch;mp.append(k)
    key=re.sub(r'\s+','',f['excerpts'][-1])[:10] if f['excerpts'] else ''
    j=comp.find(key)
    if j<0: print('(not located)',full[:1200])
    else:
        a=mp[j];print(full[max(0,a-150):a+350])
