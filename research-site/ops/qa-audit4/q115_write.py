import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_115.txt',encoding='utf8') if l.strip()]
rej={'4974-AR-09':'原文為短期計畫中「持續強化緬甸廠生產管理優勢」，屬公司自述性計畫與評價，卻以「公司年報揭露」歸屬並歸為產能欄位，未標示為計畫且未用自述歸屬',
'4976-AR-09':'R0133、R0106為年報匿名代號，陳述未註明為年報代號，讀來像真實來源名稱'}
with open('research-site/ops/qa-audit4/out_115.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r=rej.get(i)
        f.write(json.dumps({'id':i,'verdict':'REJECT' if r else 'ACCEPT','reason':r or '數字、年度、欄位與分母皆與引用頁面一致，歸屬適當'},ensure_ascii=False)+'\n')
print(len(ids))
