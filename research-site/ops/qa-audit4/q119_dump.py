import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_119.txt') if l.strip()]
want=sys.argv[1:]
cache={}
for i in ids:
    if want and not any(i.startswith(w) for w in want): continue
    tk=i.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
        cache[tk]=(d,pages)
    d,pages=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    for e in f['excerpts']: print('  EX:',e.replace('\n',' / '))
    pt=pages.get(f['page'],'')
    key=f['excerpts'][0].split('\n')[0].strip()[:6] if f['excerpts'] else ''
    idx=pt.find(key) if key else -1
    if idx<0: idx=0
    print('--PAGE',f['page'],'idx',idx)
    print(pt[max(0,idx-20):idx+330])
