import json,re,sys
t=sys.argv[1]; pgs=[int(x) for x in sys.argv[2].split(',')]
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8'))
x=open(d['source']['text_path'],encoding='utf-8').read()
p=re.split(r'\[PDF PAGE (\d+)\]',x)
pg={int(p[k]):p[k+1] for k in range(1,len(p),2)}
for n in pgs: print('#### PAGE',n); print('\n'.join(l for l in pg[n].split('\n') if l.strip()))
