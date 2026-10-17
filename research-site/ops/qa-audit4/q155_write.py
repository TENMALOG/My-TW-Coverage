import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_155.txt',encoding='utf8') if l.strip()]
rej={'6215-AR-08':'原文「主要包括」另含智慧產線周邊系統及模組、半導體自動化模組，僅列PCBA製程設備而縮小業務範圍',
'6217-AR-01':'原文主要業務內容列7項（含各種探針、大電流端子等），僅擷取2項並稱「主要從事」，縮小業務範圍'}
with open('research-site/ops/qa-audit4/out_155.jsonl','w',encoding='utf8') as f:
    for i in ids:
        v=('REJECT',rej[i]) if i in rej else ('ACCEPT','與引用頁面相符')
        f.write(json.dumps({'id':i,'verdict':v[0],'reason':v[1]},ensure_ascii=False)+'\n')
print(len(ids))
