import json,re,sys
tk,kw=sys.argv[1],sys.argv[2]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',t)
for i in range(1,len(parts),2):
    if kw in parts[i+1]:
        txt=parts[i+1];j=txt.index(kw);print('PAGE',parts[i]);print(txt[max(0,j-300):j+700]);print('-----')
