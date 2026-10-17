import json, sys
job = sys.argv[1]
base = 'research-site/ops/codex-review/'
ids = [l.strip() for l in open(base + 'jobs_sonnet/%s.txt' % job, encoding='utf8') if l.strip()]
v = {}
for l in open(base + 'out_sonnet/t13_%s_v.txt' % job, encoding='utf8'):
    l = l.rstrip('\n')
    if not l.strip(): continue
    r, vd, reason = l.split(' ', 2)
    a, _, b = r.partition('-'); b = b or a
    for i in range(int(a), int(b) + 1):
        v[i] = ('ACCEPT' if vd == 'A' else 'REJECT', reason)
missing = [i for i in range(len(ids)) if i not in v]
if missing: print('MISSING', missing); sys.exit(1)
with open(base + 'out_sonnet/%s.jsonl' % job, 'w', encoding='utf8') as f:
    for i, fid in enumerate(ids):
        f.write(json.dumps({'id': fid, 'verdict': v[i][0], 'reason': v[i][1]}, ensure_ascii=False) + '\n')
print(job, len(ids), 'ACCEPT', sum(1 for i in v.values() if i[0]=='ACCEPT'), 'REJECT', sum(1 for i in v.values() if i[0]=='REJECT'))
for i in sorted(v):
    if v[i][0]=='REJECT': print('  R', ids[i], v[i][1])
