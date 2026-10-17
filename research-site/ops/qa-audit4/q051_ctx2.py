import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_051.txt') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2]); C=int(sys.argv[3]) if len(sys.argv)>3 else 4
cache={}
def pages(tp):
    if tp not in cache:
        t=open(tp,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        cache[tp]={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    return cache[tp]
for i in ids[lo:hi]:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=pages(d['source']['text_path']); p=f['page']
    print('=====',i,f['field'],f['period'],'p',p,'|',f['statement'])
    lines=pg.get(p,'').split('\n')+['--NEXT--']+pg.get(p+1,'').split('\n')[:25]
    toks=set()
    for e in f['excerpts']:
        for t in re.split(r'[\s、，,；;（）()]+',e):
            if len(t)>=2: toks.add(t)
    # prefer rare tokens: numbers & longest
    toks=sorted(toks,key=lambda t:-len(t))[:8]
    hit=set()
    for n,l in enumerate(lines):
        ls=l.replace(' ','')
        if any(t in l or t in ls for t in toks):
            for k in range(max(0,n-C),min(len(lines),n+C+1)): hit.add(k)
    prev=-2
    for k in sorted(hit)[:60]:
        if k!=prev+1: print('  ...')
        print(lines[k]); prev=k
