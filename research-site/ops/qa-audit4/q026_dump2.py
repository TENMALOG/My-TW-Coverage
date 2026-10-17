import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_026.txt') if l.strip()]
start,end=int(sys.argv[1]),int(sys.argv[2]); W=int(sys.argv[3])
cache={}
for i in ids[start:end]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    if t not in cache:
        txt=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',txt); cache[t]={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    pages=cache[t]; p=f['page']; pt=pages.get(p,'')
    print('='*20,i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| p',p)
    print('STMT:',f['statement'])
    # window around first excerpt's first 8 chars
    pos=-1
    for e in f['excerpts']:
        k=re.sub(r'\s+','',e)[:6]
        flat=re.sub(r'\s+','',pt)
        m=flat.find(k)
        if m>=0: pos=m;break
    flat=re.sub(r'[ \t]+',' ',pt)
    # find in non-flattened: try raw search of first 6 non-space chars via regex
    k=re.sub(r'\s+','',f['excerpts'][0])[:6]
    rx=r'\s*'.join(map(re.escape,k))
    m=re.search(rx,pt)
    if m:
        s=max(0,m.start()-W//3); print(pt[s:s+W])
    else:
        print('[excerpt not found, page head]');print(pt[:W])
