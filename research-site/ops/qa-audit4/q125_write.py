import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_125.txt',encoding='utf8') if l.strip()]
rej={'5289-AR-18':'「丑公司」為年報匿名代號，卻被當成供應商名稱列出，未標明為代號',
'5291-AR-06':'市佔率偏低為公司自我評價，卻以「公司年報揭露」呈現，attribution 應為公司年報自述（未經獨立驗證的排名或評價），且語句截去「不具任何影響力」',
'5291-AR-08':'「占比最高」為年報未做的排名推論，僅是依表列數值或列序推得'}
with open('research-site/ops/qa-audit4/out_125.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r={'id':i,'verdict':'REJECT' if i in rej else 'ACCEPT','reason':rej.get(i,'數字、年度、單位與年報引用頁一致，範圍與歸屬無誤')}
        f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(ids))
