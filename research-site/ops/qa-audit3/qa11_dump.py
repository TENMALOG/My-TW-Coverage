import json,re,sys
root='research-site/'
ids=[l.strip() for l in open(root+'ops/qa-audit3/ids_11.txt') if l.strip()]
start,end=int(sys.argv[1]),int(sys.argv[2])
cache={}
def pages(path):
    if path not in cache:
        t=open(path,encoding='utf-8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        cache[path]={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    return cache[path]
for i in ids[start:end]:
    tk=i.split('-AR-')[0]
    d=json.load(open(root+f'data/company-facts/{tk}.json',encoding='utf-8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=pages(d['source']['text_path'])
    p=f['page']
    print('='*30,i,d['company'])
    print('FIELD',f['field'],'| PERIOD',f['period'],'| ATTR',f['attribution'])
    print('STMT',f['statement'])
    print('EXC',f['excerpts'])
    key=(tk,p)
    if key==globals().get("last"): print("--PAGE",p,"(same as previous)")
    else: print("--PAGE",p); print(pg.get(p,"")[:2200])
    last=key
    if len(sys.argv)>3: print('--PAGE+1'); print(pg.get(p+1,'')[:1500])
