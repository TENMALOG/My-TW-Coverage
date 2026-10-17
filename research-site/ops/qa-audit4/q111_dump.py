import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_111.txt') if l.strip()]
tks=[]
for i in ids:
    t=i.split('-AR-')[0]
    if t not in tks: tks.append(t)
sel=sys.argv[1:] or tks
for tk in sel:
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    print('\n######',tk,d.get('company'),d['source'].get('fy'))
    for f in d['facts']:
        if f['id'] in ids:
            print('\n##',f['id'],f['field'],f['period'],'p',f['page'],f['attribution']);print(f['statement']);print('EX:',f['excerpts'])
