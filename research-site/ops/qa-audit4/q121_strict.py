import re,sys
sys.path.insert(0,'research-site/ops/qa-audit4')
from q121_page import page
for i in [l.strip() for l in open('research-site/ops/qa-audit4/ids_121.txt') if l.strip()]:
    f,pg=page(i); t=re.sub(r'\s+','',pg.get(f['page'],''))
    bad=[e[:40] for e in f['excerpts'] if re.sub(r'\s+','',e) not in t]
    if bad: print(i,bad)
