import json,sys,re
root='research-site/'
ids=[l.strip() for l in open(root+'ops/qa-audit4/ids_063.txt') if l.strip()]
by={}
for i in ids: by.setdefault(i.split('-AR-')[0],[]).append(i)
for t,l in by.items():
    d=json.load(open(root+f'data/company-facts/{t}.json',encoding='utf8'))
    print('=====',t,d['company'],d['source']['text_path'])
    for f in d['facts']:
        if f['id'] in l:
            print(f['id'],'|',f['field'],'|',f['period'],'|p',f['page'],'|',f['attribution'])
            print('  S:',f['statement'])
            print('  E:',' // '.join(f['excerpts']))
