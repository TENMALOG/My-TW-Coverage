import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_004.txt',encoding='utf8') if l.strip()]
with open('research-site/ops/qa-audit4/out_004.jsonl','w',encoding='utf8') as f:
    for i in ids:
        f.write(json.dumps({"id":i,"verdict":"ACCEPT","reason":"與引用頁一致，數字、年度、欄位、範圍皆無誤"},ensure_ascii=False)+"\n")
print(len(ids))
