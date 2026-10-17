import sys,json,re,os
R=os.path.abspath('../../..')
t=sys.argv[1]; p=int(sys.argv[2]); n=int(sys.argv[3]) if len(sys.argv)>3 else 3500
d=json.load(open(f'{R}/research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(f"{R}/{d['source']['text_path']}",encoding='utf8').read()
pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
pg={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
print(re.sub(r'\n\s*\n+','\n',pg.get(p,''))[:n])
