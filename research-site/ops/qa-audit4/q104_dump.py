import json,re,sys
R='../../../'
ids=[l.strip() for l in open('ids_104.txt') if l.strip()]
by={}
for i in ids: by.setdefault(i.split('-AR-')[0],[]).append(i)
for tk,lst in by.items():
    d=json.load(open(R+f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    t=open(R+d['source']['text_path'],encoding='utf8').read()
    pages={int(m.group(1)):b for m,b in []}
    parts=re.split(r'\[PDF PAGE (\d+)\]',t)
    pg={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    out=open(f'q104_{tk}.txt','w',encoding='utf8')
    out.write(f"=== {tk} {d['company']}\n")
    need=set()
    for f in d['facts']:
        if f['id'] in lst:
            out.write(f"\n## {f['id']} [{f['field']}] period={f['period']} page={f['page']} attr={f['attribution']}\nSTMT: {f['statement']}\n")
            need.add(f['page'])
    out.write("\n\n######## PAGES\n")
    for p in sorted(need):
        for q in (p,p+1):
            out.write(f"\n--- PAGE {q}\n{pg.get(q,'')}\n")
