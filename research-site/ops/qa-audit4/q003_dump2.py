import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_003.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2]); W=int(sys.argv[3]) if len(sys.argv)>3 else 700
for i in ids[a:b]:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    t=open(d['source']['text_path'],encoding='utf8').read()
    pg=f['page']
    def page(n):
        m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\]|\Z)'%(n,n+1),t,re.S)
        return m.group(1) if m else ''
    p=re.sub(r'[ \t]+',' ',page(pg)); 
    # locate: last excerpt's first 8 chars (no spaces)
    pos=-1
    for ex in f['excerpts'][::-1]:
        k=re.sub(r'\s+','',ex)
        # find in page ignoring spaces: map
        ps=''.join(c for c in p if not c.isspace()); 
        j=ps.find(k[:12])
        if j>=0:
            # map index back
            cnt=0
            for idx,c in enumerate(p):
                if not c.isspace():
                    if cnt==j: pos=idx;break
                    cnt+=1
            break
    s=max(0,(pos if pos>=0 else 0)-W); 
    print('=====',i,d['company'],f['field'],f['period'],'|',f['attribution'],'p',pg,'found' if pos>=0 else 'NOTFOUND')
    print('STMT:',f['statement']); print('EXC:',f['excerpts'])
    print('--PAGE--'); print(p[s:s+2*W])
