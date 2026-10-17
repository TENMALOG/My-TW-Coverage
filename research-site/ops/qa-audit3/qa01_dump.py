import json,re,sys
root='../../../'
ids=[l.strip() for l in open('ids_01.txt',encoding='utf8') if l.strip()]
start,end=int(sys.argv[1]),int(sys.argv[2])
for i in ids[start:end]:
    t=i.split('-AR-')[0]
    d=json.load(open(root+f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=f['page']
    txt=open(root+d['source']['text_path'],encoding='utf8').read()
    pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pm={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
    print('='*60);print(i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| p',p)
    print('STMT:',f['statement'])
    lines=[l for l in pm.get(p,'').split('\n') if l.strip()]
    keys=[e.replace(' ','')[:6] for e in f['excerpts']]
    hit=set()
    for n,l in enumerate(lines):
        ls=l.replace(' ','')
        if any(k and k in ls for k in keys):
            hit.update(range(max(0,n-6),min(len(lines),n+7)))
    if not hit: hit=set(range(min(25,len(lines))))
    print('\n'.join(lines[n] for n in sorted(hit)))
    nx=[l for l in pm.get(p+1,'').split('\n') if l.strip()][:5]
    print('--next:','\n'.join(nx))
