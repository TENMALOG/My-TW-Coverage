import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_029.txt') if l.strip()]
cache={}
NL=chr(10)
def norm(x):
    return re.sub(r'\s+',' ',x)
def win(t,ex):
    t=norm(t)
    for e in sorted(ex,key=len,reverse=True):
        e2=norm(e)
        k=t.find(e2[:14])
        if k>=0 and len(e2)>=6:
            return t[max(0,k-150):k+len(e2)+250]
    return 'NOT FOUND: '+t[:1000]
out=[]
for i in ids:
    tk=i.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
        cache[tk]=(d,pages)
    d,pages=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    p=f['page']
    out.append(f"=== {i} {d['company']} field={f['field']} period={f['period']} attr={f['attribution']} page={p}{NL}STMT: {f['statement']}{NL}EXC: {f['excerpts']}{NL}--- p{p}: {win(pages.get(p,''),f['excerpts'])}{NL}")
open(sys.argv[1],'w',encoding='utf8').write(NL.join(out))
