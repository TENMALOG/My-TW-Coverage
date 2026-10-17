import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_159.txt',encoding='utf8') if l.strip()]
cache={}
def load(tk):
    if tk not in cache:
        d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
        cache[tk]=(d,pages)
    return cache[tk]
start,end=int(sys.argv[1]),int(sys.argv[2])
for id_ in ids[start:end]:
    tk=id_.split('-AR-')[0]
    d,pages=load(tk)
    f=[x for x in d['facts'] if x['id']==id_][0]
    print('='*70);print(id_,d['company'],f['field'],f['period'],f['attribution'],'p',f['page'])
    print('STMT:',f['statement']);print('EXC:',f['excerpts'])
    p=f['page']
    pg=pages.get(p,'')
    pos=-1
    for e in sorted(f["excerpts"],key=len,reverse=True):
        k=e[:8]
        pos=pg.find(k)
        if pos>=0: break
    if pos<0: print('--EXCERPT NOT FOUND ON PAGE; page head');pos=0
    a=max(0,pos-80)
    print('--PAGE',p,'@',pos);print(pg[a:pos+380])
    if len(pg)-pos<250: print('--NEXT',p+1);print(pages.get(p+1,'')[:300])
