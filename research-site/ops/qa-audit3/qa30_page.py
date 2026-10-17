import json,re,sys
for id in sys.argv[1:]:
    tk=id.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==id][0]
    t=open(d['source']['text_path'],encoding='utf8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',t)
    pg={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    print('#####',id,f['page'],f['statement']);print(pg.get(f['page'])); 
    if f['page']+1 in pg: print('--NEXT--');print(pg[f['page']+1][:1500])
