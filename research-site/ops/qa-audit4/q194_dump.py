import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_194.txt') if l.strip()]
tk=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',t)
pg={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
used=set()
for f in d['facts']:
    if f['id'] in ids:
        print('=====',f['id'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
        print('S:',f['statement'])
        used.add(f['page'])
for p in sorted(used):
    print('######## PAGE',p)
    print(re.sub(r'[ \t]*\n[ \t]*','\n',pg.get(p,'')).strip())
    print('######## PAGE',p+1,'(next, head)')
    print(re.sub(r'[ \t]*\n[ \t]*','\n',pg.get(p+1,'')).strip()[:800])
