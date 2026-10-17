import json,sys,re
sys.path.insert(0,'research-site/ops/qa-audit4')
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_131.txt') if l.strip()]
cache={}
def load(t):
    if t in cache: return cache[t]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    txt=open(d['source']['text_path'],encoding='utf8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    cache[t]=(d,{int(parts[k]):parts[k+1] for k in range(1,len(parts),2)});return cache[t]
lo,hi,w=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
for i in ids[lo:hi]:
    t=i.split('-AR-')[0];d,pages=load(t)
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=pages.get(f['page'],'')
    print('=====',i,d['company'],'|',f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    # locate first excerpt
    ex=f['excerpts'][0]
    key=re.sub(r'\s','',ex)[:6]
    flat=pg
    pos=-1
    for m in re.finditer(re.escape(ex[:4]),pg):
        pos=m.start();break
    if pos<0: pos=0
    if len(pg)<=w: print(pg)
    else: print(pg[max(0,pos-w//3):pos+w*2//3])
