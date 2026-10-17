import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_152.txt',encoding='utf8') if l.strip()]
rej={'6196-AR-13':'陳述加入「自動化系統整合能力」，但年報該句（第92頁）未載明所指能力，且緊接在高科技設備材料銷售業務項目之後，範圍被改寫。'}
with open('research-site/ops/qa-audit4/out_152.jsonl','w',encoding='utf8') as o:
    for i in ids:
        if i in rej: r={'id':i,'verdict':'REJECT','reason':rej[i]}
        else: r={'id':i,'verdict':'ACCEPT','reason':'與引用頁面內容、數字、年度、欄位及範圍一致'}
        o.write(json.dumps(r,ensure_ascii=False)+'\n')
