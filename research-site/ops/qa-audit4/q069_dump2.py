import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_069.txt') if l.strip()]
tick=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tick}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
pages={int(m.group(1)):m.end() for m in re.finditer(r'\[PDF PAGE (\d+)\]',t)}
def page(n):
    if n not in pages: return ''
    s=pages[n]; e=pages.get(n+1,len(t))
    return re.sub(r'[ \t]+',' ',re.sub(r'\n\s*\n+','\n',t[s:e]))
print('#####',tick,d['company'],d['source']['fy'])
W=int(sys.argv[2]) if len(sys.argv)>2 else 450
for f in d['facts']:
    if f['id'] in ids and f['id'].startswith(tick):
        print('=====',f['id'],f['field'],f['period'],'p',f['page'],f['attribution'])
        print('STMT:',f['statement'])
        pg=page(f['page'])+'\n[NEXT]\n'+page(f['page']+1)
        # anchor on excerpts
        shown=[]
        for ex in f['excerpts']:
            toks=[x for x in re.split(r'\s+',ex) if len(x)>=2]
            best=None
            for tk in sorted(toks,key=len,reverse=True):
                i=pg.find(tk)
                if i>=0: best=i;break
            if best is None: print('  [excerpt not located]',ex[:60]); continue
            if any(abs(best-s)<W for s in shown): continue
            shown.append(best)
            print('  ...',pg[max(0,best-W//2):best+W].replace('\n',' | '))
