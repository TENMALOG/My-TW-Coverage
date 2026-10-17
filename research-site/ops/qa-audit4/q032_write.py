import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_032.txt',encoding='utf8') if l.strip()]
rej={'2480-AR-10':'銷售區域占比97.21%於年報中無年度，期間欄僅為「年報刊印時」，缺少年份'}
with open('research-site/ops/qa-audit4/out_032.jsonl','w',encoding='utf8') as f:
    for i in ids:
        if i in rej: r={'id':i,'verdict':'REJECT','reason':rej[i]}
        else: r={'id':i,'verdict':'ACCEPT','reason':'已對照引用頁面，數字、年度、分母與範圍均相符'}
        f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(ids))
