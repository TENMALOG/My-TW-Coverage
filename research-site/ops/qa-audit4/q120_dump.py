import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_120.txt') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[lo:hi]:
    t=i.split('-AR-')[0]
    d=cache.setdefault(t,json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8')))
    f=[x for x in d['facts'] if x['id']==i][0]
    txt=open(d['source']['text_path'],encoding='utf8').read()
    pages=re.split(r'\n?\[PDF PAGE \d+\]\n',txt)[1:]
    p=f['page']
    print('='*70);print(i,d['company'],f['field'],f['period'],'| attr:',f['attribution'],'| page',p,'npages',len(pages))
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    if len(pages)>1:
        for q in (p,p+1):
            if 1<=q<=len(pages):
                print(f'--- page {q} ---');print(pages[q-1][:2500] if q==p+1 else pages[q-1][:4000])
    else: print('NO FF SPLIT')
