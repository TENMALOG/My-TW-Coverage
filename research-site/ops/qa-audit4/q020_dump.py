import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_020.txt') if l.strip()]
cur=None
lo,hi=int(sys.argv[1]),int(sys.argv[2])
cache={}
shown=set()
for n,i in enumerate(ids[lo:hi],lo):
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    if tk not in cache:
        t=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]\n',t)
        pg={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
        cache[tk]=pg
    pg=cache[tk]
    print(f"##### {n} {i} [{d['company']}] field={f['field']} period={f['period']} attr={f['attribution']} page={f['page']}")
    print("STMT:",f['statement'])
    key=(tk,f['page'])
    if key not in shown:
        shown.add(key)
        print(f"--- PAGE {f['page']} ---");print(pg.get(f['page'],'MISSING')[:3000])
        print(f"--- PAGE {f['page']+1} (head) ---");print(pg.get(f['page']+1,'')[:500])
    else: print("(page already shown)")
