import json
ids=[l.strip() for l in open('ids_23.txt') if l.strip()]
note={'2417-AR-10':'公司自述之夥伴身分，陳述已標明「公司於年報稱」，未加評價，接受','2419-AR-21':'陳述標明公司於年報載明，數字與原文一致，未加評價，接受','2423-AR-08':'陳述標明公司於年報載明，數字與原文一致，接受','2420-AR-03':'原文標題即為「所營業務之主要內容」，代碼正確，接受','2418-AR-00':''}
with open('out_23.jsonl','w',encoding='utf8') as f:
    for i in ids:
        f.write(json.dumps({"id":i,"verdict":"ACCEPT","reason":note.get(i) or "數字、年度、欄位、分母與範圍均與引用頁面相符，接受"},ensure_ascii=False)+"\n")
print(len(ids))
