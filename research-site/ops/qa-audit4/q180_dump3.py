import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_180.txt') if l.strip()]
sel=sys.argv[1:]
B=int(sel[0]);A=int(sel[1]);sel=sel[2:]
cache={}
def pages(path):
    if path not in cache:
        t=open(path,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        cache[path]={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    return cache[path]
for i in sel:
    i=[x for x in ids if x==i or x.endswith('-'+i) ][0] if i not in ids else i
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=pages(d['source']['text_path']); p=f['page']
    txt=pg.get(p,'')
    ns=re.sub(r'\s','',txt)
    m=[k for k,c in enumerate(txt) if not c.isspace()]
    print('=====',i,f['field'],f['period'],'|',f['statement'])
    print('EXC',f['excerpts'])
    for e in f['excerpts'][-1:]:
        e=re.sub(r'\s','',e); pos=ns.find(e)
        if pos>=0:
            o=m[pos]; print(re.sub(r'\n\s*\n+','\n',txt[max(0,o-B):o+A]))
        else: print('NOTFOUND')
