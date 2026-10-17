import json
ids=[l.strip() for l in open('ids_15.txt') if l.strip()]
rej={'2114-AR-11':'年報表中的「A 公司」為匿名代號，陳述未標明代號，易被誤讀為實名',
     '2114-AR-13':'年報表中的「E」為匿名供應商代號，陳述寫成「供應商E」未標明代號，易被誤讀為實名'}
with open('out_15.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r=rej.get(i)
        f.write(json.dumps({'id':i,'verdict':'REJECT' if r else 'ACCEPT','reason':r or '數字、年度、單位、範圍與年報引用頁一致'},ensure_ascii=False)+'\n')
