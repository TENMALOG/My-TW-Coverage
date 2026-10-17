import json
ids=[l.strip() for l in open('ids_12.txt',encoding='utf8') if l.strip()]
rej={
'2013-AR-09':'百分比（內銷100%、外銷0%）未載明分母，陳述自承年報未載分母',
'2013-AR-10':'百分比（內銷77%、外銷23%）未載明分母，陳述自承年報未載分母',
'2013-AR-16':'比率未明確命名分母，且該表表頭印為「進貨淨額比率」與銷貨淨額不一致，分母不明',
'2013-AR-17':'比率未明確命名分母，且該表表頭印為「進貨淨額比率」與銷貨淨額不一致，分母不明',
}
with open('out_12.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r={'id':i,'verdict':'REJECT','reason':rej[i]} if i in rej else {'id':i,'verdict':'ACCEPT','reason':'數字、年度、範圍與引用頁一致'}
        f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(ids))
