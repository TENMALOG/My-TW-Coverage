import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_145.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
W=int(sys.argv[3]) if len(sys.argv)>3 else 700
cache={}
def pages(path):
    if path not in cache:
        t=open(path,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        cache[path]={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    return cache[path]
for i in ids[a:b]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=pages(d['source']['text_path']); p=f['page']
    txt=pg.get(p,'')
    ns=re.sub(r'\s','',txt)
    found=[re.sub(r'\s','',e) in ns for e in f['excerpts']]
    print('=====',i,f['field'],f['period'],'|',f['statement'])
    print('found',found)
    # locate last excerpt start via char mapping
    m=[k for k,c in enumerate(txt) if not c.isspace()]
    e=re.sub(r'\s','',f['excerpts'][0]); pos=ns.find(e)
    if pos>=0:
        o=m[pos]
        print(re.sub(r'\n\s*\n+','\n',txt[max(0,o-250):o+W]))
