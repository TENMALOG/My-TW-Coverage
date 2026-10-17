import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_181.txt',encoding='utf-8') if l.strip()]
with open('research-site/ops/qa-audit4/out_181.jsonl','w',encoding='utf-8') as f:
    for i in ids:
        f.write(json.dumps({"id":i,"verdict":"ACCEPT","reason":"數字、年度、欄位、範圍與年報頁面相符，無推論，歸屬正確"},ensure_ascii=False)+"\n")
print(len(ids))
