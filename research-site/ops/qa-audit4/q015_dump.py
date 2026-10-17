import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_015.txt') if l.strip()]
want=sys.argv[1:]
by={}
for i in ids: by.setdefault(i.split('-AR-')[0],[]).append(i)
for tk in want:
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    t=open(d['source']['text_path'],encoding='utf8').read()
    parts=re.split(r'\n\[PDF PAGE (\d+)\]\n',t)
    pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    print('=====',tk,d['company'])
    pg=set()
    for f in d['facts']:
        if f['id'] in by[tk]:
            print(f['id'],f['field'],'|',f['statement'],'|',f['period'],'| p',f['page'],'|',f['attribution'])
            pg.add(f['page'])
    for p in sorted(pg):
        print('--- PAGE',p); print(re.sub(r'[ \t]+',' ',pages.get(p,'?')))
        print('--- PAGE',p+1,'(start)'); print(re.sub(r'[ \t]+',' ',pages.get(p+1,'?'))[:1200])
