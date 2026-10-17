import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_144.txt',encoding='utf8') if l.strip()]
tick=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tick}.json',encoding='utf8'))
s=open(d['source']['text_path'],encoding='utf8').read()
pages=dict((int(m.group(1)),m.group(2)) for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)',s,re.S))
print('#',tick,d['company'],d['source']['fy'])
shown=set()
for f in d['facts']:
    if f['id'] not in ids: continue
    print(f"\n=== {f['id']} field={f['field']} period={f['period']} page={f['page']} attr={f['attribution']}\nSTMT: {f['statement']}")
    p=f['page']
    for q in (p,p+1):
        if q in pages and q not in shown:
            shown.add(q); print(f'--- PAGE {q}\n'+re.sub(r'[ \t]+',' ',pages[q])[:3500])
