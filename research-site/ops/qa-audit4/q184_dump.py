import json,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_184.txt',encoding='utf8') if l.strip()]
cache={}
for i in ids:
    t=i.split('-AR-')[0]
    if t not in cache:
        cache[t]=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    d=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],'|',f['field'],'|',f['period'],'|p',f['page'],'|',f['attribution'])
    print('S:',f['statement'])
    for e in f['excerpts']: print('  E:',e)
