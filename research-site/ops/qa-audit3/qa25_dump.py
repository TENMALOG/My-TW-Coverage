import json,sys,re,os
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_25.txt') if l.strip()]
start,end=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[start:end]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=d['source']['text_path']
    if p not in cache: cache[p]=open(p,encoding='utf8').read()
    txt=cache[p]
    pp=re.split(r'\[PDF PAGE (\d+)\]',txt); pages={int(pp[k]):pp[k+1] for k in range(1,len(pp),2)}
    print('='*30,i,d['company'],'page',f['page'],'npages',len(pages))
    print('FIELD',f['field'],'| PERIOD',f['period'],'| ATTR',f['attribution'])
    print('STMT',f['statement'])
    print('EXC',f['excerpts'])
    pg=f['page']
    for q in (pg,):
        print('--PAGE',q); print(pages.get(q,'')[:3000])
