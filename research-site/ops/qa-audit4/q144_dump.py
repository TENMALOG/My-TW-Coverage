import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_144.txt',encoding='utf8') if l.strip()]
cache={}
out=[]
for i in ids:
    t=i.split('-AR-')[0]
    if t not in cache:
        cache[t]=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    d=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    out.append(f"=== {i} [{d['company']}] field={f['field']} period={f['period']} page={f['page']} attr={f['attribution']}\nSTMT: {f['statement']}\nEXC: {f['excerpts']}")
open(sys.argv[1],'w',encoding='utf8').write('\n'.join(out))
t=json.load(open('research-site/data/company-facts/6125.json',encoding='utf8'))['source']['text_path']
s=open(t,encoding='utf8').read()
print(len(s)); print(repr(s[:600]))
