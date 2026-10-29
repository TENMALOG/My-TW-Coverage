"""Read-only checks for P2 bases and the explore export, without writing storyboards.

  python -X utf8 -B explore-demo/scripts/check_p2.py [--baseline companies-before.json]

The export is captured in memory. P2 source citations use real, accepted facts in
memory instead of model-written storyboards; no generated or source file is written.
"""
import argparse
import contextlib
import importlib.util
import io
import json
import sys
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / 'research-site'
SHORTS = SITE / 'ops/shorts'
sys.path.insert(0, str(SITE / 'scripts/generic'))
import build_company_pages_p2 as p2


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def capture_export(exporter, storyboards):
    exists, read_text, glob = Path.exists, Path.read_text, Path.glob
    p2_tickers = {r['ticker'] for r in p2.p2_companies()}
    captured = {}

    def virtual_exists(path):
        if path.parent == SHORTS / 'storyboard' and path.stem in p2_tickers:
            return path in storyboards
        return path in storyboards or exists(path)

    def virtual_read(path, *args, **kwargs):
        return json.dumps(storyboards[path], ensure_ascii=False) if path in storyboards else read_text(path, *args, **kwargs)

    def capture_write(path, text, *args, **kwargs):
        captured[path] = text
        return len(text)

    def virtual_glob(path, pattern, *args, **kwargs):
        if path == SHORTS / 'out/master' and pattern == '*_poster.jpg':
            return iter(())
        return glob(path, pattern, *args, **kwargs)

    with patch.object(Path, 'exists', virtual_exists), patch.object(Path, 'read_text', virtual_read), \
            patch.object(Path, 'write_text', capture_write), patch.object(Path, 'mkdir'), patch.object(Path, 'glob', virtual_glob), \
            patch.object(exporter.shutil, 'copy2'), contextlib.redirect_stdout(io.StringIO()):
        exporter.main()
    return {path.name: json.loads(text) for path, text in captured.items()}


def main(baseline):
    rows = p2.p2_companies()
    accepted, rejected = p2.accepted_ids(), p2.base.semantic_rejects()
    directory = {r['ticker']: r for r in read_json(p2.DIRECTORY)['companies']}
    names, isin_only = p2.industry_names_official(directory)
    by_name = {v: k for k, v in names.items()}
    financials = p2.load_financials()
    bases, codes = {}, {}
    for r in rows:
        tk = r['ticker']
        path = SHORTS / 'base' / f'{tk}.json'
        if tk in p2.UNRESOLVED:
            assert not path.exists(), f'unresolved company has a base: {tk}'
            continue
        base = read_json(path)
        kind = base['source']['kind']
        folder = 'company-facts-prospectus' if kind == 'prospectus' else 'company-facts'
        doc = read_json(SITE / 'data' / folder / f'{tk}.json')
        assert not p2.base.identity_problems(doc, tk, r['company']), tk
        expected = [f for f in doc['facts'] if (f.get('verification') or {}).get('status') == 'PASS'
                    and f['id'] in accepted and f['id'] not in rejected]
        assert base['facts'] and [f['id'] for f in base['facts']] == [f['id'] for f in expected], tk
        assert base['name'] == r['company'] and base['legal_name'] == doc['legal_name'], tk
        assert base['relations'] == base['renames'] == [], tk
        code = directory[tk].get('industry_code') or ''
        industry = names.get(code) or isin_only.get(tk)
        assert industry and base['industry'] == industry, tk
        codes[tk] = code or by_name[industry]
        expected_fin = {y: {'revenue_k': v['items_k']['營業收入'], 'gross_margin_pct': v.get('gross_margin_pct')}
                        for y, v in financials.get(tk, {}).get('years', {}).items()
                        if (v.get('items_k') or {}).get('營業收入') is not None}
        assert base['fin'] == expected_fin, tk
        if kind == 'prospectus':
            assert base['source']['fy'] is None
            assert all(base['source'][k] == doc['source'][k] for k in ('doc_label', 'filed_month'))
        bases[tk] = base
    assert len(bases) == len(rows) - len(p2.UNRESOLVED) == 586
    assert sum(b['source']['kind'] == 'prospectus' for b in bases.values()) == 25
    print('P2 bases: 586 (561 annual, 25 prospectus); facts, identity, industries and financials PASS')

    spec = importlib.util.spec_from_file_location('export_data', Path(__file__).with_name('export_data.py'))
    exporter = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(exporter)
    current = capture_export(exporter, {})
    assert current['meta.json']['p2_companies'] == 0
    if baseline:
        before, after = read_json(baseline), current['companies.json']
        normalized = json.loads(json.dumps(after))
        for c in normalized:
            assert c['report'].pop('kind') == 'annual'
        assert before == normalized, 'catalog output differs beyond report.kind'
        print(f'companies.json regression: {len(before)} catalog companies; only report.kind=annual; normalized diff 0')

    # Use actual source text and ids solely to exercise export paths; never write P2 storyboards.
    storyboards = {SHORTS / 'storyboard' / f'{tk}.json': {
        'what': {'lines': [base['facts'][0]['statement']], 'facts': [base['facts'][0]['id']]},
        'fin': base['fin'], 'relations': [],
    } for tk, base in bases.items()}
    expanded = capture_export(exporter, storyboards)
    comps = {c['ticker']: c for c in expanded['companies.json']}
    inds = {i['slug']: i for i in expanded['industries.json']}
    assert expanded['meta.json']['p2_companies'] == 586
    assert len(comps) == len(current['companies.json']) + 586
    for tk, base in bases.items():
        c = comps[tk]
        assert c['industry'] == {'slug': f'n-{codes[tk]}', 'name': f'{base["industry"]}（新增公司）'}, tk
        assert tk in inds[c['industry']['slug']]['tickers'] and c['corrected_from'] is None, tk
        assert c['mops_industry'] == base['industry'], tk
        assert c['report']['kind'] == base['source']['kind'] and c['report']['fy'] == base['source']['fy'], tk
        assert c['fin_missing'] == (None if base['fin'] else 'format' if tk in financials else 'absent'), tk
        assert len(c['facts']) == len(base['facts']) and c['sources'][base['facts'][0]['id']]['page'], tk
        if c['report']['kind'] == 'prospectus':
            assert all(c['report'][k] == base['source'][k] for k in ('doc_label', 'filed_month'))
    assert expanded['meta.json']['industries'] == len(inds)
    print(f'In-memory P2 export: {len(comps)} companies; 586 P2; n-* industries, citations, source metadata and fin_missing PASS')

    spec = importlib.util.spec_from_file_location('og_cards', Path(__file__).with_name('og_cards.py'))
    og = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(og)
    read_text = Path.read_text

    def card_data(path, *args, **kwargs):
        if path == og.DATA / 'companies.json':
            return json.dumps(expanded['companies.json'], ensure_ascii=False)
        return read_text(path, *args, **kwargs)

    with patch.object(Path, 'read_text', card_data), patch.object(Path, 'mkdir'), \
            patch.object(og, 'sync_playwright') as playwright, contextlib.redirect_stdout(io.StringIO()):
        page = playwright.return_value.__enter__.return_value.chromium.launch.return_value.new_page.return_value
        og.main(set(bases))
        cards = [call.args[1] for call in page.evaluate.call_args_list if len(call.args) == 2]
    assert len(cards) == 586
    for card in cards:
        prospectus = bases[card['tk']]['source']['kind'] == 'prospectus'
        assert ('公開說明書' in card['foot']) == prospectus
        if prospectus:
            assert '年報' not in card['foot']
    print('OG card source labels: 586 cards checked in memory; 25 prospectus labels PASS')
    return expanded


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--baseline', type=Path)
    main(ap.parse_args().baseline)
