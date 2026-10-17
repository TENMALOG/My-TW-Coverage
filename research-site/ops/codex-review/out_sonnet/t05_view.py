import json,sys,re
job=sys.argv[1]; start=int(sys.argv[2]); end=int(sys.argv[3])
W=int(sys.argv[4]) if len(sys.argv)>4 else 1500
ids=open(f'research-site/ops/codex-review/jobs_sonnet/{job}.txt',encoding='utf8').read().split()
cache={}
def pages(path):
    if path not in cache:
        t=open(path,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        cache[path]={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    return cache[path]
def ns_map(txt):
    ns=[];mp=[]
    for k,c in enumerate(txt):
        if not c.isspace(): ns.append(c);mp.append(k)
    return ''.join(ns),mp
for n,i in enumerate(ids[start:end],start):
    t=i.split('-')[0]
    j=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in j['facts'] if x['id']==i][0]
    print(f"\n##### [{n}] {i} {j['company']} {f['field']} period={f['period']} p{f['page']} attr={f['attribution']}")
    print("STMT:",f['statement'])
    print("EXC:",' | '.join(f['excerpts']))
    pg=pages(j['source']['text_path'])
    if (t,f['page'])==globals().get('last'):
        print('(same page as previous fact)'); continue
    last=(t,f['page'])
    txt=pg.get(f['page'],'')
    ns,mp=ns_map(txt)
    pos=None;missing=False
    for e in f['excerpts']:
        q=ns.find(''.join(e.split())[:10])
        if q>=0:
            if pos is None: pos=mp[q]
        else: missing=True
    if pos is None: pos=0
    a=max(0,pos-250)
    print("--- PAGE ---\n"+('...' if a else '')+txt[a:a+W])
    if missing:
        t2=pg.get(f['page']+1,'')
        print("--- NEXT PAGE ---\n"+t2[:700])
