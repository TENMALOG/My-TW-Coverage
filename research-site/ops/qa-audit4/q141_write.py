import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_141.txt',encoding='utf8') if l.strip()]
rej={
'6035-AR-12':'占比約63%年報未載明分母（statement亦自承），百分比未命名分母',
'6035-AR-13':'占比約82%年報未載明分母，百分比未命名分母',
'6104-AR-01':'以「所營業務為」斷定，僅列(1)積體電路與(2)軟體，漏列A至F其他產品及(3)代理與進出口貿易，縮窄業務範圍',
}
with open('research-site/ops/qa-audit4/out_141.jsonl','w',encoding='utf8') as o:
    for i in ids:
        v={'id':i,'verdict':'REJECT','reason':rej[i]} if i in rej else {'id':i,'verdict':'ACCEPT','reason':'數字、年度、欄位、範圍與引用頁相符'}
        o.write(json.dumps(v,ensure_ascii=False)+'\n')
print(len(ids))
