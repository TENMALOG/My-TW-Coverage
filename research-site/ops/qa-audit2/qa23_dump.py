import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit2/ids_3.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[a:b]:
    t=i.split('-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=d['source']['text_path']
    if p not in cache: cache[p]=open(p,encoding='utf8').read()
    txt=cache[p]
    pg=f['page']
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pages={int(parts[k]):parts[k+1] for k in range(1,len(parts)-1,2)}
    print('='*20,i,d['company'])
    print('STMT:',f['statement'],'|',f['period'],'|p',pg,'|',f['attribution'])
    print('EXC:',f['excerpts'])
    W=int(sys.argv[3])
    for q in (pg,pg+1):
        s=pages.get(q,'')
        if q==pg:
            k=-1
            for e in f['excerpts']:
                k=s.find(e[:12])
                if k>=0: break
            lo=max(0,k-W//2) if k>=0 else 0
            print(f'--- page {q} ({len(s)}) from {lo}'); print(s[lo:lo+W])
        else:
            print(f'--- page {q} head'); print(s[:W//4])
