import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_052.txt') if l.strip()]
cache={}
def pages(t):
    txt=open(t,encoding='utf8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    return {int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
lo,hi=int(sys.argv[1]),int(sys.argv[2])
for i in ids[lo:hi]:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    if tk not in cache: cache[tk]=pages(d['source']['text_path'])
    f=[x for x in d['facts'] if x['id']==i][0]
    p=f['page']
    print('='*30,i,d['company'],'FY',d['source']['fy'])
    print('STMT:',f['statement']);print('FIELD:',f['field'],'PERIOD:',f['period'],'ATTR:',f['attribution'],'PAGE',p)
    print('EXC:',f['excerpts'])
    pg=cache[tk]
    txt=pg.get(p,'')
    print('--PAGE',p); print(re.sub(r'\n\s*\n+','\n',txt)[:3500])
    if len(txt)>3500 or True:
        nx=pg.get(p+1,'')
        print('--NEXT'); print(re.sub(r'\n\s*\n+','\n',nx)[:1200])
