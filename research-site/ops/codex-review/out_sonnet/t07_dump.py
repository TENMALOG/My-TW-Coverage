import sys,json,re,os
R=os.path.abspath('../../..')
job=sys.argv[1]; W=int(sys.argv[2]) if len(sys.argv)>2 else 4
ids=[l.strip() for l in open(f'jobs_sonnet/{job}.txt',encoding='utf8') if l.strip()]
cache={}
seen=set()
for i in ids:
    t=i.split('-')[0]
    if t not in cache:
        d=json.load(open(f'{R}/research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(f"{R}/{d['source']['text_path']}",encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
        pg={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
        cache[t]=(d,pg)
    d,pg=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],'|',f['field'],'|',f['period'],'| p',f['page'],'|',f['attribution'])
    print('S:',f['statement'])
    print('E:',' // '.join(f['excerpts']))
    lines=pg.get(f['page'],'').split('\n')
    key=f['excerpts'][0]
    idx=[k for k,l in enumerate(lines) if key[:12] in l]
    if not idx:
        idx=[k for k,l in enumerate(lines) if any(e[:8] in l for e in f['excerpts'])]
    full=(not idx) or any(w in f['field'] for w in ('major','employee','customer','supplier','market','share'))
    if full and (t,f['page']) in seen:
        print('P: (same page as earlier full print above)')
    elif full:
        seen.add((t,f['page']))
        print('P(full):',re.sub(r'\n\s*\n+','\n',pg.get(f['page'],''))[:3800])
    else:
        a=max(0,idx[0]-W); b=idx[0]+W+len(f['excerpts'])+3
        print('P:','\n   '.join(l[:200] for l in lines[a:b]))
