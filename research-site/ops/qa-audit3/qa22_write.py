import json
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_22.txt') if l.strip()]
rej={
'2387-AR-01':'營收結構比重（73%／27%）未標示任何年度，違反營收結構須載年度之規則',
'2387-AR-16':'員工人數表未載明母公司或合併範圍，陳述寫「公司員工」暗示公司（母公司）範圍，且未註明表格未載範圍',
'2388-AR-14':'員工人數表未載明範圍，陳述寫「公司從業員工」暗示公司範圍，且未註明表格未載範圍',
}
with open('research-site/ops/qa-audit3/out_22.jsonl','w',encoding='utf8') as f:
    for i in ids:
        if i in rej: r={'id':i,'verdict':'REJECT','reason':rej[i]}
        else: r={'id':i,'verdict':'ACCEPT','reason':'已對照引用頁面，數字、年度、單位、欄位、分母與範圍皆與原文相符，無新增推論'}
        f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(ids))
