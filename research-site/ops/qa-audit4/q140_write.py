import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_140.txt',encoding='utf8') if l.strip()]
rej={'5904-AR-07':'銷售地區陳述未載年度（原文為最近三年度區域表），缺年份',
'6016-AR-08':'員工表含「子公司」162人列，合計804人含子公司，陳述稱「未載明範圍」與表不符，範圍描述錯誤'}
with open('research-site/ops/qa-audit4/out_140.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r=rej.get(i)
        f.write(json.dumps({'id':i,'verdict':'REJECT' if r else 'ACCEPT','reason':r or '與引用頁面一致'},ensure_ascii=False)+'\n')
print(len(ids))
