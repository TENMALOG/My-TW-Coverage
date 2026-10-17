import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
R='./'
items=json.load(open(R+'research-site/ops/qa-audit4/emp_in_3.json',encoding='utf-8'))
cache={}
KW=re.compile(r'母公司|合併|子公司|本公司|台灣|臺灣|國內|外籍|不含|含|集團|分公司|海外|大陸|中國|越南|泰國|馬來|工廠|廠')
out=[]
for it in items:
    tk=it['id'].split('-')[0]
    d=json.load(open(R+f'research-site/data/company-facts/{tk}.json',encoding='utf-8'))
    f=[x for x in d['facts'] if x['id']==it['id']][0]
    tp=d['source']['text_path']
    if tp not in cache: cache[tp]=open(R+tp,encoding='utf-8').read()
    s=cache[tp]
    def page(n):
        m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)'%n,s,re.S)
        return m.group(1) if m else ''
    txt=page(f['page'])+'\n--NEXT--\n'+page(f['page']+1)
    # locate heading
    hs=[m.start() for m in re.finditer(r'從業員工|從 業 員 工|員工資料|員工人數',txt)]
    last=f['excerpts'][-1]
    nums=re.findall(r'\d[\d,\.]*',last)
    pos=-1
    if nums:
        key=nums[0]
        # find the total row
        m=re.search(re.escape(last.split()[0])+r'.{0,3}'+re.escape(nums[0]),txt)
        pos=m.start() if m else txt.find(nums[0])
    hh=[h for h in hs if h<=max(pos,0)]
    st=hh[-1] if hh else max(pos-600,0)
    seg=txt[st:max(pos,st)+40] if pos>=0 else txt[st:st+800]
    seg=re.sub(r'\n+','|',seg)
    print('==',it['id'],d['company'],'|',f['statement'],'|',f['period'])
    print(seg[-420:] if len(seg)>420 else seg)
    after=txt[pos:pos+700] if pos>=0 else ''
    lines=[l for l in after.split('\n')[1:12] if KW.search(l) and not re.search(r'平均|碩士|博士|大專|高中',l)]
    if lines: print('AFTER:',' / '.join(lines)[:400])
