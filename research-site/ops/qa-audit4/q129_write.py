import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_129.txt') if l.strip()]
rej={'5425-AR-12':'員工人數表附註載明數字僅含整流器集團人數，不含條碼印表機部門（鼎翰科技），陳述卻寫「未載明範圍」且未揭露此範圍限制，範圍有誤。'}
with open('research-site/ops/qa-audit4/out_129.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r=rej.get(i)
        f.write(json.dumps({'id':i,'verdict':'REJECT' if r else 'ACCEPT','reason':r or '與引用頁內容一致，數字、年度、分母與範圍皆無誤'},ensure_ascii=False)+'\n')
