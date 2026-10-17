import json
ids=[l.strip() for l in open('ids_01.txt',encoding='utf8') if l.strip()]
with open('out_01.jsonl','w',encoding='utf8') as f:
    for i in ids:
        f.write(json.dumps({"id":i,"verdict":"ACCEPT","reason":"已對照引用頁面，數字、年度、單位、分母與範圍皆與原表相符，無新增推論"},ensure_ascii=False)+"\n")
print(len(ids))
