import json
R='research-site/ops/qa-audit3/'
ids=[l.strip() for l in open(R+'ids_08.txt') if l.strip()]
rej={
 '1608-AR-03':'營業比重（銅片22%）年報原文未載會計年度，陳述亦無年份，營收組合比率缺年份',
 '1608-AR-04':'營業比重（銅線15%）年報原文未載會計年度，陳述亦無年份，營收組合比率缺年份',
 '1609-AR-01':'營業比重（交連聚乙烯電力電纜56.58%）年報表格未載年度，陳述亦無年份，營收組合比率缺年份',
 '1609-AR-02':'營業比重（塑膠電線電纜16.25%）年報表格未載年度，陳述亦無年份，營收組合比率缺年份',
 '1609-AR-03':'營業比重（漆包線12.48%）年報表格未載年度，陳述亦無年份，營收組合比率缺年份',
}
with open(R+'out_08.jsonl','w',encoding='utf8') as f:
    for i in ids:
        if i in rej: o={'id':i,'verdict':'REJECT','reason':rej[i]}
        else: o={'id':i,'verdict':'ACCEPT','reason':'數字、年度、欄位與引用頁面一致，範圍與分母敘述無誤'}
        f.write(json.dumps(o,ensure_ascii=False)+'\n')
print(len(ids),len(rej))
