"""Export the verified research data the explore-layer demo renders (no new facts are created here).

  py explore-demo/scripts/export_data.py

Writes explore-demo/src/data/:
  companies.json   one record per company: name, legal name, industry (corrected) + 證交所產業別, Shorts script
                   (hook/what/mix/regions/cards, all validated against annual-report facts), FY2024/2025 revenue
                   and gross margin, listed counterparties, and a `sources` map fact id -> {page, period, url}
  industries.json  slug, name, company count, tickers
Every number shown by the demo comes from these records, and every card carries the fact ids it rests on.
"""
import csv
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / 'research-site'
OUT = ROOT / 'explore-demo/src/data'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    names = {r['industry_folder']: r for r in csv.DictReader(open(SITE / 'data/industry-names.csv', encoding='utf-8-sig'))}
    cat = list(csv.DictReader(open(SITE / 'catalog/release-scope-companies.csv', encoding='utf-8-sig')))
    basic = {json.loads(l)['ticker']: json.loads(l) for l in open(SITE / 'data/basic-data.jsonl', encoding='utf-8')}
    fixes = {r['ticker']: r for r in csv.DictReader(open(SITE / 'data/industry-corrections.csv', encoding='utf-8-sig'))}
    # YouTube video ids filled in after upload (ticker,youtube_id); pages embed the upload, else show the poster
    yt = {r['ticker']: r['youtube_id'].strip() for r in csv.DictReader(open(SITE / 'data/youtube-ids.csv', encoding='utf-8-sig'))
          if r.get('youtube_id', '').strip()}
    posters = ROOT / 'research-site/ops/shorts/out/master'
    pub = ROOT / 'explore-demo/public/poster'
    pub.mkdir(parents=True, exist_ok=True)
    # the page shows only the 1:1 core of the 9:16 frame (y 280-1360), so ship a small square WebP, not the 1080x1920 JPEG
    from PIL import Image
    for f in posters.glob('*_poster.jpg'):
        dst = pub / f.name.replace('_poster.jpg', '.webp')
        if dst.exists() and dst.stat().st_mtime >= f.stat().st_mtime:
            continue
        im = Image.open(f).convert('RGB')
        k = im.width / 1080
        im.crop((0, round(280 * k), im.width, round(1360 * k))).resize((560, 560), Image.LANCZOS).save(dst, 'WEBP', quality=82, method=6)
    # why a company has no financial chart: the MOPS summary has it in a non-standard format, or not at all
    fin_all = {r['ticker']: r for r in json.loads((SITE / 'data/financials/fy2025-financials-all.json').read_text(encoding='utf-8'))}
    sys.path.insert(0, str(SITE / 'scripts/generic'))
    import build_company_pages_p2 as p2

    p2_rows = p2.p2_companies()
    p2_tickers = {r['ticker'] for r in p2_rows}
    assert not p2_tickers.intersection(r['ticker'] for r in cat), 'P2 overlaps the catalog'
    directory = {r['ticker']: r for r in json.loads(p2.DIRECTORY.read_text(encoding='utf-8'))['companies']}
    code_names, isin_only = p2.industry_names_official(directory)
    by_name = {v: k for k, v in code_names.items()}
    fin_p2 = p2.load_financials()
    comps, inds = [], {}
    for r in cat + p2_rows:
        tk = r['ticker']
        is_p2 = tk in p2_tickers
        if is_p2 and tk in p2.UNRESOLVED:
            continue
        sb_p = ROOT / 'research-site/ops/shorts/storyboard' / f'{tk}.json'
        base_p = ROOT / 'research-site/ops/shorts/base' / f'{tk}.json'
        if not sb_p.exists() or not base_p.exists():
            continue
        sb = json.loads(sb_p.read_text(encoding='utf-8'))
        base = json.loads(base_p.read_text(encoding='utf-8'))
        kind = base['source'].get('kind', 'annual') if is_p2 else 'annual'
        folder = 'company-facts-prospectus' if kind == 'prospectus' else 'company-facts'
        doc = json.loads((SITE / 'data' / folder / f'{tk}.json').read_text(encoding='utf-8'))
        pages = {f['id']: f for f in doc['facts']}
        cited = set()
        for k in ('hook', 'what', 'mix', 'regions'):
            if sb.get(k):
                cited.update(sb[k].get('facts') or [])
        for c in sb.get('cards') or []:
            cited.update(c.get('facts') or [])
        src = base['source']
        sources = {i: {'page': pages[i].get('page'), 'period': pages[i].get('period'), 'statement': pages[i]['statement']}
                   for i in cited if i in pages}
        if is_p2:
            code = directory[tk].get('industry_code') or ''
            name = code_names.get(code) or isin_only.get(tk) or (f'產業代碼 {code}（官方資料未載名稱）' if code else '未分類')
            code = code or by_name.get(name, 'unclassified')
            ind = {'slug': f'n-{code}', 'name_zh': f'{name}（新增公司）'}
        else:
            ind = names[r['industry_folder']]
        fx = None if is_p2 else fixes.get(tk)
        report = {'fy': src.get('fy'), 'filename': src.get('filename'), 'url': src.get('url'), 'kind': kind}
        if is_p2:
            report.update({'doc_label': src.get('doc_label'), 'filed_month': src.get('filed_month')})
        comps.append({
            'ticker': tk, 'name': r['company'], 'legal_name': base.get('legal_name') or '',
            'industry': {'slug': ind['slug'], 'name': ind['name_zh'].rstrip('?？')},
            'mops_industry': name if is_p2 else (basic.get(tk) or {}).get('industry_mops') or '',
            'corrected_from': names[fx['original_folder']]['name_zh'].rstrip('?？') if fx else None,
            'report': report,
            'hook': sb.get('hook'), 'what': sb.get('what'), 'mix': sb.get('mix'), 'regions': sb.get('regions'),
            'cards': sb.get('cards') or [], 'tags': sb.get('tags') or [],
            'fin': sb.get('fin') or {}, 'relations': sb.get('relations') or [], 'sources': sources,
            'youtube_id': yt.get(tk),
            'fin_missing': None if sb.get('fin') else ('format' if tk in (fin_p2 if is_p2 else fin_all) else 'absent'),
            # every verified fact (PASS, not rejected) for the 「年報重點全文」 section and the search index
            'facts': [{'id': f['id'], 'field': f['field'], 'statement': f['statement'], 'page': pages[f['id']].get('page')}
                      for f in base['facts'] if f['id'] in pages],
        })
        i = inds.setdefault(ind['slug'], {'slug': ind['slug'], 'name': ind['name_zh'].rstrip('?？'), 'tickers': []})
        i['tickers'].append(tk)
    # complete relation lists: the storyboard keeps at most 8 per company, so add every edge in which the company
    # is the counterparty of another company's report (role flipped), from the published listed_edges.csv
    names_by = {c['ticker']: c['name'] for c in comps}
    full = {c['ticker']: {(r['ticker'], r['side']): r for r in c['relations']} for c in comps}
    for e in csv.DictReader(open(SITE / 'data/relations/listed_edges.csv', encoding='utf-8-sig')):
        a, b, role = e['ticker'], e['counterparty_ticker'], e['role']
        if role not in ('customer', 'supplier') or a not in full or b not in full:
            continue
        share = e['share_text'] if re.search(r'\d', e['share_text'] or '') else ''
        kind = '銷貨' if role == 'customer' else '進貨'
        # a's report names b: for a, b is `role`; for b, a is the opposite role
        full[a].setdefault((b, role), {'name': names_by[b], 'ticker': b, 'side': role, 'share': share,
                                       'label': f'占{names_by[a]}{kind} {share}' if share else '', 'period': e['period']})
        opp = 'supplier' if role == 'customer' else 'customer'
        full[b].setdefault((a, opp), {'name': names_by[a], 'ticker': a, 'side': opp, 'share': share,
                                      'label': f'{names_by[b]}占{names_by[a]}{kind} {share}' if share else '', 'period': e['period']})
    for c in comps:
        c['relations'] = list(full[c['ticker']].values())
    (OUT / 'companies.json').write_text(json.dumps(comps, ensure_ascii=False), encoding='utf-8')
    (OUT / 'industries.json').write_text(json.dumps(sorted(inds.values(), key=lambda x: -len(x['tickers'])),
                                                   ensure_ascii=False), encoding='utf-8')
    # slim per-company summary for the client-side tools (compare, screener, watchlist, map): ~0.5 MB
    summ = []
    for c in comps:
        ys = sorted(c['fin'])
        last = c['fin'][ys[-1]] if ys else None
        yoy = (c['fin'][ys[-1]]['revenue_k'] / c['fin'][ys[0]]['revenue_k'] - 1) * 100 if len(ys) > 1 and c['fin'][ys[0]]['revenue_k'] else None
        top_c = max((float(r['share'].rstrip('%')) for r in c['relations'] if r['side'] == 'customer' and r['share'].rstrip('%').replace('.', '', 1).isdigit()), default=None)
        summ.append({'t': c['ticker'], 'n': c['name'], 'i': c['industry']['slug'], 'in': c['industry']['name'], 'm': c['mops_industry'],
                     'y': ys[-1] if ys else None, 'rev': round(last['revenue_k'] / 1e5, 2) if last else None,
                     'gm': last.get('gross_margin_pct') if last else None, 'yoy': round(yoy, 1) if yoy is not None else None,
                     'mix': (c['mix'] or {}).get('items', [])[:4], 'mixy': (c['mix'] or {}).get('year'), 'mixb': (c['mix'] or {}).get('basis'),
                     'reg': (c['regions'] or {}).get('items', [])[:4], 'regy': (c['regions'] or {}).get('year'), 'regb': (c['regions'] or {}).get('basis'),
                     'h': (c['hook'] or {}).get('text', ''), 'rel': [[r['ticker'], r['side'], r['label']] for r in c['relations']],
                     'moved': bool(c['corrected_from']), 'yt': c.get('youtube_id')})
    pub_data = ROOT / 'explore-demo/public/data'
    pub_data.mkdir(parents=True, exist_ok=True)
    # the full correction tables, downloadable from the 「抓到錯了？」 page
    (pub_data / 'errata').mkdir(exist_ok=True)
    for k in ('names', 'classification', 'claims'):
        shutil.copy2(SITE / f'errata/{k}.csv', pub_data / 'errata' / f'{k}.csv')
    (pub_data / 'summary.json').write_text(json.dumps(summ, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    (OUT / 'meta.json').write_text(json.dumps({'built': __import__('datetime').date.today().isoformat(),
        'companies': len(comps), 'p2_companies': sum(c['ticker'] in p2_tickers for c in comps),
        'industries': len(inds), 'facts': sum(len(c['facts']) for c in comps),
        'fy_counts': dict(__import__('collections').Counter(str(c['report']['fy']) for c in comps)),
        'fin_missing': dict(__import__('collections').Counter(c['fin_missing'] for c in comps if c['fin_missing'])),
        'errata': {k: sum(1 for _ in csv.DictReader(open(SITE / f'errata/{k}.csv', encoding='utf-8-sig'))) for k in ('names', 'classification', 'claims')},
        'claims_original': dict(__import__('collections').Counter(r['原句查核結果'] for r in csv.DictReader(open(SITE / 'errata/claims.csv', encoding='utf-8-sig')))),
        'claims_revised': dict(__import__('collections').Counter(r['更正句結果'] for r in csv.DictReader(open(SITE / 'errata/claims.csv', encoding='utf-8-sig'))))}, ensure_ascii=False), encoding='utf-8')
    print('companies', len(comps), 'industries', len(inds), 'summary bytes', (pub_data / 'summary.json').stat().st_size)


if __name__ == '__main__':
    main()
