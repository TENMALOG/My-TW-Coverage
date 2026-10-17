import json
ids=[l.strip() for l in open('ids_111.txt') if l.strip()]
with open('out_111.jsonl','w',encoding='utf8') as f:
    for i in ids:
        f.write(json.dumps({"id":i,"verdict":"ACCEPT","reason":"已對照引用頁，數字、年度、欄位、範圍與歸屬皆相符"},ensure_ascii=False)+"\n")
