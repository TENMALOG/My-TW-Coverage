import json,sys,re
t=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\n\[PDF PAGE (\d+)\]\n',txt)
pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
for p in sys.argv[2:]:
    print(f'##### {t} PAGE {p}'); print(re.sub(r'[ \t]+',' ',pages[int(p)]))
