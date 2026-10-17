import json,sys,re,os
t,pg=sys.argv[1],int(sys.argv[2]); a=int(sys.argv[3]); b=int(sys.argv[4])
f=json.load(open(f'data/company-facts/{t}.json',encoding='utf8'))
s=open('../'+f['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF\s+PAGE\s+(\d+)\]',s)
d={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
sys.stdout.buffer.write(d[pg][a:b].encode('utf8'))
