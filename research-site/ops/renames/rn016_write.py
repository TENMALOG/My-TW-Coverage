import json
d=json.load(open('research-site/ops/renames/jobs/rn_016.json',encoding='utf-8'))
out=[]
for e in d:
    r=[];n="hits only about committees, subsidiaries, investees, products or boilerplate; no issuer rename"
    if e['id']=='6578':
        r=[{"former_name":"","new_name":"達邦蛋白生技股份有限公司","date_text":"民國 112 年 10 月 11 日","kind":"chinese","page":129,"excerpt":"10 月 11 日經經濟部核准更名為達邦蛋白生技股份有限公司。"}]
        n="former name not stated in report"
    out.append({"id":e['id'],"renames":r,"note":n})
with open('research-site/ops/renames/out/rn_016.jsonl','w',encoding='utf-8',newline='\n') as f:
    for o in out:f.write(json.dumps(o,ensure_ascii=False)+'\n')
print(len(out))
