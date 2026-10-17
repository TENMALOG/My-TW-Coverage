import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_134.txt') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
cache={};seen=set()
def pg(t,n):
    if t not in cache:
        txt=open(t,encoding='utf8').read()
        cache[t]={int(m.group(1)):m.group(2) for m in re.finditer(r'\[PDF PAGE (\d+)\](.*?)(?=\[PDF PAGE \d+\]|\Z)',txt,re.S)}
    return cache[t].get(n,'<none>')
for i in ids[lo:hi]:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],'|',f['attribution'],'|',f['period'],'p',f['page'])
    print('S:',f['statement'])
    key=(tk,f['page'])
    if key not in seen:
        seen.add(key)
        s=pg(d['source']['text_path'],f['page']); s=re.sub(r'\n\s*\n+','\n',s); print('PAGE',key,'\n',s[:1800])
