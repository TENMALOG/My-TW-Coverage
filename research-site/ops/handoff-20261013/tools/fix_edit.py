"""Usage: fix_edit.py SCRATCH TAG FIX.json — {id: [new_statement, added_excerpt|null, reason]}. Review fixes: statement rewrites with numbers preserved; optional added excerpt. Appends ovr59.json."""
import json, os, re, sys, datetime
S = sys.argv[1]
D = 'research-site/data/company-facts'
now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
nums = lambda s: sorted(re.findall(r'\d[\d,.]*', s))
FIX = {k: tuple(v) for k, v in json.load(open(sys.argv[3], encoding='utf-8')).items()}
TAG = sys.argv[2]
ovr_path = f'{S}/ovr{TAG}.json'
ovr = json.load(open(ovr_path, encoding='utf-8')) if os.path.exists(ovr_path) else {}
logs = []
for fid, (new, add_ex, reason) in FIX.items():
    p = f'{D}/{fid[:4]}.json'
    d = json.load(open(p, encoding='utf-8'))
    f = next(x for x in d['facts'] if x['id'] == fid)
    old = {k: f[k] for k in ('statement', 'excerpts')}
    assert nums(old['statement']) == nums(new), (fid, nums(old['statement']), nums(new))
    f['statement'] = new
    if add_ex:
        assert add_ex in open(d['source']['text_path'], encoding='utf-8').read(), fid
        f['excerpts'] = f['excerpts'] + [add_ex]
    open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
    logs.append({'ticker': fid[:4], 'id': fid, 'field': 'statement/excerpts', 'old': old,
                 'new': {k: f[k] for k in ('statement', 'excerpts')}, 'reason': reason, 'at': now})
    ovr[fid] = 'ACCEPT|已修正：' + reason
    print(fid, new)
with open(f'{D}/_manual-fixes.jsonl', 'a', encoding='utf-8') as fh:
    for r in logs:
        fh.write(json.dumps(r, ensure_ascii=False) + '\n')
json.dump(ovr, open(ovr_path, 'w', encoding='utf-8'), ensure_ascii=False)
