import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_114.txt') if l.strip()]
tk=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
print('=====',tk,d['company'],d['source'])
for f in d['facts']:
    if f['id'] in ids:
        print('##',f['id'],f['field'],f['period'],'p',f['page'],f['attribution']);print(f['statement']);print('EX:',f['excerpts'])
