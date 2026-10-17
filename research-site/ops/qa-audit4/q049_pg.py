import json,re,sys
t=sys.argv[1];p=int(sys.argv[2]);a=int(sys.argv[3]);b=int(sys.argv[4])
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
pg={int(pages[i]):pages[i+1] for i in range(1,len(pages),2)}
print(pg[p][a:b])
