import json,sys,re
inp=json.load(open('research-site/ops/qa-audit4/anon_in_3.json',encoding='utf8'))
print(len(inp))
for it in inp:
    t=it['id'].split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    facts=d['facts'] if isinstance(d,dict) and 'facts' in d else d
    f=[x for x in facts if x.get('id')==it['id']][0]
    print('=====',it['id'],f.get('period'),f.get('page'))
    print('S:',f['statement'])
    print('E:',json.dumps(f.get('excerpts'),ensure_ascii=False)[:700])
