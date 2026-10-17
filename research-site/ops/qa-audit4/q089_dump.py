import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
t=sys.argv[1]
ids=set(l.strip() for l in open('research-site/ops/qa-audit4/ids_089.txt') if l.strip())
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8'))
txt=open(d['source']['text_path'],encoding='utf-8').read()
pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
pg={int(pages[i]):pages[i+1] for i in range(1,len(pages),2)}
pp=set()
for f in d['facts']:
    if f['id'] in ids:
        print('=====',f['id'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
        print('S:',f['statement']); print('E:',f['excerpts'])
        pp.add(f['page'])
for p in sorted(pp):
    print('\n######## PAGE',p); print(pg.get(p,'')[:int(sys.argv[2]) if len(sys.argv)>2 else 6000])
