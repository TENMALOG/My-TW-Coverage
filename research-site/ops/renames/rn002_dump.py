import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research-site" / "scripts" / "annual"))
from slice_annual import page_texts

jobs = json.load(open(ROOT / "research-site/ops/renames/jobs/rn_002.json", encoding="utf8"))
a, b = int(sys.argv[1]), int(sys.argv[2])
KW = re.compile(r"更名|改名|原名|更改名稱|名稱變更|變更名稱|改稱|更改公司名稱|變更公司名稱|名稱為|原稱|易名")
W = int(sys.argv[3]) if len(sys.argv) > 3 else 220
for e in jobs[a:b]:
    t = e["id"]
    f = json.load(open(ROOT / f"research-site/data/company-facts/{t}.json", encoding="utf8"))
    tp = f["source"]["text_path"]
    p = Path(tp)
    if not p.is_absolute():
        p = ROOT / tp
    pages = page_texts(p.read_text(encoding="utf8"))
    print("=" * 10, t, e["company"], e["legal_name"])
    for h in e["hits"]:
        pg = pages.get(h["page"], "")
        pg = re.sub(r"\s+", " ", pg)
        last = -1
        for m in KW.finditer(pg):
            if m.start() < last:
                continue
            s = max(0, m.start() - W)
            en = min(len(pg), m.end() + W)
            last = en
            print(f"[p{h['page']}] ...{pg[s:en]}...")
