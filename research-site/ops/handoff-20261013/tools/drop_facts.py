"""Usage: drop_facts.py REASON FACT_ID ... — remove facts from company-facts files (logged)."""
import json, sys, datetime
reason, ids = sys.argv[1], sys.argv[2:]
D = 'research-site/data/company-facts'
now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
logs = []
for fid in ids:
    p = f'{D}/{fid[:4]}.json'
    d = json.load(open(p, encoding='utf-8'))
    f = next(x for x in d['facts'] if x['id'] == fid)
    d['facts'] = [x for x in d['facts'] if x['id'] != fid]
    logs.append({'ticker': fid[:4], 'id': fid, 'field': 'removed', 'old': f, 'new': None, 'reason': reason, 'at': now})
    open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
    print('removed', fid, '|', f['statement'][:60])
with open(f'{D}/_manual-fixes.jsonl', 'a', encoding='utf-8') as fh:
    for r in logs:
        fh.write(json.dumps(r, ensure_ascii=False) + '\n')
