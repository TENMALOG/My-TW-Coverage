import json,re,sys
ids=open('research-site/ops/qa-audit3/ids_03.txt').read().split()
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[a:b]:
    tk=i.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\n\[PDF PAGE (\d+)\]\n',t)
        pm={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
        cache[tk]=(d,pm)
    d,pm=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('='*80);print(i,d['company'],d['source']['fy'])
    for k in('field','statement','period','attribution','page','excerpts'):print(k,':',f.get(k))
    p=f['page']
    print('--- PAGE',p);
    pt=pm.get(p,'MISSING')
    norm=lambda x:re.sub(r'\s+','',x)
    # locate first excerpt by raw search of first 12 chars
    pos=-1
    for ex in f['excerpts']:
        j=pt.find(ex[:12])
        if j>=0: pos=j;break
    if pos<0: print('[EXCERPT NOT FOUND ON PAGE]'); print(pt[:2000])
    else: print(pt[max(0,pos-150):pos+800])
    print('--- NEXT',p+1);print(pm.get(p+1,'')[:0])
