import json
base = r"C:/Users/Neo Pegasus/Documents/ChatGPT/078-kaori sample/artifacts/stock-coverage-audit-20261003/incoming/latest-audit/My-TW-Coverage/research-site/ops/qa-audit3/"
ids = [l.strip() for l in open(base + 'ids_16.txt', encoding='utf-8') if l.strip()]
rej = {
    '2221-AR-12': '年報「TOP3 庫存商」為排名性質的敘述，卻以「公司年報揭露」呈現；應標示為公司年報自述（未經獨立驗證的排名或評價）。',
}
with open(base + 'out_16.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for i in ids:
        if i in rej:
            o = {"id": i, "verdict": "REJECT", "reason": rej[i]}
        else:
            o = {"id": i, "verdict": "ACCEPT", "reason": "與引用頁面內容、數字、年度、欄位、範圍及歸屬一致。"}
        f.write(json.dumps(o, ensure_ascii=False) + '\n')
print(len(ids))
