import json,sys,re
tick,pn,pat=sys.argv[1],int(sys.argv[2]),sys.argv[3]
bef=int(sys.argv[4]) if len(sys.argv)>4 else 200; aft=int(sys.argv[5]) if len(sys.argv)>5 else 900
d=json.load(open(f'research-site/data/company-facts/{tick}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
pages={int(m.group(1)):m.end() for m in re.finditer(r'\[PDF PAGE (\d+)\]',t)}
def page(n):
    if n not in pages: return ''
    s=pages[n]; e=pages.get(n+1,len(t))
    return re.sub(r'[ \t]+',' ',re.sub(r'\n\s*\n+','\n',t[s:e]))
pg=page(pn)+'\n[NEXTPAGE]\n'+page(pn+1)
i=pg.find(pat)
print(tick,pn,pat,'->',i)
if i>=0: print(pg[max(0,i-bef):i+aft])
