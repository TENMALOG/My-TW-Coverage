import json,sys,re
t=sys.argv[1]; pages=[int(x) for x in sys.argv[2:]]
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
m={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
for p in pages:
    print('=====',t,'page',p); print(m.get(p))
