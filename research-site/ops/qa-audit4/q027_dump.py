import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_027.txt') if l.strip()]
start,end=int(sys.argv[1]),int(sys.argv[2]); W=int(sys.argv[3]) if len(sys.argv)>3 else 700
cache={}
def pages(t,d):
    if t not in cache:
        txt=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]\n',txt)
        m={}
        for k in range(1,len(parts),2): m[int(parts[k])]=parts[k+1]
        cache[t]=m
    return cache[t]
for i in ids[start:end]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    pg=pages(t,d)
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'])
    print('FIELD',f['field'],'| PERIOD',f['period'],'| ATTR',f['attribution'],'| PAGE',f['page'])
    print('STMT',f['statement'])
    p=f['page']; s=pg.get(p,'')
    ex=f['excerpts'][0]
    key=re.sub(r'\s','',ex)[:8]
    # find position ignoring whitespace
    flat=''; idx=[]
    for n,c in enumerate(s):
        if not c.isspace(): flat+=c; idx.append(n)
    pos=flat.find(key)
    if pos<0: print('!!KEY NOT FOUND; page head:'); print(s[:W*2])
    else:
        a=idx[pos]; print('CTX>>',s[max(0,a-W//3):a+W])
