import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_078.txt',encoding='utf-8') if l.strip()]
want=sys.argv[1]
cache={}
def norm(s): return re.sub(r'[\s\u3000]+','',s)
for i in ids:
    t=i.split('-AR-')[0]
    if t!=want: continue
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8'))
    if t not in cache:
        txt=open(d['source']['text_path'],encoding='utf-8').read()
        cache[t]=dict((int(m.group(1)),m.group(2)) for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)',txt,re.S))
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],'|',f['period'],'| p',f['page'],'|',f['attribution'])
    print('STMT:',f['statement'])
    for p in (f['page'],f['page']+1):
        lines=[re.sub(r'[ \u3000]{2,}',' ',l) for l in cache[t].get(p,'').split('\n')]
        hit=set()
        for e in f['excerpts']:
            k=norm(e)[:12]
            for n,l in enumerate(lines):
                if k and k in norm(l): hit.update(range(max(0,n-4),min(len(lines),n+7)))
        if hit:
            print(f'--- p{p}');print('\n'.join(lines[n] for n in sorted(hit)))
        elif p==f['page']: print('--- NO EXCERPT HIT p',p,'EXC:',f['excerpts'])
