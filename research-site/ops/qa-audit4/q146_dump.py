import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_146.txt') if l.strip()]
tick=sorted(set(i.split('-AR-')[0] for i in ids))
for t in tick:
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    txt=open(d['source']['text_path'],encoding='utf8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pg={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    print('#### COMPANY',t,d['company'],d['legal_name'])
    shown=set()
    for f in d['facts']:
        if f['id'] not in ids: continue
        print('=====',f['id'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
        print('STMT:',f['statement'])
        print('EXC:',f['excerpts'])
        if f['page'] not in shown:
            shown.add(f['page'])
            print('--PAGE',f['page']); print(re.sub(r'[ \t]+',' ',pg.get(f['page'],'MISSING'))[:2200])
