import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_153.txt',encoding='utf-8') if l.strip()]
rej={'6202-AR-11':'附註2載明欣宏為「本公司子公司」採權益法評價之被投資公司，陳述省略子公司層級，改變關係範圍'}
with open('research-site/ops/qa-audit4/out_153.jsonl','w',encoding='utf-8') as f:
    for i in ids:
        r={'id':i,'verdict':'REJECT','reason':rej[i]} if i in rej else {'id':i,'verdict':'ACCEPT','reason':'與引用頁面表格及文字相符'}
        f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(ids))
