import json,sys,re,collections
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_094.txt') if l.strip()]
by=collections.OrderedDict()
for i in ids: by.setdefault(i.split('-AR-')[0],[]).append(i)
t=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
print(t,d['company'],d['legal_name'],'pages',len(pages))
F={f['id']:f for f in d['facts']}
for i in by[t]:
    f=F[i]
    print('=====',i,f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('S:',f['statement'])
    if '--pages' in sys.argv:
        p=f['page']
        for q in (p,p+1):
            if q in pages:
                print('--- page',q)
                print(re.sub(r'[ \t]+',' ',pages[q].replace(' ',''))[:3000] if '--nosp' in sys.argv else re.sub(r'[ \t]+',' ',pages[q])[:3000])
    else:
        print('E:',f['excerpts'])
