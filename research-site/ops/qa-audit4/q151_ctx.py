import json,re,sys
sys.path.insert(0,'.')
t=sys.argv[1]; pgs=[int(x) for x in sys.argv[2:]]
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
for p in pgs:
    print(f'--- PAGE {p} ---'); print(re.sub(r'\n\s*\n+','\n',re.sub(r'[ \t]+',' ',pages.get(p,'MISSING'))))
