import sys, json
F = r"C:\Users\Neo Pegasus\Documents\ChatGPT\078-kaori sample\artifacts\stock-coverage-audit-20261003\incoming\latest-audit\My-TW-Coverage\research-site\ops\codex-review"
job = sys.argv[1]
ids = [l.strip() for l in open(f"{F}/jobs_sonnet/{job}.txt", encoding="utf8") if l.strip()]
v = {}
for l in open(f"{F}/out_sonnet/s02_v_{job}.txt", encoding="utf8"):
    l = l.rstrip("\n")
    if not l: continue
    i, x, r = l.split("|", 2)
    v[i] = (x, r)
miss = [i for i in ids if i not in v]
if miss: print("MISSING", job, miss); sys.exit(1)
extra = [i for i in v if i not in ids]
if extra: print("EXTRA", extra); sys.exit(1)
n = {"A": 0, "R": 0}
with open(f"{F}/out_sonnet/{job}.jsonl", "w", encoding="utf8") as o:
    for i in ids:
        x, r = v[i]; n[x] += 1
        o.write(json.dumps({"id": i, "verdict": "ACCEPT" if x == "A" else "REJECT", "reason": r}, ensure_ascii=False) + "\n")
print(job, "ACCEPT", n["A"], "REJECT", n["R"])
for i in ids:
    if v[i][0] == "R": print("  ", i, v[i][1])
