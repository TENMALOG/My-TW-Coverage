import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_020.txt') if l.strip()]
rej={'2106-AR-05':'「全球前31大」為公司引述第三方排名並加「穩居」等自評，屬排名陳述，但attribution為「公司年報引述第三方資料」，應為「公司年報自述（未經獨立驗證的排名或評價）」'}
with open('research-site/ops/qa-audit4/out_020.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r={"id":i,"verdict":"REJECT" if i in rej else "ACCEPT","reason":rej.get(i,"數字、年度、分母與範圍均與引用頁面相符")}
        f.write(json.dumps(r,ensure_ascii=False)+"\n")
print(len(ids))
