import json,re,sys
root='../../../'
tick=sys.argv[1]
d=json.load(open(root+f'research-site/data/company-facts/{tick}.json',encoding='utf8'))
txt=open(root+d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pg={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
for p in sys.argv[2:]:
    print(f'--- page {p}');print(pg.get(int(p),''))
