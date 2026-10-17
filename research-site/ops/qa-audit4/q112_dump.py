import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_112.txt') if l.strip()]
want=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{want}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
used=set()
for i in ids:
    if i.split('-AR-')[0]!=want: continue
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('ST:',f['statement']); print('EX:',f['excerpts'])
    used.add(f['page'])
for p in sorted(used):
    print('\n######## PAGE',p); print(pages.get(p,'NA')[:int(sys.argv[2]) if len(sys.argv)>2 else 4000])
