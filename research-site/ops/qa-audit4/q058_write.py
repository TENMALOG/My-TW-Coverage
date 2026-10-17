import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_058.txt',encoding='utf8') if l.strip()]
rej={'3230-AR-05':'陳述句未載明年度（僅 period 欄位有 114年度），營收比重數字在陳述中無年份'}
with open('research-site/ops/qa-audit4/out_058.jsonl','w',encoding='utf8') as f:
    for i in ids:
        v='REJECT' if i in rej else 'ACCEPT'
        r=rej.get(i,'與引用頁面內容相符')
        f.write(json.dumps({'id':i,'verdict':v,'reason':r},ensure_ascii=False)+'\n')
print(len(ids))
