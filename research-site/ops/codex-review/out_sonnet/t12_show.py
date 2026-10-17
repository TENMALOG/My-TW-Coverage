import json,sys,re
job=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3])
F='research-site/ops/codex-review/'
ids=open(F+f'jobs_sonnet/{job}.txt',encoding='utf8').read().split()
for n,id in enumerate(ids[a:b],a):
    t=id.split('-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    facts=d['facts'] if isinstance(d,dict) and 'facts' in d else d
    f=[x for x in facts if x.get('id')==id][0]
    tp=f.get('source',{}).get('text_path') if isinstance(f.get('source'),dict) else None
    if not tp: tp=d.get('source',{}).get('text_path')
    txt=open(tp,encoding='utf8').read()
    pg=f.get('page')
    pat=r'\[PDF PAGE %s\](.*?)(?=\[PDF PAGE |\Z)'%pg
    m=re.search(pat,txt,re.S); p=m.group(1) if m else ''
    m2=re.search(r'\[PDF PAGE %s\](.*?)(?=\[PDF PAGE |\Z)'%(pg+1),txt,re.S); p2=m2.group(1) if m2 else ''
    full=p+'\n<<NEXT>>\n'+p2
    exs=f.get('excerpts') or []
    pos=[];
    for e in exs:
        i=full.find(e[:25]); 
        if i>=0: pos.append((i,i+len(e)))
    print('=====',n,id,f.get('field'),'|',f.get('period'),'|p',pg,'|',f.get('attribution'))
    print('S:',f['statement'])
    print('X:',exs)
    if pos:
        lo=max(0,min(x for x,_ in pos)-120); hi=max(y for _,y in pos)+120
        if hi-lo>900: hi=lo+900
        print('CTX:',full[lo:hi].replace('\n',' | '))
    else: print('CTX(nopos):',full[:1500].replace('\n',' | '))
