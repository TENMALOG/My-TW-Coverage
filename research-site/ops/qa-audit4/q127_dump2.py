import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_127.txt') if l.strip()]
tk=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
pages=re.split(r'\[PDF PAGE (\d+)\]\n',t)
pg={int(pages[i]):pages[i+1] for i in range(1,len(pages),2)}
print('COMPANY',d['company'],d['legal_name'],d['source']['fy'])
ns=lambda s:re.sub(r'\s+','',s)
for f in d['facts']:
    if f['id'] not in ids: continue
    print('\n=== ',f['id'],f['field'],'|',f['period'],'|p',f['page'],'|',f['attribution'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    p=f['page']
    for pp in (p,p+1):
        lines=[l for l in pg.get(pp,'').split('\n') if l.strip()]
        hit=set()
        for e in f['excerpts']:
            k=ns(e)
            for key in (k, k[-12:], k[:12]):
                for i,l in enumerate(lines):
                    if len(key)>=4 and key in ns(l):
                        hit.update(range(max(0,i-4),min(len(lines),i+5)))
                if hit: break
        if hit:
            print(f'--- p{pp}')
            last=-2
            for i in sorted(hit):
                if i!=last+1: print('  ...')
                print(lines[i]); last=i
            break
