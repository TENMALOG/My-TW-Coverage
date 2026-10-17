import json,re,sys
root='../../../'
ids=set(l.strip() for l in open('ids_15.txt') if l.strip())
tick=sys.argv[1]
d=json.load(open(root+f'research-site/data/company-facts/{tick}.json',encoding='utf8'))
txt=open(root+d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pg={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
used=[]
for f in d['facts']:
    if f['id'] not in ids: continue
    print('==',f['id'],f['field'],f['period'],'|',f['attribution'],'| p',f['page'])
    print('ST:',f['statement'])
    print('EX:',' / '.join(f['excerpts']))
    if f['page'] not in used: used.append(f['page'])
for p in used:
    print(f'#### PAGE {p}')
    t=re.sub(r'\n\s*\n+','\n',pg.get(p,''))
    print(t[:int(sys.argv[2]) if len(sys.argv)>2 else 3500])
