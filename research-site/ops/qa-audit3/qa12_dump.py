import json,re,sys,os
R='../../../'
ids=[l.strip() for l in open('ids_12.txt',encoding='utf8') if l.strip()]
os.makedirs('qa12_tmp',exist_ok=True)
by={}
for i in ids: by.setdefault(i.split('-AR-')[0],[]).append(i)
for t,l in by.items():
    d=json.load(open(R+f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    txt=open(R+d['source']['text_path'],encoding='utf8',errors='replace').read()
    pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pg={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
    out=[f"##### {t} {d['company']} fy{d['source']['fy']}\n"]
    facts={f['id']:f for f in d['facts']}
    need=set()
    for i in l:
        f=facts[i]
        out.append(f"=== {i} field={f['field']} period={f['period']} page={f['page']} attr={f['attribution']}\nSTATEMENT: {f['statement']}\nEXCERPTS: {f['excerpts']}\n")
        need.add(f['page'])
    out.append("\n######## PAGES\n")
    seen=set()
    for p in sorted(need):
        for q in (p,p+1):
            if q in seen: continue
            seen.add(q)
            out.append(f"--- PAGE {q}\n{re.sub(r'[ \t]+',' ',pg.get(q,''))}\n")
    open(f'qa12_tmp/{t}.txt','w',encoding='utf8').write('\n'.join(out))
    print(t,len(l),sum(len(pg.get(q,'')) for p in need for q in (p,p+1)))
