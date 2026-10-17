import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_149.txt',encoding='utf8') if l.strip()]
cache={}
def load(t):
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
        pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
        cache[t]=(d,pages)
    return cache[t]
o=open('C:/Users/NEOPEG~1/AppData/Local/Temp/claude/C--Users-Neo-Pegasus-Documents-ChatGPT-078-kaori-sample-artifacts-stock-coverage-audit-20261003-incoming-latest-audit-My-TW-Coverage/1bd92d0e-e36f-4ef8-b701-31d7a9c88c71/scratchpad/dump149.txt','w',encoding='utf8')
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
