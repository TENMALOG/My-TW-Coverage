import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_123.txt',encoding='utf8') if l.strip()]
t=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
pages={}
for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)',txt,re.S):
    pages[int(m.group(1))]=re.sub(r'\s*\n\s*','',m.group(2))
print('COMPANY',d['company'],d['legal_name'])
pp=set()
for f in d['facts']:
    if f['id'] in ids:
        print('\n##',f['id'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page']);print(f['statement']);pp.add(f['page'])
for p in sorted(pp):
    print('\n=== PAGE',p);print(pages.get(p,'')[:5000])
    if p+1 in pages and len(pages[p])<5000: pass
