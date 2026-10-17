import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_054.txt') if l.strip()]
cache={}
def load(t):
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        pages=dict((int(m.group(1)),m.group(2)) for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]\n|\Z)',txt,re.S))
        cache[t]=(d,pages)
    return cache[t]
a,b=int(sys.argv[1]),int(sys.argv[2])
for i in ids[a:b]:
    t=i.split('-AR-')[0]
    d,pages=load(t)
    f=[x for x in d['facts'] if x['id']==i][0]
    print('='*30,i,d['company'],f['field'],f['period'],f['attribution'],'p',f['page'])
    print('STMT:',f['statement']);print('EXC:',f['excerpts'])
    p=f['page']
    for q in (p,p+1):
        if q in pages and (q==p or '--next' in sys.argv):
            s=re.sub(r'[ \t]+',' ',pages[q]);s=re.sub(r'\n\s*\n+','\n',s)
            print(f'--- page {q}');
            k=-1
            for e in f['excerpts']:
                e2=re.sub(r'\s+','',e)[:10]
                m=re.search(r'\s*'.join(map(re.escape,e2)),s)
                if m: k=m.start();break
            a0=max(0,k-150) if k>=0 else 0
            print(s[a0:a0+420])
