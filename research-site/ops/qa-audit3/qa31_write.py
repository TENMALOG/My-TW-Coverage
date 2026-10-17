import json
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_31.txt') if l.strip()]
rej={'2937-AR-17':'截斷句子：原文為「雖無自行開發或他人授權之技術，但…須經具有經驗與專業技術人員規劃搭配…是優於其他同業之技術能力」，僅保留前半句使業務範圍被窄化'}
with open('research-site/ops/qa-audit3/out_31.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r=rej.get(i)
        f.write(json.dumps({'id':i,'verdict':'REJECT' if r else 'ACCEPT','reason':r or '數字、年度、單位、分母與原頁一致，無範圍或推論問題'},ensure_ascii=False)+'\n')
