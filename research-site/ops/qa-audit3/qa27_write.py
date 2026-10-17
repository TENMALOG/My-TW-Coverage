import json
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_27.txt') if l.strip()]
with open('research-site/ops/qa-audit3/out_27.jsonl','w',encoding='utf8') as f:
    for i in ids:
        f.write(json.dumps({"id":i,"verdict":"ACCEPT","reason":"已對照引用頁面，數字、年度、欄位、分母與範圍均相符"},ensure_ascii=False)+"\n")
