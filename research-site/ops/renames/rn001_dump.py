import json,sys,re
from pathlib import Path
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
job=json.load(open('research-site/ops/renames/jobs/rn_001.json',encoding='utf8'))
KW=re.compile(r'更名|改名|原名|名稱變更|變更名稱|更改名稱|更改公司名|易名|前身|更名為|公司名稱')
lo,hi=int(sys.argv[1]),int(sys.argv[2])
for e in job[lo:hi]:
    t=e['id']
    f=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    txt=Path(f['source']['text_path']).read_text(encoding='utf8') if Path(f['source']['text_path']).exists() else Path('.',f['source']['text_path']).read_text(encoding='utf8')
    pg=page_texts(txt)
    print('=====',t,e['company'],e['legal_name'])
    for h in e['hits']:
        p=h['page'];s=pg.get(p,'')
        for m in KW.finditer(s):
            if '欄位名稱' in s[max(0,m.start()-40):m.end()+20]: continue
            a=max(0,m.start()-150);b=min(len(s),m.end()+200)
            print(f'  [p{p}]',re.sub(r'\s+',' ',s[a:b]));
