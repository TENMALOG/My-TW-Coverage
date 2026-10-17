import json,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_109.txt') if l.strip()]
cache={}
def pages(tk):
    if tk not in cache:
        d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        x=re.split(r'\[PDF PAGE (\d+)\]',txt)
        cache[tk]=(d,{int(x[k]):x[k+1] for k in range(1,len(x),2)})
    return cache[tk]
n=lambda s:re.sub(r'\s+','',s)
for tk in sorted(set(i.split('-AR-')[0] for i in ids)):
    d,pg=pages(tk)
    for f in d['facts']:
        if f['id'] in ids:
            p=pg.get(f['page'],'')
            nxt=pg.get(f['page']+1,'')
            for e in f['excerpts']:
                if n(e) not in n(p) and n(e) not in n(p+nxt):
                    print('MISSING',f['id'],e[:60])
print('done')
