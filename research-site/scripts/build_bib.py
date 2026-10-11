"""Build the CSL-JSON bibliography and the reference map used by filters/refs.lua.

Inputs: verified-facts.jsonl, fy2025-metrics.json, fy2025-financials.json, relations.csv.
Outputs:
  references/aerospace-defense.json   CSL-JSON items (one per source URL, www-normalised)
  data/aerospace-defense/ref-map.json  marker → [{key, locator}] for every 〔…〕 marker id

  python research-site/scripts/build_bib.py
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / 'research-site'
DATA = SITE / 'data/aerospace-defense'
MOPS = ROOT / 'audit-v5/source-cache/research-site/mops-annual'
TICKERS = ['2208', '2630', '2634', '2644', '2645', '4541', '4546', '4572', '6753', '8222']

PUBLISHER = {  # registrable domain → institution shown as author
    'moneydj.com': '嘉實資訊（MoneyDJ）', 'moea.gov.tw': '經濟部國營事業管理司', 'aidc.com.tw': '漢翔航空工業',
    'twse.com.tw': '臺灣證券交易所', 'cna.com.tw': '中央通訊社', 'ye-fong.com': '燁鋒輕合金',
    'rxweb-prd.com': 'Fastener + Fixing Magazine', 'indsr.org.tw': '國防安全研究院', 'tpex.org.tw': '證券櫃檯買賣中心',
    'kcg.gov.tw': '高雄市工商發展投資策進會', 'jongshyn.com': '中信造船', 'ida.gov.tw': '經濟部產業發展署',
    'drewloong.com.tw': '駐龍精密機械', 'taia.org.tw': '台灣航太產業發展協會', 'yuanta-consulting.com.tw': '元大投顧',
    'udn.com': '經濟日報', 'cnyes.com': '鉅亨網', 'maicl.com': '晟田科技工業', 'chaheng.com': '長亨精密',
    'aerowin.com': '寶一科技', 'airasia.com.tw': '亞洲航空', 'tacaviation.com.tw': '台翔航太', 'mnd.gov.tw': '國防部',
    'lungteh.com': '龍德造船工業',
}
LEGAL = {'2208': '台灣國際造船股份有限公司', '2630': '亞洲航空股份有限公司', '2634': '漢翔航空工業股份有限公司',
         '2644': '中信造船股份有限公司', '2645': '長榮航太科技股份有限公司', '4541': '晟田科技工業股份有限公司',
         '4546': '長亨精密股份有限公司', '4572': '駐龍精密機械股份有限公司', '6753': '龍德造船工業股份有限公司',
         '8222': '寶一科技股份有限公司'}
T163 = 'https://mopsov.twse.com.tw/mops/web/ajax_t163sb04'


def jsonl(p):
    return [json.loads(l) for l in Path(p).read_text(encoding='utf-8').splitlines() if l.strip()]


def norm_url(u):
    return re.sub(r'^https?://www\.', 'https://', u.replace('http://', 'https://'))


def publisher(u):
    host = urlparse(u).hostname or ''
    for dom, name in PUBLISHER.items():
        if host == dom or host.endswith('.' + dom):
            return name
    return host


def key_for(u):
    m = re.search(r'co_id=(\d{4})&filename=(\d{4})_', u)
    if m:
        return f'ar{m.group(2)}-{m.group(1)}'
    if u.startswith(T163):
        return 'mops-t163sb04'
    return 'src-' + hashlib.sha256(norm_url(u).encode()).hexdigest()[:8]


def issued(date):
    if not date:
        return None
    parts = [int(p) for p in re.findall(r'\d+', date)[:3]]
    return {'date-parts': [parts]} if parts else None


def ar_print_date(tk):
    meta = json.loads((MOPS / f'{tk}_2025_F04.json').read_text(encoding='utf-8'))
    t = re.sub(r'\s+', '', (ROOT / meta['text_path']).read_text(encoding='utf-8')[:6000])
    m = re.search(r'中華民國(1\d\d)年(\d{1,2})月(\d{1,2})日', t)
    return (f'{int(m.group(1)) + 1911}-{int(m.group(2)):02d}-{int(m.group(3)):02d}' if m else None), meta


def page_of(locator):
    """'PDF第41、45、47頁' → 'pp. 41, 45, 47'; '第70至71頁' → 'pp. 70–71'."""
    m = re.search(r'第([\d\s、，,至－\-–]+)頁', locator or '')
    if not m:
        return None
    span = m.group(1)
    nums = re.findall(r'\d+', span)
    if not nums:
        return None
    if len(nums) == 2 and re.search(r'[至－\-–]', span):
        return f'pp. {nums[0]}–{nums[1]}'
    return f'p. {nums[0]}' if len(nums) == 1 else 'pp. ' + ', '.join(nums)


def paragraph_map(refmap):
    """Every paragraph that carries a marker → its marker ids and bibliography keys."""
    rows = []
    files = [SITE / 'chapters/industries/aerospace-defense.qmd'] + sorted((SITE / 'chapters/companies').glob('*.qmd'))
    for f in files:
        for i, para in enumerate(re.split(r'\n\s*\n', f.read_text(encoding='utf-8'))):
            ids = []
            for grp in re.findall(r'〔([^〕]+)〕', para):
                for part in re.split(r'[；、]', grp):
                    part = part.strip()
                    m = re.match(r'R(\d+)–R(\d+)$', part)
                    ids += [f'R{j:02d}' for j in range(int(m.group(1)), int(m.group(2)) + 1)] if m else [part]
            if ids:
                keys = sorted({r['key'] for x in ids for r in refmap.get(x, [])})
                rows.append({'file': f.relative_to(SITE).as_posix(), 'paragraph': i,
                             'excerpt': re.sub(r'\s+', ' ', para)[:40], 'markers': ';'.join(ids), 'keys': ';'.join(keys)})
    with open(DATA / 'paragraph-map.csv', 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=['file', 'paragraph', 'excerpt', 'markers', 'keys']); w.writeheader(); w.writerows(rows)
    return len(rows)


def main():
    items, refmap = {}, {}

    def add(url, title, date=None, note=None):
        k = key_for(url)
        if k not in items:
            it = {'id': k, 'type': 'report' if url.lower().endswith('.pdf') or 'filename=' in url else 'webpage',
                  'title': title or url, 'author': [{'literal': publisher(url)}], 'URL': url}
            if issued(date):
                it['issued'] = issued(date)
            if note:
                it['note'] = note
            items[k] = it
        return k

    # annual reports (MOPS)
    for tk in TICKERS:
        d, meta = ar_print_date(tk)
        add(meta['citation_url'], None, d, f'公開資訊觀測站 {meta["filename"]}；快照 SHA256 {meta["text_sha256"][:16]}…')
    add(T163, '綜合損益表彙總報表（第四季，民國113、114年度，上市及上櫃）', '2026',
        '公開資訊觀測站 ajax_t163sb04 查詢結果快照，見 audit-v5/source-cache/research-site/mops-t163sb04/')
    items['mops-t163sb04']['author'] = [{'literal': '公開資訊觀測站'}]

    # facts
    for f in jsonl(DATA / 'verified-facts.jsonl'):
        refs = []
        for c in f['citations']:
            title = c.get('title')
            if 'filename=' in c['url']:
                title = None
            k = add(c['url'], title, c.get('publication_date'))
            if items[k]['title'] == c['url'] and title:
                items[k]['title'] = title
            refs.append({'key': k, 'locator': page_of(c.get('locator'))})
        fid = f['fact_id']
        refmap[fid] = refs
        if fid.startswith('revision'):
            refmap['revision:…' + fid.split(':')[-1][:8]] = refs
    # annual-report titles
    names = {r['ticker']: r['company'] for r in json.loads((DATA / 'fy2025-metrics.json').read_text(encoding='utf-8'))}
    for tk in TICKERS:
        for k, it in items.items():
            if k.startswith('ar2025-' + tk):
                it['title'] = f'{names[tk]} 114 年度（2025 年度）股東會年報'
                it['author'] = [{'literal': LEGAL[tk]}]
                it.setdefault('issued', {'date-parts': [[2026]]})
    # metrics / financials
    metrics = {r['ticker']: r for r in json.loads((DATA / 'fy2025-metrics.json').read_text(encoding='utf-8'))}
    fins = {r['ticker']: r for r in json.loads((DATA / 'fy2025-financials.json').read_text(encoding='utf-8'))}
    for tk, m in metrics.items():
        k = key_for(m['source_url'])
        refmap[f'metric:{tk}'] = [{'key': k, 'locator': f'pp. {m["revenue_page"]}, {m["customer_table_page"]}'}]
        f = fins[tk]
        if '合併綜合損益表彙總' in f['basis']:
            refmap[f'fin:{tk}'] = [{'key': 'mops-t163sb04', 'locator': None}]
        else:
            refmap[f'fin:{tk}'] = [{'key': k, 'locator': f'p. {f["source_2025"]["page"]}'}]
    refmap['metric:各公司'] = [{'key': f'ar2025-{tk}', 'locator': None} for tk in TICKERS]
    refmap['fin:各公司'] = [{'key': 'mops-t163sb04', 'locator': None}, {'key': 'ar2025-2644', 'locator': None},
                          {'key': 'ar2025-4546', 'locator': None}]
    # relations → their evidence
    for r in csv.DictReader(open(DATA / 'relations.csv', encoding='utf-8')):
        ev = r['evidence_ref']
        ev_id = ev if not ev.startswith('revision') else 'revision:…' + ev.split(':')[-1][:8]
        if ev_id not in refmap:
            raise SystemExit(f'{r["relation_id"]}: evidence {ev} unresolved')
        refmap[r['relation_id']] = refmap[ev_id]
    (SITE / 'references').mkdir(exist_ok=True)
    (SITE / 'references/aerospace-defense.json').write_text(json.dumps(list(items.values()), ensure_ascii=False, indent=1), encoding='utf-8')
    (DATA / 'ref-map.json').write_text(json.dumps(refmap, ensure_ascii=False, indent=1), encoding='utf-8')
    n = paragraph_map(refmap)
    print(f'{len(items)} bibliography items, {len(refmap)} marker ids, {n} mapped paragraphs')


if __name__ == '__main__':
    main()
