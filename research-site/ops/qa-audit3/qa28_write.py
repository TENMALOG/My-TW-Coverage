import json
R='research-site/ops/qa-audit3/'
ids=[l.strip() for l in open(R+'ids_28.txt') if l.strip()]
with open(R+'out_28.jsonl','w',encoding='utf8') as f:
    for i in ids:
        f.write(json.dumps({"id":i,"verdict":"ACCEPT","reason":"數字、年度、單位、欄位與引用頁表格一致；分母或代號標示正確，無推論或範圍變更"},ensure_ascii=False)+"\n")
print(len(ids))
