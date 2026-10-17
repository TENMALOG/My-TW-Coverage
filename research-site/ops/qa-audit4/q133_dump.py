import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_133.txt',encoding='utf8') if l.strip()]
out=open('research-site/ops/qa-audit4/q133_dump.txt','w',encoding='utf8')
cache={}
for i in ids:
    t=i.split('-AR-')[0]
    if t not in cache: cache[t]=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    d=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    out.write(f"=== {i} {d['company']} field={f['field']} period={f['period']} page={f['page']} attr={f['attribution']}\nS: {f['statement']}\nE: {f['excerpts']}\n")
