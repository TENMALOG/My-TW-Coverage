import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_061.txt') if l.strip()]
rej={'3297-AR-09':'排名（名列前50大）為公司年報自述，屬未經獨立驗證的排名，attribution 應為「公司年報自述（未經獨立驗證的排名或評價）」，不可標為引述第三方資料'}
with open('research-site/ops/qa-audit4/out_061.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r={'id':i,'verdict':'REJECT' if i in rej else 'ACCEPT','reason':rej.get(i,'數字、年度、分母與範圍均與引用頁面一致')}
        f.write(json.dumps(r,ensure_ascii=False)+'\n')
