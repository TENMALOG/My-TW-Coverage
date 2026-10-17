import json,io
d=json.load(open('ops/bare-percent/jobs_sonnet/bp024.json',encoding='utf8'))
out=io.open('ops/bare-percent/out/bp024_dump.txt','w',encoding='utf8')
cache={}
for it in d:
    t=it['id'].split('-')[0]
    if t not in cache: cache[t]=json.load(open(f'data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in cache[t]['facts'] if x['id']==it['id']]
    if not f: out.write(it['id']+' MISSING\n'); continue
    f=f[0]
    out.write(f"## {it['id']} p{f['page']} [{f['period']}] [{f['attribution']}]\nR: {it['reviewer_reason']}\nS: {f['statement']}\n")
    for e in f['excerpts']: out.write("  E: "+e.replace('\n',' / ')+"\n")
