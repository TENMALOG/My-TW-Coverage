import json,sys,re,subprocess
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_130.txt',encoding='utf8') if l.strip()]
tick=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tick}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',t)
pg={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
pages=set()
for i in ids:
    if i.split('-AR-')[0]!=tick: continue
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],'|',f['period'],'| p',f['page'],'|',f['attribution'])
    print('S:',f['statement'])
    pages.add(f['page'])
for p in sorted(pages):
    print('#### PAGE',p)
    print('\n'.join(l.strip()[:220] for l in pg.get(p,'').split('\n') if l.strip()))
