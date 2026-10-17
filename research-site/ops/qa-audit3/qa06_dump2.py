import json,re,sys
R='research-site/'
ids=[l.strip() for l in open(R+'ops/qa-audit3/ids_06.txt') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
cache={}
for n,id in enumerate(ids[lo:hi],lo):
    tk=id.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(R+f'data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        cache[tk]=(d,t)
    d,t=cache[tk]
    f=[x for x in d['facts'] if x['id']==id][0]
    p=f['page']
    m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\]|\Z)'%(p,p+1),t,re.S)
    pg=m.group(1) if m else ''
    N=lambda s:re.sub(r'\s+','',s)
    npg=N(pg)
    miss=[e for e in f['excerpts'] if N(e) not in npg]
    print('=='*5,n,id,d['company'],'|',f['field'],'|',f['period'],'|',f['attribution'],'| pg',p)
    print('S:',f['statement'])
    print('E:',' // '.join(e.replace('\n',' ') for e in f['excerpts']))
    if miss: print('!!MISSING EXCERPTS:',miss)
    # context: for tables, show row context
    ex=f['excerpts'][-1][:14]
    i=pg.find(ex.replace('\n',''))
    if i>=0 and len(sys.argv)>3:
        print('CTX:',pg[max(0,i-int(sys.argv[3])):i+int(sys.argv[3])].replace('\n',' '))
