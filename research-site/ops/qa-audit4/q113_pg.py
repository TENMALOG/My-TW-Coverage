import json,re,sys
t_,p_,pat=sys.argv[1],int(sys.argv[2]),(sys.argv[3] if len(sys.argv)>3 else '')
a=int(sys.argv[4]) if len(sys.argv)>4 else 12
d=json.load(open(f'research-site/data/company-facts/{t_}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
pp=re.split(r'\[PDF PAGE (\d+)\]',t)
pg={int(pp[i]):pp[i+1] for i in range(1,len(pp),2)}
L=[l for l in pg[p_].split('\n') if l.strip()]
if not pat: print('\n'.join(L))
else:
    idx=[n for n,l in enumerate(L) if re.search(pat,l)]
    out=sorted({m for n in idx for m in range(max(0,n-3),min(len(L),n+a))})
    print('\n'.join(L[m] for m in out))
