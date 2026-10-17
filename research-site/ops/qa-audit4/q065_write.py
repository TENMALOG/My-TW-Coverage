import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_065.txt') if l.strip()]
rej={'3354-AR-01':'年報營業項目列有5項（含LED照明產品、兼營再生能源自用發電設備業），陳述僅列前3項，縮窄業務範圍',
'3360-AR-10':'該句出自「零件通路事業」銷售地區段落，陳述寫成公司整體銷售版圖，放寬了範圍'}
with open('research-site/ops/qa-audit4/out_065.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r=rej.get(i)
        f.write(json.dumps({'id':i,'verdict':'REJECT' if r else 'ACCEPT','reason':r or '與引用頁面及表格一致'},ensure_ascii=False)+'\n')
print(len(ids))
