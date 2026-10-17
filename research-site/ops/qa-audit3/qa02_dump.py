import json,re,sys
root=''
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_02.txt',encoding='utf8') if l.strip()]
cache={}
def pages(t):
    if t in cache: return cache[t]
    txt=open(root+t,encoding='utf8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    d={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    cache[t]=d;return d
lo,hi=int(sys.argv[1]),int(sys.argv[2])
last=None
for id in ids[lo:hi]:
    tk=id.split('-AR-')[0]
    j=json.load(open(root+f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    if tk!=last:
        print('#'*20,tk,j['company'],j['source']['fy']);last=tk
    f=[x for x in j['facts'] if x['id']==id][0]
    print('---',id,f['field'],'|',f['period'],'| p',f['page'],'|',f['attribution'])
    print('S:',f['statement'])
    print('E:',f['excerpts'])
    pg=pages(j['source']['text_path'])
    p=f['page']
    t=pg.get(p,'')
    # show window around first excerpt
    ex=re.sub(r'\s+','',f['excerpts'][0])[:12]
    flat=t
    # find position by stripping whitespace map
    idxs=[i for i,c in enumerate(t) if not c.isspace()]
    s=''.join(t[i] for i in idxs)
    k=s.find(ex)
    if k<0: print('PAGE-TEXT (excerpt not found on page, first 1500):',t[:1500]);continue
    a=idxs[max(0,k-80)]; b=idxs[min(len(idxs)-1,k+420)]
    print('P:',t[a:b])
