import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_056.txt') if l.strip()]
tick=sys.argv[1]
sel=[i for i in ids if i.startswith(tick+'-')]
d=json.load(open(f'research-site/data/company-facts/{tick}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
pg={int(pages[i]):pages[i+1] for i in range(1,len(pages),2)}
byid={f['id']:f for f in d['facts']}
full='--full' in sys.argv
shown=set()
for i in sel:
    f=byid[i]
    print('=====',i,f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
for i in sel:
    f=byid[i]
    for p in (f["page"],):
        if p in shown or not full: continue
        shown.add(p); print('#### PAGE',p); print(pg.get(p,'')[:3000])
