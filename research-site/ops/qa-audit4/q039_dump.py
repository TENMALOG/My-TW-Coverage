import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_039.txt') if l.strip()]
want=sys.argv[1:]
cache={}
def pages_of(t,path):
    if t not in cache:
        txt=open(path,encoding='utf8').read()
        parts=re.split(r'\n?\[PDF PAGE (\d+)\]\n',txt)
        cache[t]={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    return cache[t]
for i in ids:
    t=i.split('-AR-')[0]
    if want and t not in want: continue
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    P=pages_of(t,d['source']['text_path'])
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],'fy',d['source']['fy'])
    print('FIELD',f['field'],'| PERIOD',f['period'],'| ATTR',f['attribution'],'| PAGE',f['page'])
    print('STMT',f['statement'])
    p=f['page']
    for pp in (p,p+1):
        lines=P.get(pp,'').split('\n')
        hit=set()
        for ex in f['excerpts']:
            for part in ex.split('\n'):
                key=part.strip()[:10]
                if len(key)<4: continue
                for k,l in enumerate(lines):
                    if key in l: hit.update(range(max(0,k-3),min(len(lines),k+4)))
        if hit:
            print('--page',pp)
            print('\n'.join(lines[k] for k in sorted(hit)))
        elif pp==p: print('--page',pp,'NOHIT; first 800:',P.get(pp,'')[:800])
