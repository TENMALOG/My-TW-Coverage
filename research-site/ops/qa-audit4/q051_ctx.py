import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_051.txt') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
cache={}
def pages(tp):
    if tp not in cache:
        t=open(tp,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        cache[tp]={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    return cache[tp]
seen=set()
for i in ids[lo:hi]:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=pages(d['source']['text_path'])
    p=f['page']
    print('=====',i,f['field'],'p',p,'|',f['statement'])
    if (tk,p) in seen: 
        print('(page already shown)'); continue
    seen.add((tk,p))
    # printed page numbering offset unknown: show page text
    print(pg.get(p,'')[:3500])
    print('--next--'); print(pg.get(p+1,'')[:1500])
