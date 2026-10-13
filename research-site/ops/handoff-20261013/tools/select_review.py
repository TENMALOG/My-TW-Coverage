"""Usage: select_review.py SCRATCH TICKERFILE TAG NCHUNKS [flag_ticker:field,field ...]
High-risk (market_position, outlook, 自述, 第三方, flagged ticker/fields) all; others 30% random.
Writes review_ids{TAG}_{i}.txt and review_ids{TAG}_random.txt grouped by ticker."""
import json, random, collections, sys
S, tf, tag, n = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
flag = {}
for a in sys.argv[5:]:
    t, _, fs = a.partition(':')
    flag[t] = set(fs.split(',')) if fs else None
T = open(tf).read().split()
high, rest = [], []
for t in T:
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf-8'))
    for f in d['facts']:
        a = f.get('attribution', '')
        hit = f['field'] in ('market_position', 'outlook') or '自述' in a or '第三方' in a
        if t in flag and (flag[t] is None or f['field'] in flag[t]):
            hit = True
        (high if hit else rest).append(f['id'])
random.seed(20261012 + len(tag)); rnd = sorted(random.sample(rest, round(len(rest) * 0.3)))
open(f'{S}/review_ids{tag}_random.txt', 'w').write('\n'.join(rnd) + '\n')
by = collections.defaultdict(list)
for x in high + rnd:
    by[x.split('-')[0]].append(x)
chunks = [[] for _ in range(n)]
for t in sorted(by, key=lambda t: -len(by[t])):
    min(chunks, key=len).extend(by[t])
for i, c in enumerate(chunks, 1):
    open(f'{S}/review_ids{tag}_{i}.txt', 'w').write('\n'.join(sorted(c, key=lambda x: (x[:4], int(x.split('-')[-1])))) + '\n')
print('facts', len(high) + len(rest), 'high', len(high), 'random', len(rnd), 'chunks', [len(c) for c in chunks])
