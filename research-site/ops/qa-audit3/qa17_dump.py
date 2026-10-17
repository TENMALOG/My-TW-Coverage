import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_17.txt') if l.strip()]
cache={}
def pages(path):
    if path not in cache:
        t=open(path,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]\n',t)
        cache[path]={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    return cache[path]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
full = len(sys.argv)>3
for i in ids[lo:hi]:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=pages(d['source']['text_path'])
    p=f['page']
    print('='*80);print(i,d['company'],'FY',d['source']['fy'])
    print('field:',f['field'],'| period:',f['period'],'| attr:',f['attribution'],'| page',p)
    print('STATEMENT:',f['statement'])
    print('EXCERPTS:',f['excerpts'])
    txt=pg.get(p,'')
    ex=f['excerpts']
    print('--- PAGE',p,'---')
    print(txt[:3500] if not full else txt)
    if len(sys.argv)>3 or True:
        n=pg.get(p+1,'')
        print('--- NEXT (head) ---');print(n[:1200])
