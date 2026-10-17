import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_17.txt') if l.strip()]
cache={}
def pages(path):
    if path not in cache:
        t=open(path,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]\n',t)
        cache[path]={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    return cache[path]
ns=lambda s:re.sub(r'\s+','',s)
lo,hi=int(sys.argv[1]),int(sys.argv[2]); ctx=int(sys.argv[3]) if len(sys.argv)>3 else 4
for i in ids[lo:hi]:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=pages(d['source']['text_path'])
    p=f['page']
    print('='*70);print(i,d['company'],'|',f['field'],'|',f['period'],'|',f['attribution'],'| p',p)
    print('S:',f['statement'])
    print('E:',f['excerpts'])
    for q in (p,):
        lines=pg.get(q,'').split('\n')
        keys=set()
        for e in f['excerpts']:
            for w in re.findall(r'[\d,\.]{3,}|[\u4e00-\u9fffA-Za-z]{3,}',e): keys.add(ns(w))
        hit=set()
        for n,l in enumerate(lines):
            L=ns(l)
            if any(k in L for k in keys if len(k)>=3):
                hit.update(range(max(0,n-ctx),min(len(lines),n+ctx+1)))
        if q==p+1 and len(hit)>0 and False: pass
        print(f'--- p{q} ({len(hit)} lines)')
        for n in sorted(hit)[:28]: print(lines[n])
