import json,sys,re,os
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_130.txt',encoding='utf8') if l.strip()]
tick=sys.argv[1]
cache={}
for i in ids:
    t=i.split('-AR-')[0]
    if t!=tick: continue
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i]
    if not f: print(i,'MISSING');continue
    f=f[0]
    print('=====',i,f['field'],'|',f['period'],'| p',f['page'],'|',f['attribution'])
    print('S:',f['statement'])
    print('E:',f['excerpts'])
if True:
    d=json.load(open(f'research-site/data/company-facts/{tick}.json',encoding='utf8'))
    print('TEXT',d['source']['text_path'])
