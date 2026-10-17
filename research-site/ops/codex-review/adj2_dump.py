import json,io
R='research-site/'
d=json.load(open(R+'ops/codex-review/adj_2.json',encoding='utf8'))
out=io.open(R+'ops/codex-review/adj2_dump.txt','w',encoding='utf8')
cache={}
for it in d:
    t=it['id'].split('-')[0]
    if t not in cache: cache[t]=json.load(open(R+'data/company-facts/%s.json'%t,encoding='utf8'))
    c=cache[t]
    f=[x for x in c['facts'] if x['id']==it['id']][0]
    out.write('=== %s [%s] %s\n'%(it['id'],it['source'],c['company']))
    out.write('REVIEWER: %s\n'%it['reviewer_reason'])
    out.write('STMT: %s\nPERIOD: %s PAGE: %s ATTR: %s FIELD: %s\n'%(f['statement'],f['period'],f['page'],f['attribution'],f['field']))
    for e in f['excerpts']: out.write('  EX: %s\n'%e)
