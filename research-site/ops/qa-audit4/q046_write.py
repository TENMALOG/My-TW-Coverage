import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_046.txt') if l.strip()]
rej={'3028-AR-08':'僅摘錄趨勢段落「主要從事記憶體產品代理及零售」，縮窄業務範圍；同年報他處載明為半導體零組件通路，記憶卡僅占營業比重30.55%'}
with open('research-site/ops/qa-audit4/out_046.jsonl','w',encoding='utf8') as f:
    for i in ids:
        if i in rej: o={"id":i,"verdict":"REJECT","reason":rej[i]}
        else: o={"id":i,"verdict":"ACCEPT","reason":"與引用頁面表格及文字相符，年度、分母、範圍均正確"}
        f.write(json.dumps(o,ensure_ascii=False)+'\n')
