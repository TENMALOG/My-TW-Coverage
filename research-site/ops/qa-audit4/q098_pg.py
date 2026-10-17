import json,re,sys
t,p=sys.argv[1],int(sys.argv[2])
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
x=re.split(r'\[PDF PAGE (\d+)\]',txt)
print({int(x[k]):x[k+1] for k in range(1,len(x),2)}[p])
