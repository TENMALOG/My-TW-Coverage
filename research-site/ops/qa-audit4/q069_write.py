import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_069.txt') if l.strip()]
rej={
'3450-AR-15':'報表中的「AAAA 公司」為匿名代號，陳述未標明為代號（如「某客戶（代號）」），讀來像真實公司名',
'3450-AR-16':'同上，「AAAA 公司」為匿名代號卻當成公司名呈現',
'3450-AR-17':'「AAO公司」為匿名代號，陳述未標明為代號，易被當成真實公司名',
'3450-AR-18':'「AO 公司」為匿名代號，陳述未標明為代號，易被當成真實公司名',
'3450-AR-19':'「AP公司」為匿名代號，陳述未標明為代號，易被當成真實公司名',
'3450-AR-21':'「甲公司/乙公司/丙公司」為匿名代號，陳述未標明，易被當成真實公司名',
'3450-AR-22':'「A公司」為匿名代號，陳述未標明為代號，易被當成真實公司名',
}
with open('research-site/ops/qa-audit4/out_069.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r=rej.get(i)
        f.write(json.dumps({'id':i,'verdict':'REJECT' if r else 'ACCEPT','reason':r or '數字、年度、分母與範圍均與引用頁面一致'},ensure_ascii=False)+'\n')
print(len(ids),len(rej))
