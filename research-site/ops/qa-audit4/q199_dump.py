import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_199.txt') if l.strip()]
tick=sys.argv[1]; W=int(sys.argv[2]) if len(sys.argv)>2 else 10
d=json.load(open(f'research-site/data/company-facts/{tick}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
pages=dict((int(m.group(1)),m.start()) for m in re.finditer(r'\[PDF PAGE (\d+)\]',txt))
def page(n):
    s=pages[n]; e=pages.get(n+1,len(txt)); return txt[s:e]
n=lambda s:re.sub(r'\s+','',s)
print('##',tick,d['company'])
for f in d['facts']:
    if f['id'] not in ids: continue
    print('\n=====',f['id'],f['field'],f.get('period'),'| attr:',f.get('attribution'),'| p',f['page'])
    print('STMT:',f['statement'])
    lines=re.sub(r'[ \t]+',' ',page(f['page'])).split('\n')
    nl=[n(l) for l in lines]
    hit=None
    for ex in f['excerpts']:
        k=n(ex)
        for i,l in enumerate(nl):
            if len(l)>=4 and (k[:12] in l or l in k and len(l)>=8): hit=i;break
        if hit is not None:break
    if hit is None: print('NO HIT; EXC',f['excerpts']); hit=0
    print('\n'.join(lines[max(0,hit-W):hit+W+1]))
