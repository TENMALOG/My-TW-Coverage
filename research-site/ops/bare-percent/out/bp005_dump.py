import json,sys
d=json.load(open('ops/bare-percent/jobs_sonnet/bp005.json',encoding='utf8'))
out=[]
for x in d:
    t=x['id'].split('-')[0]
    c=json.load(open(f'data/company-facts/{t}.json',encoding='utf8'))
    f=[y for y in c['facts'] if y['id']==x['id']][0]
    out.append(f"## {f['id']} [{f['field']}] p{f['page']} {f['period']} | {f['attribution']}\nS: {f['statement']}\nE: "+" || ".join(f['excerpts']))
open('ops/bare-percent/out/bp005_dump.txt','w',encoding='utf8').write("\n".join(out))
