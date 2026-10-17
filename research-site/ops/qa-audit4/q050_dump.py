import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_050.txt') if l.strip()]
want=sys.argv[1]; lim=int(sys.argv[2])
tk=want
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
pages={int(m.group(1)):s for m,s in zip(re.finditer(r'\[PDF PAGE (\d+)\]',t),re.split(r'\[PDF PAGE \d+\]',t)[1:])}
print('=====',tk,d['company'],d['source']['fy'])
fs={f['id']:f for f in d['facts']}
seen=set()
for i in ids:
    if i not in fs: continue
    f=fs[i]
    print('---',i,f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    seen.add(f['page'])
for pn in sorted(seen):
    print('##### PAGE',pn)
    x=re.sub(r'[ \t]+',' ',pages.get(pn,''))
    x=re.sub(r'\s*\n\s*','\n',x)
    print(x[:lim])
