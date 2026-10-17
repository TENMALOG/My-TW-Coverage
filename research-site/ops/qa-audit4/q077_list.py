import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_077.txt') if l.strip()]
cache={}
def pages(p):
    if p not in cache:
        t=open(p,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        d={}
        for k in range(1,len(parts),2): d[int(parts[k])]=parts[k+1]
        cache[p]=d
    return cache[p]
n=lambda s:re.sub(r'\s+','',s)
for i in ids[int(sys.argv[1]):int(sys.argv[2])]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=pages(d['source']['text_path'])
    print('==',i,d['company'],f['field'],f['period'],'p',f['page'],'|',f['attribution'])
    print(' S:',f['statement'])
    for e in f['excerpts']:
        fp=[k for k,v in pg.items() if n(e) in n(v)]
        print('  E:',e[:160].replace('\n',' / '),'->',fp)
