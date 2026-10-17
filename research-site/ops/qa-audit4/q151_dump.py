import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_151.txt',encoding='utf8') if l.strip()]
cache={}
def load(t):
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
        pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
        cache[t]=(d,pages)
    return cache[t]
o=open('research-site/ops/qa-audit4/q151_dump.txt','w',encoding='utf8')
shown=set()
for i in ids:
    t=i.split('-AR-')[0]
    d,pages=load(t)
    f=[x for x in d['facts'] if x['id']==i][0]
    o.write(f"===== {i} {d['company']} {f['field']} | {f['period']} | p{f['page']} | {f['attribution']}\nS: {f['statement']}\nE: {f['excerpts']}\n")
    for p in (f['page'],):
        if (t,p) not in shown:
            shown.add((t,p))
            o.write(f"--- PAGE {p} ---\n"+re.sub(r'[ \t]+',' ',pages.get(p,'MISSING'))+"\n")
            nxt=pages.get(p+1,'')
            o.write(f"--- PAGE {p+1} (head) ---\n"+re.sub(r'[ \t]+',' ',nxt)[:1200]+"\n")
