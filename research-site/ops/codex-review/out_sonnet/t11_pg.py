import json,sys,re
tk=sys.argv[1]; pgn=int(sys.argv[2]); s=int(sys.argv[3]) if len(sys.argv)>3 else 0; L=int(sys.argv[4]) if len(sys.argv)>4 else 4000
d=json.load(open('research-site/data/company-facts/%s.json'%tk,encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',t)
for i in range(1,len(parts),2):
    if int(parts[i])==pgn: print(parts[i+1][s:s+L].replace('\n',' / '))
