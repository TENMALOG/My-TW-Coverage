import json,re
specs=[("6640",61,"AOI",800),("6668",58,"2026 年起",500),("6671",88,"控股公司",900),("9938",103,"黏扣帶",900),("9962",90,"不銹鋼板",600),("6614",59,"客製化",300),("6614",64,"短期業務發展",300),("6887",68,"僅四家",500)]
for t,p,k,w in specs:
    d=json.load(open(f"data/company-facts/{t}.json",encoding="utf-8"))
    tp="../"+d["source"]["text_path"] if not __import__("os").path.exists(d["source"]["text_path"]) else d["source"]["text_path"]
    import os
    for cand in [d["source"]["text_path"],"../"+d["source"]["text_path"],"../../"+d["source"]["text_path"]]:
        if os.path.exists(cand): tp=cand;break
    txt=open(tp,encoding="utf-8").read()
    pages=re.split(r"\f",txt)
    print("=====",t,p,len(pages),tp)
    for pg in (p-1,p):
        s=pages[pg-1] if pg-1<len(pages) else ""
        i=s.find(k)
        if i>=0: print("--page",pg); print(s[max(0,i-w//2):i+w])
