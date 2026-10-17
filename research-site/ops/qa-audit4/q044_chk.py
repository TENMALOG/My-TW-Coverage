import json,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_044.txt') if l.strip()]
C={}
def pages(t):
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    txt=open(d['source']['text_path'],encoding='utf8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    return d,{int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
n=lambda s:re.sub(r'\s+','',s)
for i in ids:
    t=i.split('-AR-')[0]
    if t not in C:C[t]=pages(t)
    d,P=C[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=f['page']; body=n(P.get(pg,''))
    nxt=n(P.get(pg+1,''))
    miss=[e for e in f['excerpts'] if n(e) not in body]
    miss2=[e for e in miss if n(e) not in nxt]
    nums=re.findall(r'\d[\d,\.]*\d|\d',f['statement'])
    nm=[x for x in nums if x not in body and x not in nxt and len(x)>2]
    if miss2 or nm: print(i,'MISSING EXC',miss2,'NUMS',nm)
print('done')
