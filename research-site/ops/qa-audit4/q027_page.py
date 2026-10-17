import json,sys,re
t,p=sys.argv[1],int(sys.argv[2]); a=int(sys.argv[3]) if len(sys.argv)>3 else 0; b=int(sys.argv[4]) if len(sys.argv)>4 else 4000
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]\n',txt)
m={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
print(m[p][a:b])
