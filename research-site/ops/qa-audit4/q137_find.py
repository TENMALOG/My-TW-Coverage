import json,re,sys
t=sys.argv[1]; kw=sys.argv[2]
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
for i in range(1,len(parts),2):
    b=parts[i+1]; idx=[j for j,c in enumerate(b) if not c.isspace()]; sb=''.join(b[j] for j in idx)
    k=re.sub(r'\s+','',kw)
    for m in re.finditer(re.escape(k),sb):
        a=idx[max(0,m.start()-80)]; print('p',parts[i],':',b[a:a+400].replace('\n',' / ')); 
