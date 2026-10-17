import json
items=json.load(open('research-site/ops/qa-audit4/rowrank_in.json',encoding='utf-8'))
for it in items:
    t=it['id'].split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8'))
    facts=d['facts'] if isinstance(d,dict) and 'facts' in d else d
    f=[x for x in facts if x.get('id')==it['id']][0]
    print('==',it['id'],'|',f['statement'])
    for k,v in f.items():
        if k not in('statement','id'): print('  ',k,':',str(v)[:700])
