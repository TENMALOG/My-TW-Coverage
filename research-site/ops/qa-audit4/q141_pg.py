import json,re,sys
tk=sys.argv[1]; pg=int(sys.argv[2]); pat=sys.argv[3] if len(sys.argv)>3 else ''; a=int(sys.argv[4]) if len(sys.argv)>4 else 1800
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
s=re.split(r'\[PDF PAGE (\d+)\]',t)
pages={int(s[k]):s[k+1] for k in range(1,len(s),2)}
x=re.sub(r'\n\s*\n','\n',pages[pg]); m=x.find(pat) if pat else 0
if m<0:m=0
print(f'## {tk} p{pg}'); print(x[max(0,m-300):m+a])
