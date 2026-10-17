import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_003.txt') if l.strip()]
rej={'1339-AR-09':'該表依註1為「昭輝個體資訊」（合計1,526,367仟元，即個體營收淨額），敘述未標明個體範圍，與另一張合併表（1,932,091仟元）易混淆，範圍不明'}
with open('research-site/ops/qa-audit4/out_003.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r=rej.get(i)
        f.write(json.dumps({'id':i,'verdict':'REJECT' if r else 'ACCEPT','reason':r or '與引用頁內容相符，數字、年度、分母與範圍無誤'},ensure_ascii=False)+'\n')
print(len(ids))
