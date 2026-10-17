import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_026.txt') if l.strip()]
start,end=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[start:end]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    if t not in cache:
        txt=open(d['source']['text_path'],encoding='utf8').read()
        cache[t]=re.split(r'\[PDF PAGE (\d+)\]',txt)
    parts=cache[t]; pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    p=f['page']
    print('='*30,i,d['company'],f['field'],f['period'],f['attribution'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    print('--- page',p); print(pages.get(p,'')[:int(sys.argv[3]) if len(sys.argv)>3 else 2500])
