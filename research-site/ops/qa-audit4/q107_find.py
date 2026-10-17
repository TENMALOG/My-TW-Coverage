import json,re,sys
t=sys.argv[1]; pat='\s*'.join(re.escape(c) for c in sys.argv[2] if not c.isspace()); ctx=int(sys.argv[3]) if len(sys.argv)>3 else 300
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8'))
txt=open(d['source']['text_path'],encoding='utf-8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
for k in range(1,len(parts),2):
    for m in re.finditer(pat,parts[k+1]):
        s=parts[k+1]; print('--- page',parts[k],'---'); print(s[max(0,m.start()-ctx):m.end()+ctx])
