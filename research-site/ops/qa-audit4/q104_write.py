import json
ids=[l.strip() for l in open('ids_104.txt',encoding='utf8') if l.strip()]
rej={'4706-AR-20':'年報原文為「國內」顏料市場佔有率（台灣區顏染料公會統計），陳述漏列「國內」範圍，市占分母不明且可能被解讀為更廣市場'}
with open('out_104.jsonl','w',encoding='utf8') as f:
    for i in ids:
        v='REJECT' if i in rej else 'ACCEPT'
        f.write(json.dumps({'id':i,'verdict':v,'reason':rej.get(i,'數字、年度、單位、範圍與年報引用頁一致')},ensure_ascii=False)+'\n')
print(len(ids))
