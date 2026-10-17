import json,sys,re
t,pg=sys.argv[1],int(sys.argv[2]); kw=sys.argv[3] if len(sys.argv)>3 else None; w=int(sys.argv[4]) if len(sys.argv)>4 else 300
f=json.load(open(f'data/company-facts/{t}.json',encoding='utf8'))
s=open('../'+f['source']['text_path'] if False else f['source']['text_path'],encoding='utf8').read() if False else None
import os
p=f['source']['text_path']
for base in ['..','.','../..']:
    if os.path.exists(os.path.join(base,p)): s=open(os.path.join(base,p),encoding='utf8').read();break
parts=re.split(r'\f',s)
if len(parts)<pg: print('pages',len(parts)); 
txt=parts[pg-1] if len(parts)>=pg else s
if kw:
    for m in re.finditer(kw,txt): print('...',txt[max(0,m.start()-w):m.end()+w].replace('\n','\n'),'\n----')
else: print(txt[:4000])
