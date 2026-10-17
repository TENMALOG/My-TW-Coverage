import json,sys,re,os
R=os.getcwd()
F='research-site/ops/codex-review/'
job,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
ids=open(F+'jobs_sonnet/'+job+'.txt',encoding='utf8').read().split()
cache={}
def pages(path):
    if path not in cache:
        t=open(path,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        d={}
        for i in range(1,len(parts),2): d[int(parts[i])]=parts[i+1]
        cache[path]=d
    return cache[path]
W=int(sys.argv[4]) if len(sys.argv)>4 else 700
for n,i in enumerate(ids[a:b],a):
    tk=i.split('-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=pages(d['source']['text_path'])
    print(f"=== #{n} {i} [{d['company']}] {f['field']} p{f['page']} | {f['period']} | {f['attribution']}")
    print("S:",f['statement'])
    print("E:",' // '.join(f['excerpts']))
    txt=pg.get(f['page'],'')
    nxt=pg.get(f['page']+1,'')
    full=txt+'\n<<p+1>>'+nxt[:400]
    e=f['excerpts'][0][:25]
    pos=txt.find(e)
    s=max(0,pos-W//3) if pos>=0 else 0
    print("P:",re.sub(r'\n+',' | ',full[s:s+W+len(' '.join(f['excerpts']))]))
