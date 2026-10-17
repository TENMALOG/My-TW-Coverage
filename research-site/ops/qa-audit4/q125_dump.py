import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_125.txt',encoding='utf8') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
cache={}
def pages(t):
    if t not in cache:
        txt=open(t,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
        cache[t]={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    return cache[t]
for i in ids[lo:hi]:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=pages(d['source']['text_path'])
    print('='*80);print(i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STATEMENT:',f['statement']);print('EXC:',f['excerpts'])
    pg=f['page']
    s=p.get(pg,'')
    # show only part around first excerpt
    
    ex=f['excerpts'][0][:12]; k=s.find(ex)
    if k<0: k=0
    print('--WIN--');print(s[max(0,k-100):k+380])
    if len(sys.argv)>3: print('--PAGE',pg+1,'--');print(p.get(pg+1,'')[:1500])
