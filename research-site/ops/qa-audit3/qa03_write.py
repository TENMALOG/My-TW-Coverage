import json
ids=open('research-site/ops/qa-audit3/ids_03.txt').read().split()
rej={'1513-AR-01':'範圍縮窄：年報主要業務內容還包括新能源解決方案、停車場、空調、發電機、電表、工程承攬、住宅開發、精密加工等，且電機能源以外業務占比近三成；陳述僅摘第一句且無「等」，改變業務範圍'}
with open('research-site/ops/qa-audit3/out_03.jsonl','w',encoding='utf8') as f:
    for i in ids:
        v={'id':i,'verdict':'REJECT' if i in rej else 'ACCEPT','reason':rej.get(i,'數字、年度、單位、欄位與年報引用頁一致，範圍與歸屬無誤')}
        f.write(json.dumps(v,ensure_ascii=False)+'\n')
