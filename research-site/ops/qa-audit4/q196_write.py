import json
ids=[l.strip() for l in open('ids_196.txt',encoding='utf8') if l.strip()]
rej={'6887-AR-16':'market_position 項目，「臺灣僅四家企業獲核可」屬公司自述的競爭地位，attribution 卻標為公司年報揭露，應標公司年報自述（未經獨立驗證的排名或評價）'}
with open('out_196.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r=rej.get(i)
        f.write(json.dumps({'id':i,'verdict':'REJECT' if r else 'ACCEPT','reason':r or '與引用頁內容相符'},ensure_ascii=False)+'\n')
print(len(ids))
