import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_121.txt') if l.strip()]
cache={}
for i in ids:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=d['source']['text_path']
    if p not in cache: cache[p]=open(p,encoding='utf8').read()
    print('=====',i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'p',f['page'])
    print('S:',f['statement'])
    print('E:',[e[:300] for e in f['excerpts']])
