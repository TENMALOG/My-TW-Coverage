import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_107.txt') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2]); W=int(sys.argv[3]) if len(sys.argv)>3 else 1300
cache={}
for i in ids[lo:hi]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=d['source']['text_path']
    if p not in cache:
        txt=open(p,encoding='utf-8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
        cache[p]={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    n=f['page']; s=cache[p].get(n,'')
    pos=-1
    for e in f['excerpts']:
        pos=s.find(e[:12])
        if pos>=0: break
    a=max(0,pos-120) if pos>=0 else 0
    print('='*20,i,d['company'],f['field'],f['period'],'|',f['attribution'],'p',n)
    print('ST:',f['statement'])
    print('EX:',' / '.join(f['excerpts'])[:300])
    print('PG:',s[a:a+W])
