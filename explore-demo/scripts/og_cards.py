"""Share cards (Open Graph 1200x630 JPEG) for every company and industry page → public/og/{ticker}.jpg, public/og/i-{slug}.jpg

  py explore-demo/scripts/og_cards.py [tickers...]

Text comes from src/data (company name, verified hook sentence, industry); no new claims. Rixingsong only.
"""
import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / 'src' / 'data'
OUT = HERE.parent / 'public' / 'og'


def main(only):
    OUT.mkdir(parents=True, exist_ok=True)
    comps = json.loads((DATA / 'companies.json').read_text(encoding='utf-8'))
    inds = json.loads((DATA / 'industries.json').read_text(encoding='utf-8'))
    jobs = []
    for c in comps:
        if only and c['ticker'] not in only:
            continue
        fy = (c.get('report') or {}).get('fy') or ''
        jobs.append((OUT / f"{c['ticker']}.jpg", {
            'kicker': '公司速覽', 'right': c['industry']['name'], 'tk': c['ticker'], 'name': c['name'],
            'hook': (c.get('hook') or {}).get('text', ''), 'foot': f'資料：{fy} 年度年報｜每一句都附年報頁碼'}))
    if not only:
        for i in inds:
            jobs.append((OUT / f"i-{i['slug']}.jpg", {
                'kicker': '產業速覽', 'right': f"{len(i['tickers'])} 家上市櫃公司", 'tk': '', 'name': i['name'],
                'hook': '', 'foot': '每一家都附年報出處'}))
    with sync_playwright() as p:
        b = p.chromium.launch(channel='chrome')
        pg = b.new_page(viewport={'width': 1200, 'height': 630})
        pg.goto((HERE / 'og.html').as_uri())
        pg.evaluate('window.ready')
        for path, d in jobs:
            pg.evaluate('d => fill(d)', d)
            pg.screenshot(path=str(path), type='jpeg', quality=86)
        b.close()
    print('cards', len(jobs))


if __name__ == '__main__':
    main(set(sys.argv[1:]))
