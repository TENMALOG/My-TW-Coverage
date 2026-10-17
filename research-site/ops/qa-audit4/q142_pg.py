import json,re,sys
t=sys.argv[1];pgs=[int(x) for x in sys.argv[2:]]
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8'))
txt=open(d['source']['text_path'],encoding='utf-8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
c={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
for p in pgs: print('#### PAGE',p); print('\n'.join(l for l in c.get(p,'').split('\n') if l.strip()))
