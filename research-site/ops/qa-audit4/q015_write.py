import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_015.txt') if l.strip()]
rej={
'1742-AR-17':'年報表列「A 公司」為匿名代號，陳述未標示為代號，易被當成真實公司名稱',
'1742-AR-18':'年報表列「B 公司」為匿名代號，陳述未標示為代號，易被當成真實公司名稱',
'1742-AR-19':'年報表列「C 公司」為匿名代號，陳述未標示為代號，易被當成真實公司名稱',
'1742-AR-20':'年報表列「E 公司」為匿名代號，陳述未標示為代號，易被當成真實公司名稱',
}
with open('research-site/ops/qa-audit4/out_015.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r={"id":i,"verdict":"REJECT","reason":rej[i]} if i in rej else {"id":i,"verdict":"ACCEPT","reason":"數字、年度、比例與分母、範圍及歸屬皆與引用頁面一致"}
        f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(ids))
