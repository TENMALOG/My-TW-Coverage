import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_016.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[a:b]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=d['source']['text_path']
    if p not in cache:
        cache[p]=re.split(r'\[PDF PAGE (\d+)\]',open(p,encoding='utf8').read())
    parts=cache[p]
    pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    print('='*80);print(i,d['company'],f['field'],'| period:',f['period'],'| attr:',f['attribution'],'| page',f['page'])
    print('STMT:',f['statement']);print('EXC:',f['excerpts'])
    txt=pages.get(f['page'],'')
    txt=re.sub(r'[ \t]+',' ',txt);txt=re.sub(r'\n\s*\n+','\n',txt)
    print('--PAGE--');
    flat=re.sub(r'\s+','',txt)
    key=re.sub(r'\s+','',f['excerpts'][0])[:12]
    # window on raw text
    m=re.search(r'\s*'.join(map(re.escape,key)),txt)
    pos=m.start() if m else 0
    print(txt[max(0,pos-300):pos+800])
