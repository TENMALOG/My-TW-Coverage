import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_127.txt') if l.strip()]
tk=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
pages=re.split(r'\[PDF PAGE (\d+)\]\n',t)
pg={int(pages[i]):pages[i+1] for i in range(1,len(pages),2)}
print('COMPANY',d['company'],d['legal_name'],d['source']['fy'])
shown=set()
for f in d['facts']:
    if f['id'] in ids:
        print('\n=== ',f['id'],f['field'],'|',f['period'],'|p',f['page'],'|',f['attribution'])
        print('STMT:',f['statement'])
        print('EXC:',f['excerpts'])
for f in d['facts']:
    if f['id'] in ids:
        p=f['page']
        if p not in shown:
            shown.add(p)
            print('\n##### PAGE',p); print(re.sub(r'[ \n]*\n[ \n]*','\n',pg.get(p,'MISSING'))[:5000])
            print('##### NEXT',p+1); print(re.sub(r'[ \n]*\n[ \n]*','\n',pg.get(p+1,''))[:1500])
