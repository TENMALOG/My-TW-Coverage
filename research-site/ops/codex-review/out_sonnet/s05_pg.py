import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
t=sys.argv[1]; p=int(sys.argv[2]); a=int(sys.argv[3]); b=int(sys.argv[4])
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
pg={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
print(re.sub(r'\s+',' ',pg.get(p,''))[a:b])
