"""Usage: fix_replace.py SCRATCH TAG OLD NEW REASON OK FACT_ID ... — replace OLD with NEW (once) in each
statement; numbers must stay identical. Appends ACCEPT|OK overrides to ovr{TAG}.json."""
import json, os, re, sys, datetime
S, tag, a, b, reason, ok, ids = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7:]
D = 'research-site/data/company-facts'
now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
ovr_path = f'{S}/ovr{tag}.json'
ovr = json.load(open(ovr_path, encoding='utf-8')) if os.path.exists(ovr_path) else {}
nums = lambda s: re.findall(r'\d[\d,.]*', s)
logs = []
for fid in ids:
    p = f'{D}/{fid[:4]}.json'
    d = json.load(open(p, encoding='utf-8'))
    f = next(x for x in d['facts'] if x['id'] == fid)
    old = f['statement']
    new = old.replace(a, b, 1)
    assert new != old and nums(old) == nums(new), fid
    f['statement'] = new
    logs.append({'ticker': fid[:4], 'id': fid, 'field': 'statement', 'old': old, 'new': new, 'reason': reason, 'at': now})
    ovr[fid] = 'ACCEPT|' + ok
    open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
    print(fid, '|', new)
with open(f'{D}/_manual-fixes.jsonl', 'a', encoding='utf-8') as fh:
    for r in logs:
        fh.write(json.dumps(r, ensure_ascii=False) + '\n')
json.dump(ovr, open(ovr_path, 'w', encoding='utf-8'), ensure_ascii=False)
