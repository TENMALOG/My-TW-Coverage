import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_052.txt') if l.strip()]
rej={'3095-AR-01':'「致力於產品品質、技術提升」屬公司自我評價（原文接續「深受國際大廠肯定，顯示產品品質優良」），卻標為「公司年報揭露」，應標示為公司年報自述（未經獨立驗證的排名或評價）'}
with open('research-site/ops/qa-audit4/out_052.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r=rej.get(i)
        f.write(json.dumps({'id':i,'verdict':'REJECT' if r else 'ACCEPT','reason':r or '與引用頁面內容、年度欄位、分母及範圍相符'},ensure_ascii=False)+'\n')
print(len(ids))
