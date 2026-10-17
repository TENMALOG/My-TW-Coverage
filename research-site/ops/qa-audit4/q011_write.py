import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_011.txt') if l.strip()]
rej={'1582-AR-04':'營收比重（液晶電視底座約占10%）未標示年度，屬產業章節概述，不符合須有年份之規定'}
with open('research-site/ops/qa-audit4/out_011.jsonl','w',encoding='utf-8') as f:
    for i in ids:
        r=rej.get(i)
        f.write(json.dumps({'id':i,'verdict':'REJECT' if r else 'ACCEPT','reason':r or '數字、年度、單位、範圍與引用頁相符；自述類已標示自述歸屬'},ensure_ascii=False)+'\n')
