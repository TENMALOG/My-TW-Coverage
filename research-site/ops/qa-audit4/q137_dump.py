import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_137.txt') if l.strip()]
by={}
for i in ids: by.setdefault(i.split('-AR-')[0],[]).append(i)
for t,l in by.items():
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    txt=open(d['source']['text_path'],encoding='utf8').read()
    print('=====',t,d['company'],d['source']['fy'],len(txt))
    for f in d['facts']:
        if f['id'] in l:
            print(f['id'],f['field'],f['period'],'p',f['page'],f['attribution'])
            print('  S:',f['statement'])
            print('  X:',f['excerpts'])
