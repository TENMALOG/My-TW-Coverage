import json,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_083.txt') if l.strip()]
cache={}
def load(t):
    if t in cache: return cache[t]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    txt=open(d['source']['text_path'],encoding='utf8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    cache[t]=(d,pages); return cache[t]
n=lambda s:re.sub(r'\s+','',s)
if __name__=='__main__':
  for i in ids:
    t=i.split('-AR-')[0]; d,pages=load(t)
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=n(pages.get(f['page'],''))
    miss=[e for e in f['excerpts'] if n(e) not in pg]
    if miss: print(i,'MISSING',miss)
  print('done')
