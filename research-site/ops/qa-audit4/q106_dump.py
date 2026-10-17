import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_106.txt') if l.strip()]
want=sys.argv[1]
cache={}
seen=set()
for i in ids:
    t=i.split('-AR-')[0]
    if t!=want: continue
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    if t not in cache:
        txt=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
        cache[t]={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    if f['page'] in seen: print('(page %d shown above)'%f['page']); continue
    seen.add(f['page'])
    pg=cache[t].get(f['page'],'')
    print('PAGE:',re.sub(r'\n\s*','\n',pg)[:int(sys.argv[2]) if len(sys.argv)>2 else 2500])
