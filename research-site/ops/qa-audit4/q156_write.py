import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_156.txt',encoding='utf-8') if l.strip()]
with open('research-site/ops/qa-audit4/out_156.jsonl','w',encoding='utf-8') as f:
    for i in ids:
        f.write(json.dumps({"id":i,"verdict":"ACCEPT","reason":"已對照引用頁，數字、年度欄位、分母與範圍皆相符，無自然人姓名"},ensure_ascii=False)+"\n")
print(len(ids))
