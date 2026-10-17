import re,sys
sys.path.insert(0,'research-site/ops/qa-audit4')
from q121_page import page
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_121.txt') if l.strip()]
for i in ids:
    f,pg=page(i)
    p=f['page']; txt=pg.get(p,'')+pg.get(p+1,'')
    t2=re.sub(r'\s+','',txt)
    nums=re.findall(r'\d[\d,\.]*\d|\d',f['statement'])
    miss=[n for n in nums if n not in txt and n.replace(',','') not in t2]
    ex=[e for e in f['excerpts'] if re.sub(r'\s+','',e) not in t2]
    print(i,'MISS',miss,'EXMISS',len(ex), 'NOPAGE' if p not in pg else '')
