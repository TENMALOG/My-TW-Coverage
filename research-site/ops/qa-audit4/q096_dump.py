import json,re,sys
tk=sys.argv[1]
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_096.txt') if l.strip()]
ids=[i for i in ids if i.startswith(tk+'-')]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
pages={int(m.group(1)):b for m,b in zip(re.finditer(r'\[PDF PAGE (\d+)\]',txt),re.split(r'\[PDF PAGE \d+\]',txt)[1:])}
F={f['id']:f for f in d['facts']}
shown=set()
for i in ids:
    f=F[i]
    print('=====',i,f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    p=f['page']
    if p not in shown:
        shown.add(p)
        print('--PAGE',p,'--');print(pages.get(p,'')[:2600])
