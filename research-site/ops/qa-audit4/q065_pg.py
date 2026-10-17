import json,sys,re
t=sys.argv[1];p=int(sys.argv[2]);kw=sys.argv[3];n=int(sys.argv[4]) if len(sys.argv)>4 else 900
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pg={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
s=pg[p];k=s.find(kw)
print(s[max(0,k-100):k+n].replace('\n',' / '))
