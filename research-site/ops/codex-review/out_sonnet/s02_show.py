import json, re, sys, os
ROOT = r"C:\Users\Neo Pegasus\Documents\ChatGPT\078-kaori sample\artifacts\stock-coverage-audit-20261003\incoming\latest-audit\My-TW-Coverage"
F = ROOT + r"\research-site\ops\codex-review"
job, start, end = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
W = int(sys.argv[4]) if len(sys.argv) > 4 else 220
ids = [l.strip() for l in open(f"{F}/jobs_sonnet/{job}.txt", encoding="utf8") if l.strip()]
cache = {}
def pages(path):
    if path not in cache:
        t = open(os.path.join(ROOT, path), encoding="utf8").read()
        parts = re.split(r"\[PDF PAGE (\d+)\]", t)
        d = {}
        for i in range(1, len(parts), 2):
            d[int(parts[i])] = parts[i + 1]
        cache[path] = d
    return cache[path]
def norm(txt):
    idx = [i for i, c in enumerate(txt) if not c.isspace()]
    return "".join(txt[i] for i in idx), idx
for i in ids[start:end]:
    tk = i.split("-")[0]
    d = json.load(open(f"{ROOT}/research-site/data/company-facts/{tk}.json", encoding="utf8"))
    f = next(x for x in d["facts"] if x["id"] == i)
    pg = pages(d["source"]["text_path"])
    print("=" * 60)
    print(i, d.get("company"), "|", f["field"], "| p", f["page"], "|", f["period"], "|", f["attribution"])
    print("STMT:", f["statement"])
    print("EXC:", " || ".join(f["excerpts"]))
    rngs = {}
    for e in f["excerpts"]:
        en = "".join(e.split())
        for p in (f["page"], f["page"] + 1):
            txt = pg.get(p, "")
            n, idx = norm(txt)
            k = n.find(en)
            if k >= 0:
                a = idx[k]; b = idx[min(len(idx) - 1, k + len(en) - 1)]
                rngs.setdefault(p, []).append((max(0, a - W), min(len(txt), b + W)))
                break
        else:
            print("!! excerpt not found:", e)
    for p, rng in rngs.items():
        rng.sort(); m = []
        for a, b in rng:
            if m and a <= m[-1][1]: m[-1] = (m[-1][0], max(m[-1][1], b))
            else: m.append((a, b))
        for a, b in m:
            print(f"--[p{p}]--")
            print(re.sub(r"\n\s*\n+", "\n", pg[p][a:b]))
