import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_116.txt') if l.strip()]
tk=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
tx=open(d['source']['text_path'],encoding='utf8').read()
pages=re.split(r'\[PDF PAGE (\d+)\]',tx)
pg={int(pages[i]):pages[i+1] for i in range(1,len(pages)-1,2)}
print('=====',tk,d['company'],d['source']['fy'])
seen=set()
for f in d['facts']:
    if f['id'] in ids:
        print('##',f['id'],f['field'],f['period'],'p',f['page'],f['attribution']);print('STMT:',f['statement']);print('EX:',f['excerpts'])
        if f['page'] not in seen:
            seen.add(f['page'])
            print('PAGE',f['page'],':',re.sub(r'\n+',' | ',pg.get(f['page'],'')) [:3500])
