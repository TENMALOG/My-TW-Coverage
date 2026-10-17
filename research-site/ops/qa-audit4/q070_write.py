import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_070.txt',encoding='utf8') if l.strip()]
rej={'3483-AR-09':'年報該段標題為「熱散產業主要原料的供應狀況」，屬產業一般性描述（「通常採購自」），並非公司自身原料或供應來源，陳述擴大範圍',
'3483-AR-10':'年報該段為熱散產業一般性原料描述，非公司自身導熱管原料，陳述範圍被改為公司事實'}
with open('research-site/ops/qa-audit4/out_070.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r=rej.get(i)
        f.write(json.dumps({'id':i,'verdict':'REJECT' if r else 'ACCEPT','reason':r or '與引用頁內容相符，數字、年度、分母及範圍皆正確'},ensure_ascii=False)+'\n')
print(len(ids))
