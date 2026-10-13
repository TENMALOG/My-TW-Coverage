"""Usage: merge_review.py SCRATCH TAG OVERRIDES_JSON
OVERRIDES_JSON: {"id": "ACCEPT|reason" or "REJECT|reason"} written as 總經理改判.
Prints random / high-risk reject rates (subagent verdicts) and appends all to the ledger."""
import json, glob, sys, datetime
S, tag, ov = sys.argv[1], sys.argv[2], sys.argv[3]
OVR = json.load(open(ov, encoding='utf-8')) if ov != '-' else {}
LEDGER = 'research-site/data/company-facts/_semantic-review.jsonl'
now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
recs = {}
for p in sorted(glob.glob(f'{S}/semantic_review{tag}_*.jsonl')):
    for line in open(p, encoding='utf-8'):
        if line.strip():
            r = json.loads(line); recs[r['id']] = r
rnd = set(open(f'{S}/review_ids{tag}_random.txt').read().split())
sel = set()
for p in glob.glob(f'{S}/review_ids{tag}_[0-9]*.txt'):
    sel |= set(open(p).read().split())
print('selected', len(sel), 'reviewed', len(recs), 'missing', sorted(sel - set(recs)))
for name, ids in (('random', sorted(rnd)), ('high-risk', sorted(sel - rnd))):
    rj = [i for i in ids if recs.get(i, {}).get('verdict') == 'REJECT']
    print('%s reject %d/%d = %.1f%%' % (name, len(rj), len(ids), 100 * len(rj) / max(1, len(ids))), rj)
with open(LEDGER, 'a', encoding='utf-8') as fh:
    for i, r in recs.items():
        fh.write(json.dumps({'id': i, 'verdict': r['verdict'], 'reason': r.get('reason', ''), 'reviewer': 'Claude Sonnet 子代理', 'reviewed_at': now}, ensure_ascii=False) + '\n')
    for i, v in OVR.items():
        verdict, reason = v.split('|', 1)
        fh.write(json.dumps({'id': i, 'verdict': verdict, 'reason': reason, 'reviewer': '總經理（Claude Opus）改判', 'reviewed_at': now}, ensure_ascii=False) + '\n')
final = {i: r['verdict'] for i, r in recs.items()}
final.update({i: v.split('|')[0] for i, v in OVR.items()})
print('final REJECT', sorted(i for i, v in final.items() if v == 'REJECT'))
