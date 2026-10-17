import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_127.txt') if l.strip()]
rej={'5348-AR-02':'「兼營運動商品買賣」與原文不符：原文(4)運動商品買賣為獨立經營項目，「兼營」僅指(2)(3)；且僅挑衛星項目，縮窄(a)-(d)四項範圍。'}
with open('research-site/ops/qa-audit4/out_127.jsonl','w',encoding='utf8') as f:
    for i in ids:
        r=rej.get(i)
        f.write(json.dumps({'id':i,'verdict':'REJECT' if r else 'ACCEPT','reason':r or '與引用頁面內容一致'},ensure_ascii=False)+'\n')
print(len(ids))
