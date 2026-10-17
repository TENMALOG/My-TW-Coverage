import json,sys,re
job=sys.argv[1]
ids=[l.strip() for l in open(f'research-site/ops/codex-review/jobs_sonnet/{job}.txt',encoding='utf8') if l.strip()]
cache={};texts={}
def pages(path):
    if path not in texts:
        t=open(path,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        texts[path]={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    return texts[path]
def flat(s): return re.sub(r'\s*\n\s*','|',s)
for i in ids:
    tk=i.split('-')[0]
    if tk not in cache: cache[tk]=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    d=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=pages(d['source']['text_path'])
    p=f['page']
    print(f"=== {i} [{d['company']}] {f['field']} | {f['period']} | p{p} | {f['attribution']}")
    print("S:",f['statement'])
    print("E:",' ## '.join(f['excerpts']))
    txt=pg.get(p,'')+"<<NEXTPAGE>>"+pg.get(p+1,'')[:1500]
    ks=[txt.find(e[:15]) for e in f['excerpts']]
    ks=[k for k in ks if k>=0] or [0]
    a=max(0,min(ks)-120); b=max(ks)+500
    if b-a>800: b=a+800
    print("CTX:",flat(txt[a:b]))
