import json,sys,re
R='../../../'
ids=[l.strip() for l in open('ids_2.txt',encoding='utf8') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[a:b]:
    t=i.split('-')[0]
    d=json.load(open(f'{R}research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    tp=d['source']['text_path']
    if tp not in cache: cache[tp]=open(R+tp,encoding='utf8').read()
    txt=cache[tp]
    p=f['page']
    print('='*70);print(i,d.get('company'),'field=',f['field'],'period=',f.get('period'),'attr=',f.get('attribution'))
    print('STMT:',f['statement']);print('EXC:',json.dumps(f['excerpts'],ensure_ascii=False))
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pg={int(parts[k]):parts[k+1] for k in range(1,len(parts)-1,2)}
    for q in (p,p+1):
        s=pg.get(q,'')
        if q==p+1:
            s=s[:200]
        else:
            ns=''.join(ch for ch in s if not ch.isspace()); idx=[k for k,ch in enumerate(s) if not ch.isspace()]
            ex=''.join(ch for ch in f['excerpts'][0] if not ch.isspace())
            pos=ns.find(ex[:12]); pos=idx[pos] if pos>=0 else 0
            s=s[max(0,pos-120):pos+560]
        print(f'--- page {q} ---');print(s)
