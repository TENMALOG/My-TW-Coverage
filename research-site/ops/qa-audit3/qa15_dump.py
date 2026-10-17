import json,re,sys
root='../../../'
ids=[l.strip() for l in open('ids_15.txt') if l.strip()]
cache={}
def pages(t):
    txt=open(root+t,encoding='utf8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    return {int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
tick=sys.argv[1]
d=json.load(open(root+f'research-site/data/company-facts/{tick}.json',encoding='utf8'))
pg=pages(d['source']['text_path'])
for f in d['facts']:
    if f['id'] not in ids: continue
    print('=====',f['id'],f['field'],f['period'],f['attribution'],'p',f['page'])
    print('ST:',f['statement'])
    print('EX:',f['excerpts'])
    if '-p' in sys.argv:
        for p in (f['page'],f['page']+1):
            print(f'--- page {p}');print(pg.get(p,'')[:3500])
