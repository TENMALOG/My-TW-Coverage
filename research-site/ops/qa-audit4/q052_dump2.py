import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_052.txt') if l.strip()]
cache={}
def pages(t):
    txt=open(t,encoding='utf8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    return {int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
n=lambda s:re.sub(r'\s+','',s)
lo,hi=int(sys.argv[1]),int(sys.argv[2])
for i in ids[lo:hi]:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    if tk not in cache: cache[tk]=pages(d['source']['text_path'])
    f=[x for x in d['facts'] if x['id']==i][0]
    p=f['page'];pg=cache[tk]
    both=n(pg.get(p,''))+n(pg.get(p+1,''))
    one=n(pg.get(p,''))
    miss=[e for e in f['excerpts'] if n(e) not in both]
    print('==',i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| p',p,'| MISSING' if miss else '', miss if miss else '')
    print('S:',f['statement'])
    print('E:',f['excerpts'])
    # context: header lines around first excerpt line match
    lines=pg.get(p,'').split('\n')
    key=n(f['excerpts'][0])[:12] if f['excerpts'] else ''
    for k,l in enumerate(lines):
        if key and key in n(l):
            print('CTX:',' / '.join(x.strip() for x in lines[max(0,k-4):k+2])); break
