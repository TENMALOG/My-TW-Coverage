import json
base = r'C:\Users\Neo Pegasus\Documents\ChatGPT\078-kaori sample\artifacts\stock-coverage-audit-20261003\incoming\latest-audit\My-TW-Coverage\research-site\ops\relations-match'
d = json.load(open(base + r'\in_3.json', encoding='utf-8'))
bad = {0,1,2,6,8,9,14,21,22,23,35,57,58,68,80,99,100,101,102,103,118,124,125,126,127,132,133,134,135,141,157,158,159,161,174,175,177,185,186,187,188,189,207,221,223,224,225,226,227,232,233,234,238,241,246,255,271,272,276,280,281,283,290,304,306,76,77,78,79}
match = {
    106: ('2002', 'supplier', '中國鋼鐵股份有限公司 = 中鋼 legal_name'),
    253: ('1314', 'supplier', '中國石油化學工業開發股份有限公司 = 中石化 legal_name'),
    254: ('1314', 'supplier', '中國石油化學工業開發股份有限公司 = 中石化 legal_name'),
    244: ('2006', 'supplier', '東和鋼鐵企業（股）公司 = 東和鋼鐵 legal_name；欄位文字為截斷片段，但陳述完整'),
    287: ('3324', 'customer', '雙鴻科技(股)公司 = 雙鴻 legal_name'),
    288: ('2501', 'customer', '國泰建設(股)公司 = 國建 legal_name'),
    214: ('3032', 'parent', '偉訓（與公司關係為母公司）對應目錄簡稱偉訓（偉訓科技）；角色為母公司'),
}
# fix: 242-ish index mapping check by name below
out = []
for i, it in enumerate(d):
    if i in match:
        t, r, why = match[i]
        out.append(dict(relation_id=it['relation_id'], fact_id=it['fact_id'], counterparty=it['counterparty'], verdict='MATCH', counterparty_ticker=t, role=r, reason=why))
    else:
        v = 'BAD_NAME' if i in bad else 'NOT_LISTED'
        out.append(dict(relation_id=it['relation_id'], fact_id=it['fact_id'], counterparty=it['counterparty'], verdict=v, counterparty_ticker=None, role=it['role'], reason='自動依人工逐筆判定'))
with open(base + r'\out_3.jsonl', 'w', encoding='utf-8') as f:
    for o in out:
        f.write(json.dumps(o, ensure_ascii=False) + '\n')
from collections import Counter
print(Counter(o['verdict'] for o in out))
for i in sorted(match): print(i, d[i]['counterparty'], d[i]['company'])
