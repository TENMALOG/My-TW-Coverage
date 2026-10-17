import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_18.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
W=int(sys.argv[3]) if len(sys.argv)>3 else 700
cache={}
for i in ids[a:b]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=d['source']['text_path']
    if p not in cache:
        parts=re.split(r'\[PDF PAGE (\d+)\]',open(p,encoding='utf8').read())
        cache[p]={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    pages=cache[p]; pg=f['page']
    print('='*20,i,d['company'],'|',f['field'],'|',f.get('period'),'|',f['attribution'],'| p',pg)
    print('S:',f['statement'])
    txt=pages.get(pg,'')+'\n<<NEXTPAGE>>\n'+pages.get(pg+1,'')[:1500]
    spans=[]
    for e in f['excerpts']:
        k=e[:14]
        j=txt.find(k)
        if j<0:
            k=e[:6]; j=txt.find(k)
        spans.append((max(0,j-W//3),min(len(txt),j+W)) if j>=0 else None)
        if j<0: print('  [excerpt not found]',e[:40])
    ss=sorted(s for s in spans if s)
    m=[]
    for s in ss:
        if m and s[0]<=m[-1][1]: m[-1]=(m[-1][0],max(m[-1][1],s[1]))
        else: m.append(s)
    for s in m: print('...',txt[s[0]:s[1]].replace('\n\n','\n'))
