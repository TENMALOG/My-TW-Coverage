import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_124.txt',encoding='utf8') if l.strip()]
rej={
 '5274-AR-12':'「指標性客戶」為公司自述性評價，卻以「公司年報揭露」呈現為事實，且省略年報所述2024至2025年的時間範圍',
 '5285-AR-110':'「八成以上外銷」屬銷售地區比重數字，陳述未標明年度（period僅為截至年報刊印日），不符須帶年度之要求',
}
with open('research-site/ops/qa-audit4/out_124.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r=rej.get(i)
        f.write(json.dumps({'id':i,'verdict':'REJECT' if r else 'ACCEPT','reason':r or '與引用頁面內容一致，數字、年度、分母及範圍皆相符'},ensure_ascii=False)+'\n')
print(len(ids))
