import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_080.txt') if l.strip()]
want=sys.argv[1]; full=len(sys.argv)>2
d=json.load(open(f'research-site/data/company-facts/{want}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
pages={int(m.group(1)):b for m,b in zip(re.finditer(r'\[PDF PAGE (\d+)\]',txt),re.split(r'\[PDF PAGE \d+\]',txt)[1:])}
print(d['company'],d['legal_name'],d['source']['fy'])
shown=set()
for f in d['facts']:
    if f['id'] in ids:
        print('=====',f['id'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
        print('STMT:',f['statement'])
        for e in f['excerpts']: print('EXC:',e)
if full:
  for f in d['facts']:
    if f['id'] in ids:
      for p in (f['page'],f['page']+1):
        if p in shown: continue
        shown.add(p)
        print('\n#### PAGE',p); print(re.sub(r'[ \t]+',' ',pages.get(p,'')) )
