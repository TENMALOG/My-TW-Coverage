import json
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_25.txt') if l.strip()]
rej={'2458-AR-12':'表中「3」為列序號，被寫成「第3順位」，把列號當成排名；且該列114年佔比9.72%並未達10%門檻'}
with open('research-site/ops/qa-audit3/out_25.jsonl','w',encoding='utf8') as f:
    for i in ids:
        if i in rej: o={'id':i,'verdict':'REJECT','reason':rej[i]}
        else: o={'id':i,'verdict':'ACCEPT','reason':'數字、年度、單位、欄位、分母與範圍均與引用頁相符'}
        f.write(json.dumps(o,ensure_ascii=False)+'\n')
print(len(ids))
