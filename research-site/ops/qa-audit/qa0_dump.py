import json, re, sys
root = r"C:/Users/Neo Pegasus/Documents/ChatGPT/078-kaori sample/artifacts/stock-coverage-audit-20261003/incoming/latest-audit/My-TW-Coverage/"
ids = [l.strip() for l in open(root + "research-site/ops/qa-audit/ids_0.txt", encoding="utf8") if l.strip()]
a, b = int(sys.argv[1]), int(sys.argv[2])
maxc = int(sys.argv[3]) if len(sys.argv) > 3 else 2500
cache = {}
for i in ids[a:b]:
    t = i.split("-")[0]
    d = json.load(open(root + f"research-site/data/company-facts/{t}.json", encoding="utf8"))
    f = next(x for x in d["facts"] if x["id"] == i)
    p = f["page"]
    tp = d["source"]["text_path"]
    if tp not in cache:
        cache[tp] = open(root + tp, encoding="utf8").read()
    txt = cache[tp]
    pages = re.split(r"\[PDF PAGE (\d+)\]", txt)
    pm = {int(pages[k]): pages[k + 1] for k in range(1, len(pages) - 1, 2)}
    print("=" * 80)
    print(i, d["company"], f["field"], "| period:", f["period"], "| attr:", f["attribution"], "| page", p)
    print("STMT:", f["statement"])
    print("EXC:", json.dumps(f["excerpts"], ensure_ascii=False))
    # locate first excerpt in page; show window
    pg = pm.get(p, "")
    ex = f["excerpts"][0]
    pos = pg.find(ex)
    if pos < 0:
        pos = 0
    s = max(0, pos - 250)
    print("--PAGE", p, "window:")
    print(pg[s:s + maxc])
    nx = pm.get(p + 1, "")
    print("--PAGE+1 head:")
    print(nx[:150])
