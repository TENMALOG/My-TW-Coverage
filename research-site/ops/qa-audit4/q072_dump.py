import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_072.txt') if l.strip()]
by={}
for i in ids: by.setdefault(i.split('-AR-')[0],[]).append(i)
t=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
pgs=set()
for f in d['facts']:
    if f['id'] in by[t]:
        print(f['id'],f['field'],'|',f['statement'],'|',f['period'],'|',f['attribution'],'| p',f['page'],'|',f['excerpts'])
        pgs.add(f['page'])
for p in sorted(pgs):
    print('=====PAGE',p)
    print(pages.get(p,'NA'))
    if len(sys.argv)>2:
        print('=====PAGE',p+1)
        print(pages.get(p+1,'NA'))
