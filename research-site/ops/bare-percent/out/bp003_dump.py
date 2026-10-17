import json,sys
d=json.load(open('ops/bare-percent/jobs_sonnet/bp003.json',encoding='utf8'))
o=open('ops/bare-percent/out/bp003_dump.txt','w',encoding='utf8')
for it in d:
    t=it['id'].split('-')[0]
    j=json.load(open(f'data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in j['facts'] if x['id']==it['id']][0]
    o.write(f"## {it['id']} {j['company']} [{f['field']}] p{f['page']} {f['period']}\nS: {f['statement']}\nA: {f['attribution']}\n")
    for e in f['excerpts']: o.write("  E: "+e.replace('\n',' / ')+"\n")
