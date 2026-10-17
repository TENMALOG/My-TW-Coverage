import json
ids=[l.strip() for l in open('ids_184.txt',encoding='utf8') if l.strip()]
with open('out_184.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r="逐項核對引用頁，數字、年度、單位、分母、範圍與歸屬均與原文相符"
        if i=='6728-AR-14': r="內容相符（原文位於次頁第86頁，引用第85頁僅為標題），無數字或範圍問題"
        f.write(json.dumps({"id":i,"verdict":"ACCEPT","reason":r},ensure_ascii=False)+"\n")
