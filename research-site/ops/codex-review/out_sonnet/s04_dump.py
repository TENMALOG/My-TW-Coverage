import json, re, sys, os
root = r"C:\Users\Neo Pegasus\Documents\ChatGPT\078-kaori sample\artifacts\stock-coverage-audit-20261003\incoming\latest-audit\My-TW-Coverage"
job, start, end = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
ids = [l.strip() for l in open(f"{root}/research-site/ops/codex-review/jobs_sonnet/{job}.txt", encoding="utf-8") if l.strip()]
cache = {}
def pages(t):
    if t not in cache:
        txt = open(f"{root}/{t}", encoding="utf-8").read()
        parts = re.split(r"\[PDF PAGE (\d+)\]", txt)
        d = {}
        for i in range(1, len(parts), 2):
            d[int(parts[i])] = parts[i + 1]
        cache[t] = d
    return cache[t]
def clean(s):
    s = re.sub(r"[ \t]+", " ", s)
    return re.sub(r"\n\s*\n+", "\n", s)
fc = {}
for i in ids[start:end]:
    tk = i.split("-")[0]
    if tk not in fc:
        fc[tk] = json.load(open(f"{root}/research-site/data/company-facts/{tk}.json", encoding="utf-8"))
    d = fc[tk]
    f = [x for x in d["facts"] if x["id"] == i][0]
    pg = pages(d["source"]["text_path"])
    p = f["page"]
    print("=" * 60)
    print(i, d["company"], "|", f["field"], "|", f["attribution"], "|", f["period"], "| p", p)
    print("STMT:", f["statement"])
    for e in f["excerpts"]:
        print("  EX:", e)
    flat = clean(pg.get(p, ""))
    def pos(e):
        for n in (len(e), 20, 10):
            k = flat.find(e[:n])
            if k >= 0:
                return k
        return -1
    ks = [pos(e) for e in f["excerpts"]]
    ks = [k for k in ks if k >= 0]
    if ks:
        a = max(0, min(ks) - 330)
        b = min(len(flat), max(ks) + len(f["excerpts"][-1]) + 250)
        if b - a > 1300:
            b = a + 1300
        w = flat[a:b]
        if (tk, p) == globals().get("_last") and w[:300] == globals().get("_lw"):
            print("CTX: (same page window as previous fact)")
        else:
            print("CTX:", w)
        _last = (tk, p); _lw = w[:300]
    else:
        print("EXCERPT NOT LOCATED; PAGE:", flat[:1200])
        print("NEXT:", re.sub(r"\s+", " ", clean(pg.get(p + 1, "")))[:600])
