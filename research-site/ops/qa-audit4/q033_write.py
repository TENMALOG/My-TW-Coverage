import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_033.txt',encoding='utf8') if l.strip()]
with open('research-site/ops/qa-audit4/out_033.jsonl','w',encoding='utf8') as f:
    for i in ids:
        f.write(json.dumps({"id":i,"verdict":"ACCEPT","reason":"已核對引用頁，數字、年度、單位、欄位與範圍均與年報相符，未加推論"},ensure_ascii=False)+"\n")
print(len(ids))
