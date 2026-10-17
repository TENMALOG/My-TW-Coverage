import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_146.txt') if l.strip()]
rej={'6151-AR-09':'年報僅稱「近年」美元出口銷售占主營業務收入約23%，未指明年度，陳述與期間欄卻掛為截至114年度，營收／銷售地區比例缺明確年度'}
with open('research-site/ops/qa-audit4/out_146.jsonl','w',encoding='utf8') as f:
    for i in ids:
        if i in rej: r={'id':i,'verdict':'REJECT','reason':rej[i]}
        else: r={'id':i,'verdict':'ACCEPT','reason':'與引用頁面一致'}
        f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(ids))
