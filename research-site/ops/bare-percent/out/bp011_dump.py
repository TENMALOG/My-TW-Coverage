import json,sys
sys.stdout.reconfigure(encoding='utf-8')
jobs=json.load(open('research-site/ops/bare-percent/jobs_sonnet/bp011.json',encoding='utf-8'))
cache={}
for j in jobs:
    t=j['id'].split('-')[0]
    if t not in cache: cache[t]=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8'))
    f=[x for x in cache[t]['facts'] if x['id']==j['id']][0]
    print(j['id'],f['field'],'|',f['statement'],'|',f['period'],'p',f['page'],'|',f['attribution'])
    for e in f['excerpts']: print('   >',e)
