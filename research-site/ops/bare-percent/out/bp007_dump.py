import json,sys
sys.stdout.reconfigure(encoding='utf8')
jobs=json.load(open('ops/bare-percent/jobs_sonnet/bp007.json',encoding='utf8'))
for j in jobs:
    t=j['id'].split('-')[0]
    d=json.load(open(f'data/company-facts/{t}.json',encoding='utf8'))
    facts=d.get('facts') if isinstance(d,dict) else d
    f=[x for x in facts if x.get('id')==j['id']]
    if not f: print(j['id'],'NOTFOUND'); continue
    f=f[0]
    print('###',j['id']); 
    print({k:(v if k!='excerpts' else v) for k,v in f.items() if k not in('id',)})
