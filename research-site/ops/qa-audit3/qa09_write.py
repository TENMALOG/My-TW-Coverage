import json
ids=[l.strip() for l in open('ids_09.txt',encoding='utf-8') if l.strip()]
rej={'1710-AR-15':'年報原句為「液氨：東聯林園廠由台灣肥料公司供應，2026年第一季東聯部分由國外進口」，陳述截去2026年第一季部分進口的但書，變成無條件供應，範圍被改寫（部分句子）。'}
with open('out_09.jsonl','w',encoding='utf-8') as o:
    for i in ids:
        r={'id':i,'verdict':'REJECT' if i in rej else 'ACCEPT','reason':rej.get(i,'與引用頁面數字、年度、單位、欄位、範圍相符')}
        o.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(ids))
