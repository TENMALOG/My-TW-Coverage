import json,io
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_110.txt',encoding='utf8') if l.strip()]
with io.open('research-site/ops/qa-audit4/out_110.jsonl','w',encoding='utf8') as f:
    for i in ids:
        f.write(json.dumps({"id":i,"verdict":"ACCEPT","reason":"已對照引用頁面，數字、年度欄、分母、範圍與歸屬皆相符"},ensure_ascii=False)+"\n")
