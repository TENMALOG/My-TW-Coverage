import json,re,sys
t=sys.argv[1];pat=sys.argv[2]
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8'))
txt=open(d['source']['text_path'],encoding='utf-8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
for i in range(1,len(parts),2):
    if re.search(pat,parts[i+1]):
        print('PAGE',parts[i]); 
        for m in re.finditer(pat,parts[i+1]):
            s=max(0,m.start()-int(sys.argv[3])); print(parts[i+1][s:m.end()+int(sys.argv[3])]); print('---')
