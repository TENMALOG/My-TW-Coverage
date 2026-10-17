import json,re,sys
tk=sys.argv[1]
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_068.txt') if l.strip().startswith(tk+'-')]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf-8'))
t=open(d['source']['text_path'],encoding='utf-8').read()
pages={}
for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)',t,re.S):
    pages[int(m.group(1))]=m.group(2)
F={f['id']:f for f in d['facts']}
mode=sys.argv[2] if len(sys.argv)>2 else 'f'
if mode=='f':
    for i in ids:
        f=F[i]; print(i,f['field'],'|',f['statement'],'|',f['period'],'|p',f['page'],'|',f['attribution'])
else:
    for p in sys.argv[2:]:
        print('=====PAGE',p); print(re.sub(r'[ \t]+',' ',pages[int(p)]))
