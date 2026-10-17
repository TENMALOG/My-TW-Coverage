import json
rej={
"2327-AR-12":"原文為「本公司及子公司」114年度資本支出（合併範圍），陳述只寫「公司」，範圍被改成單指母公司",
"2328-AR-01":"營業比重表（電子零組件61%、消費性電子39%）原文未載年度，陳述期間欄為「年報揭露時點」，營收比重數字缺年度",
"2330-AR-19":"原文為亞利桑那州的第二座晶圓廠，陳述省略「亞利桑那州」，讀來像台積電整體第二座晶圓廠，範圍被放寬",
}
ids=[l.strip() for l in open('ids_024.txt',encoding='utf8') if l.strip()]
with open('out_024.jsonl','w',encoding='utf8') as f:
    for i in ids:
        if i in rej: o={"id":i,"verdict":"REJECT","reason":rej[i]}
        else: o={"id":i,"verdict":"ACCEPT","reason":"陳述與引用頁面一致，數字、年度、範圍、歸屬皆無誤"}
        f.write(json.dumps(o,ensure_ascii=False)+"\n")
print(len(ids))
