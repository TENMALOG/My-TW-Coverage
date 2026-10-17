import json
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_18.txt') if l.strip()]
rej={
'2250-AR-15':'年報自述「主要供應商」屬公司自我評價，歸屬標示應為「公司年報自述（未經獨立驗證的排名或評價）」，現為「公司年報揭露」',
'2250-AR-18':'「供應狀況為良好」為公司自我評價，卻以「公司年報揭露」呈現，應標示「公司年報自述（未經獨立驗證的排名或評價）」',
}
with open('research-site/ops/qa-audit3/out_18.jsonl','w',encoding='utf8') as f:
    for i in ids:
        v='REJECT' if i in rej else 'ACCEPT'
        r=rej.get(i,'數字、年度、單位、分母與範圍均與引用頁面一致，無推論或自評')
        f.write(json.dumps({'id':i,'verdict':v,'reason':r},ensure_ascii=False)+'\n')
