import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_023.txt') if l.strip()]
start,end=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[start:end]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    if t not in cache:
        txt=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
        cache[t]={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    pages=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    p=f['page']
    print('='*20,i,d['company'],'|',f['field'],'|',f['period'],'|',f['attribution'],'| p',p)
    print('STMT',f['statement'])
    print('EXC',f['excerpts'])
    pt=pages.get(p,'')+'\n<<NEXTPAGE>>\n'+pages.get(p+1,'')
    flat=pt
    # find first excerpt anchor
    anchor=None
    for e in f['excerpts']:
        k=e[:12]
        j=flat.find(k)
        if j>=0: anchor=j;break
    if anchor is None: print('!!ANCHOR NOT FOUND'); print(flat[:1200]); continue
    print('CTX:',flat[max(0,anchor-80):anchor+380])
