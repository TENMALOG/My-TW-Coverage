import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_036.txt',encoding='utf8') if l.strip()]
want=sys.argv[1]
cache={}
for i in ids:
    t=i.split('-AR-')[0]
    if t!=want: continue
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    if t not in cache:
        txt=open(d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]\n',txt)
        cache[t]={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
        print('#####',t,d['company'],d['source']['fy'])
    f=[x for x in d['facts'] if x['id']==i][0]
    print('\n=== ',i,f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    p=f['page']
    pg=cache[t].get(p,''); k=pg.find(f['excerpts'][0][:8]) if f['excerpts'] else -1; k=max(k,0); print('--PAGE',p,'@',k,'--');print(pg[max(0,k-150):k+600])

