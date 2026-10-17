import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_123.txt',encoding='utf8') if l.strip()]
rej={'5262-AR-03':'年報該列為「自有品牌，包含記憶卡，電腦週邊，手機週邊等零售包的B2C通路」，陳述只寫「手機週邊等」，縮窄了業務範圍'}
with open('research-site/ops/qa-audit4/out_123.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r=rej.get(i)
        f.write(json.dumps({'id':i,'verdict':'REJECT' if r else 'ACCEPT','reason':r or '與引用頁面一致，數字、年度、分母、範圍皆相符'},ensure_ascii=False)+'\n')
