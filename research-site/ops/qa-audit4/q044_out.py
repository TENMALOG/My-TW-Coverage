import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_044.txt') if l.strip()]
rej={'3017-AR-16':'陳述稱「本公司從業員工人數」暗示母公司範圍，但員工表未載明母公司或合併範圍（且26,444人明顯非單純母公司），應改為未載明範圍'}
with open('research-site/ops/qa-audit4/out_044.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r={'id':i,'verdict':'REJECT' if i in rej else 'ACCEPT','reason':rej.get(i,'與引用頁面表格及文字相符，分母、年度、範圍均正確')}
        f.write(json.dumps(r,ensure_ascii=False)+'\n')
