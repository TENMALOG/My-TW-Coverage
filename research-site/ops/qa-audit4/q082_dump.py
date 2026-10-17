import json,re,sys
root='../../../'
ids=[l.strip() for l in open('ids_082.txt') if l.strip()]
tick=sys.argv[1]
d=json.load(open(root+f'research-site/data/company-facts/{tick}.json',encoding='utf8'))
t=open(root+d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',t)
pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
print('##',tick,d['company'])
ps=[]
for f in d['facts']:
    if f['id'] not in ids: continue
    print('\n=== ',f['id'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('S:',f['statement'])
    print('EX:',f['excerpts'])
    if f['page'] not in ps: ps.append(f['page'])
for p in ps:
    print('\n--- PAGE',p); print(re.sub(r'\n\s*\n+','\n',pages.get(p,'')))
