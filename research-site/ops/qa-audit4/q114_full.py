import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_114.txt') if l.strip()]
for tk in sys.argv[1:]:
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    txt=open(d['source']['text_path'],encoding='utf8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pg={int(parts[i]):re.sub(r'[ \t]+',' ',parts[i+1]) for i in range(1,len(parts),2)}
    print('\n########',tk,d['company'],'FY',d['source']['fy'])
    shown=set()
    for f in d['facts']:
        if f['id'] in ids:
            print('\n## %s | %s | %s | p%s | %s\nSTMT: %s'%(f['id'],f['field'],f['period'],f['page'],f['attribution'],f['statement']))
    pgs=sorted({f['page'] for f in d['facts'] if f['id'] in ids})
    for p in pgs:
        print('\n--- PAGE',p);print(pg.get(p,'MISSING')[:3500])
