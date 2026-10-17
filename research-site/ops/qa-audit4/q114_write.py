import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_114.txt') if l.strip()]
rej={
'4967-AR-17':'排名為公司引述TrendForce「歷年」統計，未載年度與報告，屬未經獨立驗證的公司排名，attribution不應標為第三方資料',
'4967-AR-18':'排名為公司引述TrendForce「歷年」統計，未載年度與報告，屬未經獨立驗證的公司排名，attribution不應標為第三方資料',
}
with open('research-site/ops/qa-audit4/out_114.jsonl','w',encoding='utf8') as o:
    for i in ids:
        if i in rej: r={'id':i,'verdict':'REJECT','reason':rej[i]}
        else: r={'id':i,'verdict':'ACCEPT','reason':'與引用頁面內容一致'}
        o.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(ids))
