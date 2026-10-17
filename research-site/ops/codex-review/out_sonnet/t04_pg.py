import json,sys,re,os
os.chdir(r"C:/Users/Neo Pegasus/Documents/ChatGPT/078-kaori sample/artifacts/stock-coverage-audit-20261003/incoming/latest-audit/My-TW-Coverage")
tk=sys.argv[1]; pg=int(sys.argv[2]); pat=sys.argv[3] if len(sys.argv)>3 else None
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
P={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
t=P[pg]
if pat:
    for m in re.finditer(pat,t):
        print('...',t[max(0,m.start()-300):m.end()+300].replace('\n',' / '))
else: print(t)
