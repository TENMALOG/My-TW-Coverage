import json,sys,re,collections
job=sys.argv[1]
ids=[l.strip() for l in open(f'research-site/ops/codex-review/jobs_sonnet/{job}.txt',encoding='utf8') if l.strip()]
by=collections.OrderedDict()
for i in ids: by.setdefault(i.split('-')[0],[]).append(i)
for t,l in by.items():
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    txt=open(d['source']['text_path'],encoding='utf8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pg={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    fm={f['id']:f for f in d['facts']}
    print('=====',t,d['company'])
    shown=set()
    for i in l:
        f=fm[i]; p=f['page']
        print('##',i,f['field'],'|',f['statement'],'|',f['period'],'| p',p,'|',f['attribution'])
        print('  EX:',' // '.join(f['excerpts']))
        need=[q for q in (p,p+1)]
        cur=pg.get(p,'')
        norm=lambda x:re.sub(r'\s+','',x)
        allin=all(norm(e) in norm(cur) for e in f['excerpts'])
        for q in ((p,) if allin else (p,p+1)):
            if q not in shown and q in pg:
                shown.add(q); print(f'--- PAGE {q}'); print(re.sub(r'\n\s*\n+','\n',pg[q])[:3500])
