import json,re,sys
R='research-site/'
ids=[l.strip() for l in open(R+'ops/qa-audit3/ids_07.txt') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
cache={}
def norm(s): return re.sub(r'\s+','',s)
for n,id in enumerate(ids[lo:hi],lo):
    tk=id.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(R+f'data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        cache[tk]=(d,t)
    d,t=cache[tk]
    f=[x for x in d['facts'] if x['id']==id][0]
    p=f['page']
    def pg(k):
        m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\]|\Z)'%(k,k+1),t,re.S)
        return m.group(1) if m else ''
    P=norm(pg(p)); P2=norm(pg(p)+pg(p+1)+pg(p-1))
    print('='*10,n,id,d['company'],'|',f['field'],'|',f['period'],'|',f['attribution'],'| p',p)
    print('S:',f['statement'])
    for e in f['excerpts']:
        print('  EX[%s]'%('Y' if norm(e) in P else ('adj' if norm(e) in P2 else 'N')),e)
