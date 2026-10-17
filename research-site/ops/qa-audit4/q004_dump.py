import json,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_004.txt',encoding='utf8') if l.strip()]
cache={}
def pg(path):
    if path not in cache:
        t=open(path,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        cache[path]={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    return cache[path]
out=open('research-site/ops/qa-audit4/q004_dump.txt','w',encoding='utf8')
seen=set()
for i in ids:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    out.write(f"\n=== {i} {d['company']} field={f['field']} period={f.get('period')} attr={f.get('attribution')} page={f['page']}\nSTMT: {f['statement']}\n")
    P=pg(d['source']['text_path'])
    key=(tk,f['page'])
    if key in seen: out.write("(page text shown earlier)\n"); continue
    seen.add(key)
    for p in (f['page'],f['page']+1):
        out.write(f"--- page {p}\n{re.sub(r'[ \t]+',' ',P.get(p,'')) [:3500]}\n")
out.close()
