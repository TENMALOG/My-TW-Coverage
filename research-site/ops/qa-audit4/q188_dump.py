import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_188.txt') if l.strip()]
tick=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tick}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
pages={int(m.group(1)):(m.start(),m.end()) for m in re.finditer(r'\[PDF PAGE (\d+)\]',t)}
def pg(n):
    if n not in pages: return '??'
    s=pages[n][0]; nx=pages.get(n+1,(len(t),))[0]
    return t[s:nx]
print(d['company'],d['legal_name'])
shown=set()
for f in d['facts']:
    if f['id'] not in ids: continue
    print('=====',f['id'],f['field'],f['period'],'p',f['page'],f['attribution'])
    print('S:',f['statement'])
    print('E:',f['excerpts'])
    if f['page'] not in shown:
        shown.add(f['page']); print('--PAGE',f['page']); print(pg(f['page'])[:3500])
