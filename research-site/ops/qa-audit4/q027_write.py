import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_027.txt') if l.strip()]
rej={
'2380-AR-22':'年報該句位於「中國大陸」市場段落，陳述僅指中國大陸合作銷售情形，聲明改寫成公司整體印表機業務，擴大範圍',
'2382-AR-05':'引述《財星》500大排名屬未經獨立驗證的評價，attribution 未使用規定的「公司年報自述（未經獨立驗證的排名或評價）」',
'2387-AR-07':'「為其鍵盤主要供應商」屬公司自我評價，attribution 為「公司年報揭露」，應為「公司年報自述（未經獨立驗證的排名或評價）」',
}
with open('research-site/ops/qa-audit4/out_027.jsonl','w',encoding='utf8') as f:
    for i in ids:
        if i in rej: o={'id':i,'verdict':'REJECT','reason':rej[i]}
        else: o={'id':i,'verdict':'ACCEPT','reason':'數字、年度、範圍與引用頁相符'}
        f.write(json.dumps(o,ensure_ascii=False)+'\n')
print(len(ids))
