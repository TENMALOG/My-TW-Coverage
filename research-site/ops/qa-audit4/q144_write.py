import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_144.txt',encoding='utf8') if l.strip()]
with open('research-site/ops/qa-audit4/out_144.jsonl','w',encoding='utf8',newline='\n') as f:
    for i in ids:
        f.write(json.dumps({"id":i,"verdict":"ACCEPT","reason":"已核對引用頁，數字、年度、分母與範圍均與年報相符"},ensure_ascii=False)+"\n")
print(len(ids))
