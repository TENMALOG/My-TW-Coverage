import json,sys,re,io
t,page=sys.argv[1],int(sys.argv[2]); kw=sys.argv[3] if len(sys.argv)>3 else None
f=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(f['source']['text_path'],encoding='utf8').read()
# find page markers
parts=re.split(r'\f',txt)
p=parts[page-1] if len(parts)>page else ''
if len(parts)<=page: print('nopages',len(parts)); 
i=p.find(kw) if kw else 0
sys.stdout=io.open(1,'w',encoding='utf8',closefd=False)
print(p[max(0,i-600):i+900])
