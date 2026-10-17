import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_077.txt') if l.strip()]
start,end=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[start:end]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=d['source']['text_path']
    if p not in cache: cache[p]=open(p,encoding='utf8').read().split('\n')
    L=cache[p]
    print('=====',i,d['company'],f['field'],f['period'],'p',f['page'],'|',f['attribution'])
    print('STMT:',f['statement'])
    for e in f['excerpts']:
        print('EXC:',e)
        key=re.sub(r'\s+','',e.split('\n')[0])[:14]
        hit=[n for n,l in enumerate(L) if key in re.sub(r'\s+','',l)]
        if hit:
            n=hit[0]
            print('CTX(line %d, hits %d):'%(n,len(hit)))
            print('\n'.join(L[max(0,n-4):n+int(sys.argv[3]) if len(sys.argv)>3 else n+10]))
        else: print('NOHIT')
