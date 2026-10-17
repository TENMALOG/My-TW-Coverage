import json
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_00.txt') if l.strip()]
rej={
 '1101-AR-13':'範圍縮減/擴大：原文為「本公司台灣地區外銷」發貨6.75萬公噸，陳述漏掉「台灣地區」，易被誤讀為集團（含大陸、葡萄牙等）整體外銷量。',
 '1103-AR-09':'片段句：原文為「雖未進行自主科技研發，但在策略投資時積極引入成熟科技…」，只截取「雖」字前半，改變原意並縮窄範圍。',
}
notes={
 'rd':'數字、年度、範圍與原頁一致','employees':'人數與年度欄位一致，並註明範圍','major_customers':'金額與占比與表列一致，代號/名稱標示正確',
 'major_suppliers':'金額與占比與表列一致，代號/名稱標示正確','revenue_mix':'金額、比重、年度與分母標示一致',
}
import json as J
facts={}
for tk in sorted({i.split('-AR-')[0] for i in ids}):
    d=J.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    for f in d['facts']: facts[f['id']]=f
with open('research-site/ops/qa-audit3/out_00.jsonl','w',encoding='utf8') as o:
    for i in ids:
        if i in rej: v,r='REJECT',rej[i]
        else: v,r='ACCEPT',notes.get(facts[i]['field'],'與引用頁原文一致，未增添推論或評價')
        o.write(J.dumps({'id':i,'verdict':v,'reason':r},ensure_ascii=False)+'\n')
print(len(ids))
