import json,re,sys
sys.stdout.reconfigure(encoding='utf-8')
fid=sys.argv[1]; key=sys.argv[2]; n=int(sys.argv[3])
tk=fid.split('-')[0]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf-8'))
f=[x for x in d['facts'] if x['id']==fid][0]
s=open(d['source']['text_path'],encoding='utf-8').read()
m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)'%f['page'],s,re.S)
t=m.group(1); i=t.find(key)
print(re.sub(r'\n+','|',t[max(0,i-100):i+n]))
