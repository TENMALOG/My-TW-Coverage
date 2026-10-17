import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_036.txt',encoding='utf8') if l.strip()]
special={
'2548-AR-10':'數值、年度欄位、占進貨淨額比率與子公司關係皆與表格相符；單位保留未載說明，無誤',
'2605-AR-02':'金額與比重取自114年度欄，分母為年報營業收入總額，與表格相符',
'2546-AR-16':'已註明為計畫目標而非既成事實，與年報相符',
'2596-AR-15':'已註明為年報代號，未當作真實名稱或排名',
'2597-AR-11':'已註明為年報代號且為關係人，數值為114年度欄，相符',
'2603-AR-02':'公司自述排名，歸屬標示正確',
'2605-AR-13':'公司自述評價，歸屬標示正確',
'2548-AR-07':'公司自述研發項目，內容與年報相符',
}
with open('research-site/ops/qa-audit4/out_036.jsonl','w',encoding='utf8') as f:
    for i in ids:
        f.write(json.dumps({'id':i,'verdict':'ACCEPT','reason':special.get(i,'陳述與引用頁面內容、年度欄位、單位及範圍相符')},ensure_ascii=False)+'\n')
print(len(ids))
