import json,re,sys
t=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pg={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
for a in sys.argv[2:]:
    p,_,k=a.partition(':')
    s=re.sub(r'[ \t]+\n','\n',pg[int(p)])
    if k:
        i=s.find(k); s=s[max(0,i-500):i+900]
    else: s=s[:3500]
    print('=====',p,k);print(s)
