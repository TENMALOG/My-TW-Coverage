import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
R = 'C:/Users/Neo Pegasus/Documents/ChatGPT/078-kaori sample/artifacts/stock-coverage-audit-20261003/incoming/latest-audit/My-TW-Coverage/'
items = json.load(open(R + 'research-site/ops/codex-review/adj_1.json', encoding='utf-8'))
a, b = int(sys.argv[1]), int(sys.argv[2])
W = int(sys.argv[3]) if len(sys.argv) > 3 else 700
cache = {}
for it in items[a:b]:
    tk = it['id'].split('-')[0]
    d = json.load(open(R + f'research-site/data/company-facts/{tk}.json', encoding='utf-8'))
    f = [x for x in d['facts'] if x['id'] == it['id']][0]
    tp = d['source']['text_path']
    if tp not in cache:
        cache[tp] = open(R + tp, encoding='utf-8').read()
    s = cache[tp]
    pg = f['page']
    def page(n):
        m = re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)' % n, s, re.S)
        return m.group(1) if m else ''
    txt = page(pg) + '\n--NEXTPAGE--\n' + page(pg + 1)
    print('=' * 80)
    print(it['id'], d['company'])
    print('REVIEWER:', it['reviewer_reason'])
    print('STMT:', f['statement'])
    print('PERIOD:', f['period'], 'PAGE', pg, 'ATTR:', f['attribution'])
    print('EXCERPTS:', json.dumps(f['excerpts'], ensure_ascii=False))
    # window around first excerpt
    ex = f['excerpts'][0].strip()
    key = ex[:12]
    i = txt.find(key)
    if i < 0:
        nums = re.findall(r'[\d,\.]{3,}', ' '.join(f['excerpts']))
        for n in nums:
            i = txt.find(n)
            if i >= 0:
                break
    if i < 0:
        i = 0
    print('TEXT[%d:%d of %d]:' % (max(0, i - 300), i + W, len(txt)))
    print(txt[max(0, i - 300):i + W])
