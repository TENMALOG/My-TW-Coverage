import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_105.txt') if l.strip()]
tk=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
print(d['company'],d['source']['fy'],len(txt)); print(repr(txt[:300]))
for f in d['facts']:
    if f['id'] in ids:
        print('\n##',f['id'],f['field'],f['period'],'p',f['page'],f['attribution']);print(f['statement']);print(f['excerpts'])
