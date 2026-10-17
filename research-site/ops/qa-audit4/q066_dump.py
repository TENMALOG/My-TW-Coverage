import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_066.txt') if l.strip()]
tk=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
print(tk,d['company'],len(txt))
pages=set()
for f in d['facts']:
    if f['id'] in ids:
        print(f['id'],'|',f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
        print('  S:',f['statement'])
        print('  E:',f['excerpts'])
        pages.add(f['page'])
print(sorted(pages))
import os
open(f'research-site/ops/qa-audit4/q066_{tk}_txt.txt','w',encoding='utf8').write(txt)
