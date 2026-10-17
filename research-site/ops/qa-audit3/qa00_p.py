import json,re
d=json.load(open('research-site/data/company-facts/1102.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
m=re.search(r'\[PDF PAGE 102\]\n(.*?)(?=\[PDF PAGE 103\]|\Z)',t,re.S)
print(m.group(1)[:1200])
