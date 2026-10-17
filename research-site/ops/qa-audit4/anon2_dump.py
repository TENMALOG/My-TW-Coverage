import json
d=json.load(open('anon_in_2.json',encoding='utf-8'))
out=[]
for x in d:
    t=x['id'].split('-AR-')[0]
    f=json.load(open(f'../../data/company-facts/{t}.json',encoding='utf-8'))
    facts=f['facts'] if isinstance(f,dict) and 'facts' in f else f
    m=[y for y in facts if y.get('id')==x['id']][0]
    out.append(f"{x['id']} | {m['statement']} | EX: {' // '.join(m['excerpts'])}")
open('anon2_dump.txt','w',encoding='utf-8').write('\n'.join(out))
