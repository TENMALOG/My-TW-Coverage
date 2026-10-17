import json,sys,re
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
for i,p,k in [('6803',1,'原名'),('6952',91,'原登記'),('6953',1,'原名'),('6962',6,'更名'),('7578',1,'原名')]:
    f=json.load(open(f"research-site/data/company-facts/{i}.json",encoding='utf-8'))
    t=page_texts(open(f['source']['text_path'],encoding='utf-8').read())[p]
    m=re.search(k,t);print(i,repr(t[max(0,m.start()-30):m.end()+110]))
