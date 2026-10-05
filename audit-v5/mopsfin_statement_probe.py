from __future__ import annotations
import html, json, re, time, urllib.parse, urllib.request
from pathlib import Path
from bs4 import BeautifulSoup

URL="https://mopsfin.twse.com.tw/compare/report"

def fetch(period):
    pairs=[
      ("compareItem","IncomeStatement"),("ylabel","新台幣仟元"),
      ("quarter","true"),("revenue","true"),("ys",period),
      ("qnumber",""),("bcodeAvg","false"),("companyAvg","false"),
      ("companyId","1304 台聚"),
    ]
    body=urllib.parse.urlencode(pairs).encode()
    req=urllib.request.Request(URL,data=body,method="POST",headers={
      "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
      "Origin":"https://mopsfin.twse.com.tw","Referer":"https://mopsfin.twse.com.tw/",
      "X-Requested-With":"XMLHttpRequest","User-Agent":"My-TW-Coverage-audit-v5/1.0",
    })
    last=None
    for attempt in range(4):
      try:
        with urllib.request.urlopen(req,timeout=60) as r:
          return r.read().decode("utf-8",errors="replace")
      except Exception as e:
        last=e
        time.sleep(1+attempt)
    raise last

def clean(raw):
    raw=re.sub(r"<script[\s\S]*?</script>"," ",raw,flags=re.I)
    raw=re.sub(r"<style[\s\S]*?</style>"," ",raw,flags=re.I)
    raw=re.sub(r"<[^>]+>"," | ",raw)
    return re.sub(r"\s+"," ",html.unescape(raw))

out={}
for period in ["20261","20262","20254"]:
    raw=fetch(period)
    txt=clean(raw)
    soup=BeautifulSoup(raw,"html.parser")
    target_rows=[]
    for tr in soup.find_all("tr"):
        cells=[c.get_text(" ",strip=True) for c in tr.find_all(["th","td"],recursive=False)]
        if cells and any(("母公司業主" in x or "本期淨利" in x or "營業利益" in x) for x in cells):
            target_rows.append(cells)
    snippets=[]
    for needle in ["歸屬於母公司業主","本期淨利","營業利益","營業毛利","營業收入"]:
      i=txt.find(needle)
      snippets.append({"needle":needle,"snippet":txt[max(0,i-200):i+500] if i>=0 else None})
    out[period]={"length":len(raw),"target_rows":target_rows,"snippets":snippets}
path=Path("audit-v5/generated/mopsfin-statement-probe.json")
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,ensure_ascii=False,indent=2))
