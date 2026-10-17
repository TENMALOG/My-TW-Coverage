import json
ids=[l.strip() for l in open('ids_30.txt') if l.strip()]
rej={'2916-AR-04':'營收比重「約八成」屬revenue_mix數字，但陳述未載年度，period僅為年報刊印日，缺少年度'}
with open('out_30.jsonl','w',encoding='utf8') as f:
    for i in ids:
        v='REJECT' if i in rej else 'ACCEPT'
        r=rej.get(i,'數字、年度、單位、分母與範圍均與引用頁面一致')
        f.write(json.dumps({'id':i,'verdict':v,'reason':r},ensure_ascii=False)+'\n')
