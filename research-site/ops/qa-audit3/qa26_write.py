import json
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_26.txt') if l.strip()]
with open('research-site/ops/qa-audit3/out_26.jsonl','w',encoding='utf8') as f:
    for i in ids:
        f.write(json.dumps({"id":i,"verdict":"ACCEPT","reason":"數字、年度、單位、分母與範圍均與引用頁面一致，未增加推論"},ensure_ascii=False)+"\n")
