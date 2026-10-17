import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_075.txt',encoding='utf8') if l.strip()]
pages={}
def sq(s): return re.sub(r'\s+',' ',s)
for i in ids:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    if tk not in pages:
        t=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        pages[tk]={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    f=[x for x in d['facts'] if x['id']==i][0]
    p=f['page']
    txt=sq(pages[tk].get(p,''))+' ||NEXT|| '+sq(pages[tk].get(p+1,''))
    nums=re.findall(r'\d[\d,]{3,}',f['statement'])
    key=None
    if nums:
        key=nums[0]
    else:
        e=sq(f['excerpts'][-1]); key=e[:10]
    k=txt.find(key)
    print('##',i,'key',key,'pos',k)
    if k<0:
        # try loose
        k2=txt.find(sq(f['excerpts'][0])[:8]); print('  loose',k2); k=max(k2,0)
    print('  ',txt[max(0,k-250):k+350])
