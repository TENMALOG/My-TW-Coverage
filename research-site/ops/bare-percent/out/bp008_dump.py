import json,sys
sys.stdout.reconfigure(encoding='utf8')
jobs=json.load(open('research-site/ops/bare-percent/jobs_sonnet/bp008.json',encoding='utf8'))
cache={}
for j in jobs:
    t=j['id'].split('-')[0]
    if t not in cache: cache[t]=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in cache[t]['facts'] if x['id']==j['id']][0]
    print('##',j['id'],cache[t]['company'],'|',f['field'],'|',f['period'],'| p',f['page'],'|',f['attribution'])
    print('S:',f['statement'])
    for e in f['excerpts']: print('  -',e)
