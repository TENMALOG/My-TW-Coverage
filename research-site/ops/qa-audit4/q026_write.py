import json
rej={
'2359-AR-16':'年報此句為公司自述引述第三方評選的排名，attribution 應為「公司年報自述（未經獨立驗證的排名或評價）」而非「引述第三方資料」',
'2364-AR-01':'只挑所營業務第1、8、9項並略過第2至7項（電腦、主機板、ASIC、遊戲機等），使業務範圍被縮窄',
'2368-AR-02':'營業項目共9項，僅列前兩項卻寫成「包括A及B」，未註明僅為部分，縮窄業務範圍',
'2374-AR-04':'表格列序「1」被寫成「前一名客戶」，年報並未作排名陳述（列序當排名）',
'2374-AR-12':'員工表註明合併主體資訊未揭露（僅本公司單體），陳述卻未標明範圍，易被誤解為公司整體員工數',
}
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_026.txt',encoding='utf8') if l.strip()]
with open('research-site/ops/qa-audit4/out_026.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r={'id':i,'verdict':'REJECT','reason':rej[i]} if i in rej else {'id':i,'verdict':'ACCEPT','reason':'與引用頁面文字及數字相符，範圍與分母明確'}
        f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(ids))
