import json
ids=[l.strip() for l in open('ids_24.txt',encoding='utf-8') if l.strip()]
rej={'2436-AR-117':'員工人數表未載明母公司或合併範圍，陳述「公司從業員工」暗示公司（母公司）範圍，範圍措辭超出表格','2442-AR-12':'陳述為殘缺句且「75年」未標民國，年份易誤讀為西元，未完整表達成立事實'}
with open('out_24.jsonl','w',encoding='utf-8') as o:
    for i in ids:
        v='REJECT' if i in rej else 'ACCEPT'
        r=rej.get(i,'與引用頁面數字、年度、欄位、範圍相符')
        o.write(json.dumps({'id':i,'verdict':v,'reason':r},ensure_ascii=False)+'\n')
