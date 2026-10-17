import json,sys
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
t=sys.argv[1];p=int(sys.argv[2]);k=sys.argv[3]
f=json.load(open(f"research-site/data/company-facts/{t}.json",encoding='utf-8'))
pt=page_texts(open(f['source']['text_path'],encoding='utf-8').read())
x=pt[p];i=x.find(k)
print(x[max(0,i-300):i+500])
