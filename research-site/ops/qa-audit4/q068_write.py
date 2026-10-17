import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_068.txt') if l.strip()]
rej={'3441-AR-05':'「我國僅有本公司及台灣小原二家」為公司對市場結構的自我陳述，屬競爭地位評價，歸因應為「公司年報自述（未經獨立驗證的排名或評價）」，現標為「公司年報揭露」'}
with open('research-site/ops/qa-audit4/out_068.jsonl','w',encoding='utf-8') as f:
    for i in ids:
        r={'id':i,'verdict':'REJECT' if i in rej else 'ACCEPT','reason':rej.get(i,'數字、年度、分母、範圍與引用頁相符')}
        f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(ids))
