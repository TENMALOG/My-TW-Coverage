import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_133.txt',encoding='utf8') if l.strip()]
rej={
'5490-AR-04':'只列主要業務內容(1)之三項產品，漏掉(2)軟硬體系統整合、技術諮詢及維修與(3)進出口貿易，卻以「主要業務內容為」呈現，縮窄業務範圍',
'5493-AR-04':'「半導體設備材料供應及技術服務」在年報表格中是「自動化設備與震動監測」類別下的產品項目，並非獨立的主要營業類別，層級被改變',
'5493-AR-12':'「三聯自有品牌IoT物聯網監測設備將是一大利基」為公司自我評價，卻以「公司年報揭露」呈現（非自述歸屬），且引文未涵蓋該句',
}
with open('research-site/ops/qa-audit4/out_133.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r=rej.get(i)
        f.write(json.dumps({"id":i,"verdict":"REJECT" if r else "ACCEPT","reason":r or "數字、年度、單位、範圍與引用頁一致"},ensure_ascii=False)+"\n")
print(len(ids))
