import json,re,sys
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
jobs=json.load(open('research-site/ops/renames/jobs/rn_000.json',encoding='utf8'))
pat=re.compile(r'(原名|前身|更名|改名|變更名稱|變更公司名稱|名稱變更|核准變更|曾用名|舊名)')
for e in jobs:
    t=e['ticker']
    f=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    tp=f['source']['text_path']
    text=open(tp,encoding='utf8').read() if not tp.startswith('research-site') else open(tp,encoding='utf8').read()
    pg=page_texts(text)
    for p,x in pg.items():
        for m in pat.finditer(x):
            s=x[max(0,m.start()-60):m.end()+60].replace('\n',' ')
            if re.search(r'公司|股份',s) and not re.search(r'委員會|守則|辦法|報告書|政策|轉投資事業|評鑑|評估|準則|基金會|處',s):
                print(t,p,s)
