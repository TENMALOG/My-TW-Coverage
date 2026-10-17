import json,sys,re
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
jobs=json.load(open('research-site/ops/renames/jobs/rn_009.json',encoding='utf-8'))
print(len(jobs))
lo,hi=int(sys.argv[1]),int(sys.argv[2])
pat=re.compile(r'更名|改名|原名|原稱|更改名稱|名稱變更|變更名稱|變更為|易名|改稱|更改公司名稱|Formerly|renamed|changed (its|the) name')
for j in jobs[lo:hi]:
    f=json.load(open(f"research-site/data/company-facts/{j['id']}.json",encoding='utf-8'))
    pt=page_texts(open(f['source']['text_path'],encoding='utf-8').read())
    print('=====',j['id'],j['company'],j['legal_name'])
    for h in j['hits']:
        for p in (h['page'],):
            t=pt.get(p,'')
            for m in pat.finditer(t):
                s=max(0,m.start()-100);print(f'  p{p}:',t[s:m.end()+120].replace('\n',' '))
