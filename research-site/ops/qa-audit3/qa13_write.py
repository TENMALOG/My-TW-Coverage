import json
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_13.txt') if l.strip()]
rej={
 '2027-AR-09':'範圍改變：原文主詞為「本公司及其子公司（合稱大成鋼集團）」透過40個營運據點銷售，陳述省略集團範圍而寫成公司本身',
 '2029-AR-12':'百分比未命名分母：原表僅列「國內廠商供應／國外廠商供應」82.24%、17.76%，未載明比率分母（陳述自承未載明），不符規則',
}
with open('research-site/ops/qa-audit3/out_13.jsonl','w',encoding='utf8') as f:
    for i in ids:
        v='REJECT' if i in rej else 'ACCEPT'
        r=rej.get(i,'逐項核對引用頁面，數字、年度、欄位、範圍與屬性皆與原文相符')
        f.write(json.dumps({'id':i,'verdict':v,'reason':r},ensure_ascii=False)+'\n')
print(len(ids))
