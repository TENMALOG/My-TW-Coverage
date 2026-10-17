import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
R='./'
items=json.load(open(R+'research-site/ops/qa-audit4/emp_in_3.json',encoding='utf-8'))
KW=re.compile(r'母公司|合併|子公司|集團|台灣|臺灣|不含|不包含|含|本公司|國內|海外|大陸|分公司|外籍|境外|境內|包括|包含|工廠|廠')
for it in items:
    tk=it['id'].split('-')[0]
    d=json.load(open(R+f'research-site/data/company-facts/{tk}.json',encoding='utf-8'))
    f=[x for x in d['facts'] if x['id']==it['id']][0]
    s=open(R+d['source']['text_path'],encoding='utf-8').read()
    def page(n):
        m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)'%n,s,re.S)
        return m.group(1) if m else ''
    t=page(f['page'])
    # find all heading candidates "從業員工|從業人員|員工資料"
    ms=[m.start() for m in re.finditer(r'從\s*業\s*(員\s*工|人\s*員)',t)]
    hits=[]
    for st in ms:
        end=t.find('環保',st)
        seg=t[st:end if end>st else st+1200]
        # exclude table rows: only lines w/o digits-heavy
        for l in seg.split('\n'):
            if KW.search(l) and not re.search(r'最近二年度及截至年報刊印日止|環保',l): hits.append(l.strip()[:90])
    print(it['id'],'|',' // '.join(hits)[:300] if hits else 'NOSCOPE')
