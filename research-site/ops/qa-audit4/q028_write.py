import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_028.txt',encoding='utf8') if l.strip()]
rej={'2405-AR-23':'「具備醫療器材開發之專業能力與通路基礎」為公司自我評價，卻標示為「公司年報揭露」，應標為公司年報自述（未經獨立驗證的排名或評價）',
'2413-AR-19':'年報原文為「本公司及其子公司」累計研發費用185,484仟元，敘述僅稱「公司」，範圍由合併縮窄為公司本身'}
with open('research-site/ops/qa-audit4/out_028.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r=rej.get(i)
        f.write(json.dumps({'id':i,'verdict':'REJECT' if r else 'ACCEPT','reason':r or '數字、年度、分母與範圍均與引用頁相符'},ensure_ascii=False)+'\n')
print(len(ids))
