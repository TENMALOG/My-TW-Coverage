import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_129.txt') if l.strip()]
cache={}
def pages(path):
    if path not in cache:
        t=open(path,encoding='utf8').read()
        cache[path]=t
    return cache[path]
by={}
for i in ids: by.setdefault(i.split('-AR-')[0],[]).append(i)
tk=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=pages(d['source']['text_path'])
print(d['company'],d['source']['text_path'][-20:], len(t))
print(repr(t[:300]))
for f in d['facts']:
    if f['id'] in by[tk]:
        print('---',f['id'],f['field'],f['period'],'p',f['page'],f['attribution'])
        print(f['statement'])
        print(f['excerpts'])
pg={}
parts=re.split(r'\[PDF PAGE (\d+)\]',t)
for k in range(1,len(parts),2): pg[int(parts[k])]=parts[k+1]
need=set()
for f in d['facts']:
    if f['id'] in by[tk]: need.add(f['page']); pass
for p in sorted(need):
    print('=== PAGE',p); print(re.sub(r'[ \t]+',' ',pg.get(p,''))[:2600])
