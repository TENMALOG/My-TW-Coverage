import json,io
d=json.load(open('ops/bare-percent/jobs_sonnet/bp015.json',encoding='utf8'))
cache={}
o=io.open('ops/bare-percent/out/bp015_dump.txt','w',encoding='utf8')
for i in d:
    t=i['id'].split('-')[0]
    if t not in cache: cache[t]=json.load(open('data/company-facts/%s.json'%t,encoding='utf8'))
    f=[a for a in cache[t]['facts'] if a['id']==i['id']][0]
    o.write('## %s [%s] p%s %s | %s\n  S: %s\n  X: %s\n'%(i['id'],f['field'],f['page'],f['period'],f['attribution'],f['statement'],' // '.join(f['excerpts'])))
