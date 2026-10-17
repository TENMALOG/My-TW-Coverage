import json
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_147.txt', encoding='utf8') if l.strip()]
rej = {
    '6156-AR-07': '年報原文為「本集團」營業額推算之市佔率仍低，屬公司自述評價，卻標為「公司年報揭露」且改成「公司」，屬自評當事實且範圍由集團縮為公司；應標為公司年報自述（未經獨立驗證的排名或評價）並保留集團範圍。',
    '6156-AR-09': '「銷貨淨額占比最高的客戶」為年報未作的排名陳述，由表列第1列/金額推得；年報僅列示S公司1,080,159仟元、22.05%，不應加入「最高」排名。',
}
with open('research-site/ops/qa-audit4/out_147.jsonl', 'w', encoding='utf8') as f:
    for i in ids:
        if i in rej:
            o = {'id': i, 'verdict': 'REJECT', 'reason': rej[i]}
        else:
            o = {'id': i, 'verdict': 'ACCEPT', 'reason': '與引用頁面數字、年度、單位、分母及範圍一致'}
        f.write(json.dumps(o, ensure_ascii=False) + '\n')
print(len(ids))
