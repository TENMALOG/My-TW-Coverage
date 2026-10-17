import json,re,sys,os
sys.stdout.reconfigure(encoding='utf-8')
ids=[l.strip() for l in open('research-site/ops/qa-audit2/ids_1.txt',encoding='utf-8') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
def pages(path):
    if path not in cache:
        t=open(path,encoding='utf-8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        d={}
        for i in range(1,len(parts),2): d[int(parts[i])]=parts[i+1]
        cache[path]=d
    return cache[path]
for i in ids[a:b]:
    tk=i.split('-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf-8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    print('='*70);print(i,d['company'],d.get('legal_name'))
    print('STMT:',f['statement']);print('PERIOD:',f['period'],'| ATTR:',f['attribution'],'| FIELD:',f['field'],'| PAGE:',f['page'])
    print('EXC:',f['excerpts'])
    pg=pages(d['source']['text_path'])
    t=pg.get(f['page'],'')
    e=f['excerpts'][0]; k=t.find(e[:12])
    st=max(0,k-350) if k>=0 else 0
    print('--- p%d (len %d) ---'%(f['page'],len(t)));print(t[st:st+1700])
    miss=[x for x in f['excerpts'] if x[:12] not in t]
    if miss:
        print('--- p+1 head (excerpts not on p) ---');print(pg.get(f['page']+1,'')[:700])
