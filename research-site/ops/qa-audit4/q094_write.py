import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_094.txt') if l.strip()]
rej={'4503-AR-06':'表末列為「營業收入淨額」，聲明卻寫「銷售地區表合計」，分母名稱與原表不符',
'4503-AR-07':'表末列為「營業收入淨額」，聲明卻寫「銷售地區表合計」，分母名稱與原表不符',
'4513-AR-17':'該表註明為「單一企業-母公司福裕」，聲明僅引表題「集團個體」而未載明母公司範圍，易誤導為集團合併人數'}
with open('research-site/ops/qa-audit4/out_094.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r={'id':i,'verdict':'REJECT' if i in rej else 'ACCEPT','reason':rej.get(i,'數字、年度、單位、範圍與引用頁相符')}
        f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(ids))
