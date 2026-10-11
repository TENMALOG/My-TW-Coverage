"""Assemble the aerospace & defense verified-fact table (only publishable content).

Sources of admissible content:
  A. revision-pilot-001 REVISED_SUPPORTED (frozen delivery)
  B. revision-aero-001 / -002 REVISED_SUPPORTED (Codex vote + Claude primary source review PASS)
  C. company-research-aero-001 facts independently verified by Claude against the
     captured primary source (excerpt re-located in the captured text; listed below).
Each row records the evidence capture hash so the citation is reproducible.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CR = ROOT / 'audit-v5/semantic/candidate-rerun'
CACHE = ROOT / 'audit-v5/source-cache/candidate-rerun'
OUT = ROOT / 'research-site/data/aerospace-defense/verified-facts.jsonl'
REVIEWER = 'claude-opus-5-5（依董事長2026-10-11決定視為獨立審查）'

AIRASIA_AR = 'https://www.airasia.com.tw/userfiles/03.Investor_Relations/%E4%BA%9E%E8%88%AA114%E5%B9%B4%E5%A0%B1.pdf'
LUNGTEH_AR = ('https://cdn.financialreports.eu/financialreports/media/filings/52620/2026/RNS/'
              '52620_rns_2026-05-22_bae39150-3837-4562-9cad-4b97c2d')  # prefix; resolved below
LUNGTEH_WEB = 'https://www.lungteh.com/zh/about-us'
NAVY_TJ = 'https://navy.mnd.gov.tw/AboutUs/Other_Info.aspx?AID=30034&ID=1'
TAC = 'https://www.tacaviation.com.tw/service/15'
PCC_UH60 = 'https://pcc.mlwmlw.org/merchants/11381701'

AIRASIA_AR_SRC = dict(title='亞洲航空股份有限公司114年度年報', source_kind='公司年報（公司官網）', publication_date='2026-04-20')
LUNGTEH_AR_SRC = dict(title='龍德造船工業股份有限公司114年度年報', source_kind='公司年報（公開資訊觀測站）',
                      publication_date='2026-05-05')
AIRASIA_AR_SRC = dict(AIRASIA_AR_SRC, source_kind='公司年報（公開資訊觀測站）')

# (fact_id, ticker, company, topic, text, period, url, src-meta, locator, excerpt)
COMPANY_FACTS = [
    ('2630-F01', '2630', '亞航', '沿革', '依亞洲航空官網公司簡介，亞航成立於1955年，由陳納德將軍設立；1994年起成為台翔航太工業股份有限公司的子公司。',
     '1955年至今（官網）', 'https://www.airasia.com.tw/index.php?id=1&index=1&lang=cht&option=module&task=pa',
     dict(title='亞洲航空 公司簡介', source_kind='公司官網', publication_date=None), '公司簡介首段', '自1994年亞航正式成為台翔航太工業股份有限公司的子公司'),
    ('2630-F02', '2630', '亞航', '集團與轉投資', '依亞航114年度年報，台翔航太工業股份有限公司持有亞航49.67%股份，為最大股東。',
     '2026-04-19 股東名簿', AIRASIA_AR, AIRASIA_AR_SRC, 'PDF第80頁，前十大股東表', '台翔航太工業股份有限公司 104,029,402 49.67%'),
    ('2630-F03', '2630', '亞航', '營收結構', '依亞航114年度年報，2025年營業收入5,454,110千元，其中零附件維修類（自修）占42.62%、飛機維修占25.68%、委外送修及航材買賣占21.67%、機隊維持及修護補給裝機計價占10.03%。',
     '2025年度', AIRASIA_AR, AIRASIA_AR_SRC, 'PDF第85頁，營業比重表', '零附件維修類(自修) 2,324,640 42.62'),
    ('2630-F04', '2630', '亞航', '客戶', '依亞航114年度年報，2025年度占銷貨淨額10%以上的客戶為匿名「A客戶」（52.28%）及「B客戶」（15.50%），年報未揭露名稱。',
     '2025年度', AIRASIA_AR, AIRASIA_AR_SRC, 'PDF第98頁，主要銷貨客戶資料', 'A 客戶 2,851,630 52.28'),
    ('2630-F05', '2630', '亞航', '客戶', '依亞航114年度年報，公司執行「空軍第二後勤指揮部軍工廠委託民間經營案」（合約期限2023至2027年，續約）及「空軍松山基地指揮部修護補給隊委託民間經營案」。',
     '2025年度營運；合約期間依年報', AIRASIA_AR, AIRASIA_AR_SRC, 'PDF第6頁致股東報告書、第86頁', '空軍第二後勤指揮部軍工廠委託民間經營'),
    ('2630-F06', '2630', '亞航', '重大合約', '依亞航114年度年報，內政部空中勤務總隊115至116年UH-60M黑鷹直昇機隊委商管理及維修案由亞航取得，合約期限2026年1月1日至2027年12月31日，合約金額新臺幣4.15億元。',
     '2026–2027', AIRASIA_AR, AIRASIA_AR_SRC, 'PDF第87頁，國內市場(d)', '115-116 年續約亦由本公司獲得'),
    ('2630-F07', '2630', '亞航', '供應商', '依亞航114年度年報，亞航為美國貝爾直昇機及Breeze-Eastern公司授權維修中心，並與Sikorsky直昇機公司簽定技術支援協議。',
     '2025年度年報', AIRASIA_AR, AIRASIA_AR_SRC, 'PDF第7頁，直昇機維修業務', '並與 Sikorsky 直昇機公司簽定技術支援協議'),
    ('2630-F08', '2630', '亞航', '客戶', '依亞航114年度年報，陸軍OH-58D、CH-47SD、TH-67等型直昇機策略性商維案由亞航執行機體、發動機及附件維修。',
     '2025年度年報', AIRASIA_AR, AIRASIA_AR_SRC, 'PDF第7頁，直昇機維修業務', '依與陸軍簽訂 OH-58D、CH-47SD、TH-67 等型直昇機'),
    ('2630-F09', '2630', '亞航', '業務與產品', '依亞航114年度年報，商用飛機維修以波音B737、空巴A320系列、DHC-8-Q400及ATR 42/72等窄體／支線飛機為主要服務對象，2025年共有17家客戶、54架次進廠。',
     '2025年度', AIRASIA_AR, AIRASIA_AR_SRC, 'PDF第5頁及第87至88頁', '114 年本公司共獲 17 家客戶、54 架次進廠'),
    ('2630-F10', '2630', '亞航', '客戶', '依亞航114年度年報，商用維修客戶包括日本Peach Aviation、Jetstar Japan，韓國t’way、Jeju air，越南Vietjet Air等航空公司。',
     '2025年度年報所列', AIRASIA_AR, AIRASIA_AR_SRC, 'PDF第87至88頁，國外市場', '日本：Peach Aviation、Jetstar Japan'),
    ('2630-F11', '2630', '亞航', '重大合約', '依亞航114年度年報，公司於2023年底取得「銳鳶二型生產製造及組裝案」，2024年8月完成第一架交機；年報對全案完成時間分別記載為2025年8月及2025年9月驗結。',
     '2023–2025', AIRASIA_AR, AIRASIA_AR_SRC, 'PDF第6頁及第87頁', '已於113 年 8 月完成第一架交機'),
    ('2630-F12', '2630', '亞航', '業務與產品', '依台翔航太2024年8月28日公告，銳鳶二型承製案由亞航負責專案管理、非破壞性檢測及協助組裝，碳基科技負責碳纖複材機體製造及全機組裝。',
     '2024-08-28', 'https://en.tacaviation.com.tw/news_detail/65', dict(title='台翔航太新聞', source_kind='母公司官網公告', publication_date='2024-08-28'),
     '正文第40至41行', '由亞航公司負責全案專案管理及非破壞性檢測、協助組裝等工項'),
    ('6753-F01', '6753', '龍德造船', '業務與產品', '依龍德造船114年度年報，公司以生產中、高速船艇為主要業務，產品用途包括離岸及近岸巡邏艇、消防及救援船、人員運維船、研究及測量船與無人船，並提供維修服務。',
     '2025年度年報', None, LUNGTEH_AR_SRC, 'PDF第70至71頁，商品服務項目', '本公司以生產中、高速船艇為主要業務'),
    ('6753-F02', '6753', '龍德造船', '營收結構', '依龍德造船114年度年報，2025年營業收入5,246,333千元，其中船舶建造占88.56%、船舶保養占6.37%、其他占5.07%。',
     '2025年度', None, LUNGTEH_AR_SRC, 'PDF第70頁，營業比重表', '船舶建造4,224,151 82.52% 4,646,161 88.56%'),
    ('6753-F03', '6753', '龍德造船', '營收結構', '依龍德造船114年度年報，2025年內銷占營業收入86.59%，外銷東南亞占12.13%、東亞占1.28%。',
     '2025年度', None, LUNGTEH_AR_SRC, 'PDF第78頁，銷售地區表', '東南亞450,011 8.79% 636,211 12.13%'),
    ('6753-F04', '6753', '龍德造船', '客戶', '依龍德造船114年度年報，2025年度占銷貨淨額10%以上的客戶以代號「C客戶」（80.03%）及「B客戶」（12.13%）列示，年報未揭露名稱。',
     '2025年度', None, LUNGTEH_AR_SRC, 'PDF第85頁，主要銷貨客戶表', 'C客戶 4,198,858 80.03'),
    ('6753-F05', '6753', '龍德造船', '供應商', '依龍德造船114年度年報，主要原料供應表列中鋼鋁業為鋁合金板供應廠商、Rolls-Royce為引擎主機供應廠商之一；2025年度最大進貨供應商以「甲公司」代稱，占進貨淨額46.66%。',
     '2025年度年報', None, LUNGTEH_AR_SRC, 'PDF第84頁，主要原料供應狀況及主要進貨供應商表', '鋁合金板 中鋼鋁業 良好、穩定'),
    ('6753-F06', '6753', '龍德造船', '重大合約', '依龍德造船114年度年報重要契約表，公司與國防部自2025年4月25日起有布雷艇後續艇6艘建造契約，與新加坡警察海岸衛隊自2025年5月8日起有攔截艇6艘建造契約，與關務署基隆關自2025年6月14日起有巡緝艇2艘建造契約，均依約分批交船。',
     '2025年起；至2026-05-05年報刊印', None, LUNGTEH_AR_SRC, 'PDF第92至93頁，重要契約表', '國防部 114/4/25 - 依約分批交船 布雷艇後續艇6艘'),
    ('6753-F07', '6753', '龍德造船', '重大合約', '依龍德造船114年度年報致股東報告書，公司持續執行海軍高效能艦艇後續艦第二批5艘量產案，並已於2025年完成中科院「快奇專案」有人／無人工作船研發案交船。',
     '2025年度及2026年', None, LUNGTEH_AR_SRC, 'PDF第4頁，致股東報告書', '持續執行海軍高效能艦艇後續艦第二批5艘量產案'),
    ('6753-F08', '6753', '龍德造船', '沿革', '依海軍司令部網站，沱江級飛彈巡邏艦由龍德造船建造，2012年11月21日開工，2014年3月14日下水命名為沱江軍艦。',
     '2012–2014', NAVY_TJ, dict(title='沱江級飛彈巡邏艦', source_kind='海軍司令部官網', publication_date=None), '軍艦介紹', '沱江級飛彈巡邏艦為我國龍德造船場建造'),
    ('6753-F09', '6753', '龍德造船', '沿革', '依龍德造船官網沿革，公司創立於1976年；2007年起交付香港海事處鋁合金警艇17艘，2009年起交付香港海關巡防艇3艘，2013年10月得標新加坡警察海岸衛隊巡邏艇案。',
     '1976–2013', LUNGTEH_WEB, dict(title='龍德造船 公司沿革', source_kind='公司官網', publication_date=None), '公司沿革', '102年10月得標新加坡警察海岸保衛處巡邏艇標案'),
    # FY2025 MOPS annual-report facts read by Claude (url 'MOPS:<ticker>')
    ('2208-F01', '2208', '台船', '營收結構', '依台船114年度年報，2025年營業收入217.8億元，其中艦艇建造占66.53%、機械製造占15.89%、商船建造占9.15%、船艦維修占5.68%。',
     '2025年度', 'MOPS:2208', dict(title='台灣國際造船股份有限公司114年度年報', source_kind='公司年報（公開資訊觀測站）', publication_date=None),
     'PDF第84頁，營業比重表', '艦艇建造 8,878,572 61.26% 1 4,491,744 66.53%'),
    ('2208-F02', '2208', '台船', '客戶', '依台船114年度年報，2025年度占銷貨淨額10%以上的客戶為國防部海軍造船發展中心（54.77%）、台灣中油股份有限公司（15.32%）及行政院海巡署（10.57%）。',
     '2025年度', 'MOPS:2208', dict(title='台灣國際造船股份有限公司114年度年報', source_kind='公司年報（公開資訊觀測站）', publication_date=None),
     'PDF第109頁，主要銷貨客戶資料', '11,928,237 54.77'),
    ('2634-F01', '2634', '漢翔', '營收結構', '依漢翔114年度年報，2025年營業收入354.5億元，其中飛機及航空器維修類（含軍用、民用）占50.45%、引擎類占46.90%、工業技術服務類占2.65%。',
     '2025年度', 'MOPS:2634', dict(title='漢翔航空工業股份有限公司114年度年報', source_kind='公司年報（公開資訊觀測站）', publication_date=None),
     'PDF第76頁，營業比重', '17,886,733 50.45'),
    ('2644-F01', '2644', '中信造船', '業務與產品', '依中信造船114年度年報，公司目前主要產品為海巡艦艇、海軍輕型巡防艦及超重力型拖船；2025年船舶建造占營業收入93.69%，內銷占99.01%。',
     '2025年度', 'MOPS:2644', dict(title='中信造船股份有限公司114年度年報', source_kind='公司年報（公開資訊觀測站）', publication_date=None),
     'PDF第40頁及第44頁', '主要產品（建造工案）為海巡艦艇、海軍輕型巡防艦及超重力型拖船'),
    ('2644-F02', '2644', '中信造船', '其他', '中信造船114年度年報自述，在國內海巡艦艇建造數量上具70%以上市占率；此為公司自述。',
     '2025年度年報', 'MOPS:2644', dict(title='中信造船股份有限公司114年度年報', source_kind='公司年報（公開資訊觀測站）', publication_date=None),
     'PDF第44頁，市場占有率', '本公司 70%以上市占率'),
    ('2645-F01', '2645', '長榮航太', '其他', '長榮航太114年度年報自述，2025年維修波音747大型機體總數約占整個MRO 747機體市場的37%；此為公司估算。',
     '2025年度', 'MOPS:2645', dict(title='長榮航太科技股份有限公司114年度年報', source_kind='公司年報（公開資訊觀測站）', publication_date=None),
     'PDF第45頁，市場占有率', '約占整個MRO 747機體市場的37%'),
    ('2645-F02', '2645', '長榮航太', '客戶', '依長榮航太114年度年報，母公司長榮航空占2025年度銷貨淨額33.30%；2025年航空器維修及其他占營業額77.78%、零組件製造銷售占22.22%，外銷占55.96%。',
     '2025年度', 'MOPS:2645', dict(title='長榮航太科技股份有限公司114年度年報', source_kind='公司年報（公開資訊觀測站）', publication_date=None),
     'PDF第41、45、47頁', '6,053,724 2,582,003 9,543,458 18,179,185 33.30'),
    ('4541-F01', '4541', '晟田', '營收結構', '依晟田114年度年報，2025年航太零組件（客供料48.60%、自購料19.69%）合計約占營收68%，半導體設備零組件占25.36%；航太產品包括發動機機匣、渦輪懸塊及導片、起落架及飛行控制致動器零組件。',
     '2025年度', 'MOPS:4541', dict(title='晟田科技工業股份有限公司114年度年報', source_kind='公司年報（公開資訊觀測站）', publication_date=None),
     'PDF第45頁，營業比重及商品項目', '半導體設備零組件 212,709 15.02 416,835 25.36'),
    ('4546-F01', '4546', '長亨', '營收結構', '依長亨114年度年報，2025年營業收入20.1億元，其中飛機發動機高端零件占52%、組合件模組占44%；外銷美國占48.70%、法國占16.37%；最大客戶以代號「C公司」列示（48.86%）。',
     '2025年度', 'MOPS:4546', dict(title='長亨精密股份有限公司114年度年報', source_kind='公司年報（公開資訊觀測站）', publication_date=None),
     'PDF第43、54、66頁', '飛機發動機高端零件 1,038,354 52'),
    ('4572-F01', '4572', '駐龍', '營收結構', '依駐龍114年度年報，2025年飛機結構零組件占營收94.07%；營收較前一年減少，年報說明主係國內部分專案已於2024年底完成交貨。',
     '2025年度', 'MOPS:4572', dict(title='駐龍精密機械股份有限公司114年度年報', source_kind='公司年報（公開資訊觀測站）', publication_date=None),
     'PDF第59、70頁', '主係國內部分專案已於 113底完成交貨所致'),
]


def norm(s):
    return re.sub(r'\s+', '', unicodedata.normalize('NFKC', s))


MOPS = ROOT / 'audit-v5/source-cache/research-site/mops-annual'


def mops(ticker):
    m = json.loads((MOPS / f'{ticker}_2025_F04.json').read_text(encoding='utf-8'))
    return {'url': m['citation_url'], 'text_path': m['text_path'], 'text_sha256': m['text_sha256'], 'captured_at': m['captured_at']}


def find_capture(url_prefix):
    for meta in (CACHE / 'company-research-aero-001/sources').glob('*.json'):
        m = json.loads(meta.read_text(encoding='utf-8'))
        if m['url'].startswith(url_prefix) and m.get('status') == 'captured':
            return m
    raise SystemExit(f'no capture for {url_prefix}')


def main():
    rows = []
    # A + B: revision-based facts
    for path, batch in ((CR / 'revision-pilot-001/delivery/accepted-revisions.jsonl', 'revision-pilot-001'),):
        for line in path.read_text(encoding='utf-8').splitlines():
            r = json.loads(line)
            if r['ticker'] in ('2208', '2634'):
                rows.append({'fact_id': r['revision_id'], 'ticker': r['ticker'], 'company': r['company'], 'topic': '業務與歷史資料',
                             'text': r['text'], 'basis': f'{batch} REVISED_SUPPORTED', 'period': r['adjudication'].get('period_assessment', ''),
                             'citations': [{'url': e['url'], 'title': e['title'], 'locator': e['locator'], 'publication_date': e['publication_date']}
                                           for a in r['adjudication']['atomic_claims'] for e in a['evidence']]})
    for batch in ('revision-aero-001', 'revision-aero-002'):
        out = CR / batch / 'delivery/outcomes.jsonl'
        if not out.exists():
            continue
        res = {}
        for line in (CR / batch / 'adjudication/results.jsonl').read_text(encoding='utf-8').splitlines():
            r = json.loads(line); res[r['claim_id']] = r
        for line in out.read_text(encoding='utf-8').splitlines():
            o = json.loads(line)
            if o['verdict'] != 'REVISED_SUPPORTED':
                continue
            adj = res[o['claim_id']]['output']
            rows.append({'fact_id': o['claim_id'], 'ticker': o['ticker'], 'company': o['company'], 'topic': '業務與歷史資料',
                         'text': o['proposed_text'], 'basis': f'{batch} REVISED_SUPPORTED', 'period': adj['period_assessment'],
                         'citations': [{'url': e['url'], 'title': e['title'], 'locator': e['locator'], 'publication_date': e['publication_date']}
                                       for a in adj['atomic_claims'] if a['status'] == 'SUPPORTED' for e in a['evidence']]})
    # C: company facts, excerpt must be re-located in the captured text
    lungteh_ar = mops('6753')
    failures = []
    for fid, ticker, company, topic, text, period, url, src, locator, excerpt in COMPANY_FACTS:
        cap = lungteh_ar if url is None else (mops('2630') if url == AIRASIA_AR else (mops(url[5:]) if url.startswith('MOPS:') else find_capture(url)))
        body = (ROOT / cap['text_path']).read_text(encoding='utf-8', errors='replace')
        if norm(excerpt) not in norm(body):
            failures.append((fid, excerpt))
        rows.append({'fact_id': fid, 'ticker': ticker, 'company': company, 'topic': topic, 'text': text,
                     'basis': 'company-research-aero-001，Claude 以擷取原文獨立核對', 'period': period,
                     'citations': [{'url': cap['url'], **src, 'locator': locator, 'support_excerpt': excerpt,
                                    'capture_text_sha256': cap['text_sha256'], 'captured_at': cap['captured_at']}],
                     'reviewer': REVIEWER})
    if failures:
        for f in failures:
            print('EXCERPT NOT FOUND', f)
        sys.exit(1)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
    print(f'{len(rows)} verified facts -> {OUT.relative_to(ROOT).as_posix()}')


if __name__ == '__main__':
    main()
