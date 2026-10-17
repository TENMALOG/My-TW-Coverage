import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_037.txt') if l.strip()]
cache={}
def pages(path):
    if path not in cache:
        t=open(path,encoding='utf8').read()
        parts=re.split(r'\n?\[PDF PAGE (\d+)\]\n',t)
        cache[path]={int(parts[i]):parts[i+1] for i in range(1,len(parts)-1,2)}
    return cache[path]
last=None
lo,hi=int(sys.argv[1]),int(sys.argv[2])
for i in ids[lo:hi]:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=pages(d['source']['text_path'])
    print('='*80);print(i,d['company'],f['field'],f['period'],f['attribution'],'p',f['page'])
    print('STMT:',f['statement']);print('EXC:',f['excerpts'])
    pg=f['page']
    txt=p.get(pg,'')
    n=re.sub(r'\s+','',txt)
    pos=-1
    for e in f['excerpts']:
        k=txt.find(e[:12])
        if k>=0: pos=k;break
    if pos<0: pos=0; print('!!EXCERPT NOT FOUND')
    key=(f['ticker'] if 'ticker' in f else tk,pg)
    if last==key: print('(same page as previous)')
    else:
        print('--PAGE',pg);print(txt if len(txt)<2600 else txt[max(0,pos-600):pos+1600])
    last=key
