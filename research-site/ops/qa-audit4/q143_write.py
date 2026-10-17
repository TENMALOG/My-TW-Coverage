import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_143.txt',encoding='utf8') if l.strip()]
rej={'6124-AR-119':'「達到全球市場龍頭」屬公司自我期許／評價，歸屬卻標為公司年報揭露，應為公司年報自述（未經獨立驗證的排名或評價）'}
with open('research-site/ops/qa-audit4/out_143.jsonl','w',encoding='utf8') as f:
    for i in ids:
        if i in rej: r={'id':i,'verdict':'REJECT','reason':rej[i]}
        else: r={'id':i,'verdict':'ACCEPT','reason':'與引用頁面內容、欄位年度及分母相符'}
        f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(ids))
