import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_122.txt') if l.strip()]
cache={}
def pages(path):
    if path in cache: return cache[path]
    raw=open(path,'rb').read()
    try: t=raw.decode('utf8')
    except Exception: t=raw.decode('cp950',errors='replace')
    parts=re.split(r'\[PDF PAGE (\d+)\]',t)
    pg={int(parts[i]):parts[i+1] for i in range(1,len(parts)-1,2)}
    cache[path]=pg; return pg
norm=lambda x:re.sub(r'\s+','',x)
want=sys.argv[1:]
for i in ids:
    if want and not any(i==w for w in want): continue
    tk=i.split('-AR-')[0]
    d=json.load(open('research-site/data/company-facts/%s.json'%tk,encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],f['field'],'| period:',f['period'],'| attr:',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    pg=pages(d['source']['text_path'])
    txt=pg.get(f['page'],'')+'\n<<NEXTPAGE>>\n'+pg.get(f['page']+1,'')
    lines=txt.split('\n')
    keep=set()
    for j,l in enumerate(lines):
        nl=norm(l)
        if len(nl)>3 and any(nl in norm(e) or norm(e) in nl for e in f['excerpts']):
            keep.update(range(max(0,j-4),min(len(lines),j+5)))
    if not keep: keep=set(range(min(25,len(lines))))
    print('CTX:'); print('\n'.join(lines[j] for j in sorted(keep)))
