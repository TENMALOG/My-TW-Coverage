import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_011.txt') if l.strip()]
tk=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf-8'))
txt=open(d['source']['text_path'],encoding='utf-8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
def clean(s): return '\n'.join(re.sub(r'[ \u3000]+',' ',l).strip() for l in s.split('\n') if l.strip())
mine=[i for i in ids if i.startswith(tk+'-')]
print('##',tk,d['company'],d['source']['fy'])
seen=[]
for f in d['facts']:
    if f['id'] in mine:
        print('=====',f['id'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
        print('STMT:',f['statement'])
        print('EXC:',f['excerpts'])
        if f['page'] not in seen: seen.append(f['page'])
for p in seen:
    print('--- PAGE',p); print(clean(pages.get(p,''))[:2200])
