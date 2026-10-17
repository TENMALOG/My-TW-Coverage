import json, sys
root = r"C:\Users\Neo Pegasus\Documents\ChatGPT\078-kaori sample\artifacts\stock-coverage-audit-20261003\incoming\latest-audit\My-TW-Coverage\research-site\ops\codex-review"
job = sys.argv[1]
ids = [l.strip() for l in open(f"{root}/jobs_sonnet/{job}.txt", encoding="utf-8") if l.strip()]
notes = {}
for l in open(f"{root}/out_sonnet/s04_notes_{job}.txt", encoding="utf-8"):
    l = l.strip()
    if not l:
        continue
    i, v, r = l.split("|", 2)
    notes[i] = (v, r)
missing = [i for i in ids if i not in notes]
extra = [i for i in notes if i not in ids]
if missing or extra:
    print("MISSING", missing, "EXTRA", extra)
    sys.exit(1)
with open(f"{root}/out_sonnet/{job}.jsonl", "w", encoding="utf-8", newline="\n") as f:
    for i in ids:
        v, r = notes[i]
        f.write(json.dumps({"id": i, "verdict": "ACCEPT" if v == "A" else "REJECT", "reason": r}, ensure_ascii=False) + "\n")
acc = sum(1 for i in ids if notes[i][0] == "A")
print(job, "total", len(ids), "ACCEPT", acc, "REJECT", len(ids) - acc)
for i in ids:
    if notes[i][0] == "R":
        print("  R", i, notes[i][1])
