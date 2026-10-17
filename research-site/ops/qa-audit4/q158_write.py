import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_158.txt',encoding='utf-8') if l.strip()]
rej={'6240-AR-06':'僅挑選88項登記營業項目中的4項（含不相鄰項目），略去占營收77%的資訊軟體服務業，縮窄並扭曲營業範圍'}
with open('research-site/ops/qa-audit4/out_158.jsonl','w',encoding='utf-8') as f:
    for i in ids:
        v='REJECT' if i in rej else 'ACCEPT'
        r=rej.get(i,'與引用頁面一致，數字、年度、分母、範圍均無誤')
        f.write(json.dumps({'id':i,'verdict':v,'reason':r},ensure_ascii=False)+'\n')
print(len(ids))
