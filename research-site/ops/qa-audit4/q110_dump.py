import json,re,sys,io
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_110.txt',encoding='utf8') if l.strip()]
out=io.open('research-site/ops/qa-audit4/q110_dump.txt','w',encoding='utf8')
cache={}
for i in ids:
    t=i.split('-AR-')[0]
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        cache[t]=(d,txt)
    d,txt=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    out.write('=====%s %s %s p%s attr=%s\nSTMT: %s\nPERIOD: %s\nEXC: %s\n'%(i,d['company'],f['field'],f['page'],f['attribution'],f['statement'],f['period'],f['excerpts']))
out.close()
t=cache['4904'][1]
print(len(t)); print(repr(t[:300])); print(re.findall(r'.{0,20}(?:\f|<<<|=== ?Page|\[Page).{0,30}',t)[:5])
