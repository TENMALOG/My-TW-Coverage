import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_092.txt') if l.strip()]
tk=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
pages={int(m.group(1)):b for m,b in zip(re.finditer(r'\[PDF PAGE (\d+)\]',t),re.split(r'\[PDF PAGE \d+\]',t)[1:])}
need=set()
for f in d['facts']:
    if f['id'] in ids:
        print(f['id'],f['field'],'|',f['statement'],'|',f['period'],'|p',f['page'],'|',f['attribution'])
        need.add(f['page'])
for p in sorted(need):
    print('=====PAGE',p); print(re.sub(r'[ \t]+',' ',pages.get(p,'?')))

