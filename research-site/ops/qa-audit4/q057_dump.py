import json,re,sys,collections
root='../../../'
ids=[l.strip() for l in open('ids_057.txt') if l.strip()]
by=collections.OrderedDict()
for i in ids: by.setdefault(i.split('-AR-')[0],[]).append(i)
t=sys.argv[1]
d=json.load(open(f'{root}research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(root+d['source']['text_path'],encoding='utf8').read()
pages={}
for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\[PDF PAGE \d+\]|\Z)',txt,re.S): pages[int(m.group(1))]=m.group(2)
print('COMPANY',t,d['company'])
shown=set()
for f in d['facts']:
    if f['id'] in by[t]:
        print('\n##',f['id'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page']);print('S:',f['statement']);print('E:',f['excerpts'])
        shown.add(f['page'])
for p in sorted(shown):
    print('\n=====PAGE',p);print(pages.get(p,'')[:3000])
    
    nx=pages.get(p+1,'')
    if any(k in nx[:300] for k in ('續','合計')) or True: print('--next',p+1);print(nx[:500])
