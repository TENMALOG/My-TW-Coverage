import json,sys,re
tick=sys.argv[1]; pages=[int(x) for x in sys.argv[2:]]
d=json.load(open(f'research-site/data/company-facts/{tick}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',t)
pg={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
for p in pages:
    print('#### PAGE',p)
    print('\n'.join(l.strip() for l in pg.get(p,'').split('\n') if l.strip()))
