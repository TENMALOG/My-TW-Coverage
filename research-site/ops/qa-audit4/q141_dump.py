import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_141.txt', encoding='utf8') if l.strip()]
start, end = int(sys.argv[1]), int(sys.argv[2])
cache = {}


def clean(s):
    s = re.sub(r'[ \t]+', ' ', s)
    return re.sub(r'\n\s*\n+', '\n', s)


for i in ids[start:end]:
    tk = i.split('-AR-')[0]
    if tk not in cache:
        d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
        t = open(d['source']['text_path'], encoding='utf8').read()
        pages = {}
        parts = re.split(r'\[PDF PAGE (\d+)\]', t)
        for k in range(1, len(parts), 2):
            pages[int(parts[k])] = parts[k + 1]
        cache[tk] = (d, pages)
    d, pages = cache[tk]
    f = next(x for x in d['facts'] if x['id'] == i)
    print('=' * 80)
    print(i, d['company'], '|', f['field'], '|', f['period'], '|', f['attribution'], '| page', f['page'])
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
    p = f['page']
    txt = clean(pages.get(p, ''))
    nxt = clean(pages.get(p + 1, ''))
    ex = f['excerpts'][0].strip()[:8].replace(' ', '')
    pos = 0
    # find position in spaced text by scanning
    m = re.search(r'\s*'.join(map(re.escape, ex)), txt)
    if m:
        pos = m.start()
    print('--- page', p, '---')
    print(txt[max(0, pos - 100):pos + 450] if len(txt) > 600 else txt)
    print('--- next ---')
    print(nxt[:80])
