import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_063.txt') if l.strip()]
rej={'3317-AR-05':'「公司產品市場佔有率並不重大」為公司自我評價，但歸因標為「引述第三方資料」，應為公司年報自述（未經獨立驗證的排名或評價）'}
with open('research-site/ops/qa-audit4/out_063.jsonl','w',encoding='utf8') as f:
    for i in ids:
        if i in rej: o={"id":i,"verdict":"REJECT","reason":rej[i]}
        else: o={"id":i,"verdict":"ACCEPT","reason":"已核對引用頁，數字、年度、欄位、範圍與分母均相符"}
        f.write(json.dumps(o,ensure_ascii=False)+"\n")
