import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_191.txt',encoding='utf-8') if l.strip()]
cache={}
tick=sys.argv[1]
for i in ids:
    t=i.split('-AR-')[0]
    if t!=tick: continue
    d=cache.setdefault(t,json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8')))
    f=[x for x in d['facts'] if x['id']==i][0]
    txt=open(d['source']['text_path'],encoding='utf-8').read()
    print('=====',i,f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('S:',f['statement'])
    print('E:',f['excerpts'])
