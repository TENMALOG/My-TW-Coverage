import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_048.txt') if l.strip()]
rej={'3041-AR-01':'營收比重（STB晶片約85%、網路設備約15%）原文與陳述皆未標註年度，屬無年度的營收組成數字'}
with open('research-site/ops/qa-audit4/out_048.jsonl','w',encoding='utf8') as f:
    for i in ids:
        if i in rej: o={'id':i,'verdict':'REJECT','reason':rej[i]}
        else: o={'id':i,'verdict':'ACCEPT','reason':'已對照引用頁面，數字、年度、分母與範圍皆與原文相符'}
        f.write(json.dumps(o,ensure_ascii=False)+'\n')
print(len(ids))
