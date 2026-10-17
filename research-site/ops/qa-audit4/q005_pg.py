import json, re, sys
t=sys.argv[1]; p=int(sys.argv[2]); a=int(sys.argv[3]) if len(sys.argv)>3 else 0; n=int(sys.argv[4]) if len(sys.argv)>4 else 80
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8'))
txt=open(d['source']['text_path'],encoding='utf-8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pg={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
L=[l for l in pg[p].split('\n') if l.strip()]
print('\n'.join(L[a:a+n]))
