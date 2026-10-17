import json,re,sys
fid=sys.argv[1]; pre=int(sys.argv[2]) if len(sys.argv)>2 else 0; n=int(sys.argv[3]) if len(sys.argv)>3 else 1800
t=fid.split('-')[0]
d=json.load(open('research-site/data/company-facts/%s.json'%t,encoding='utf8'))
f=[x for x in d['facts'] if x['id']==fid][0]
txt=open(d['source']['text_path'],encoding='utf8').read()
m=re.search(r'\[PDF PAGE %d\]'%f['page'],txt)
pg=txt[m.start():m.start()+12000]
e=re.sub(r'\s+','',f['excerpts'][-1])
idx=[j for j,c in enumerate(pg) if not c.isspace()]
s=''.join(pg[j] for j in idx)
k=s.find(e[:10]); k=idx[k] if k>=0 else 0
print(fid, re.sub(r'\s*\n\s*',' / ',pg[max(0,k-pre):k+n]))
