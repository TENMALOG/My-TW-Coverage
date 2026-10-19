"""YouTube title / description / hashtags for each company video, built only from verified data.

  py youtube_meta.py 2330 [2330 ...]      -> out/meta/{ticker}.txt (paste-ready) and .json

Every number comes from the same storyboard the video draws (validated against annual-report facts) or the
MOPS income-statement summary; every bullet names its source (annual-report page or MOPS). Published on the
creator channel 尼奧天馬 @tenmalog as the 股.tw 研究室 series. Title ≤ 100 characters (YouTube limit).
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from record_web import storyboard  # noqa: E402  (corrected industry, 證交所產業別, fact pages)

OUT = HERE / 'out' / 'meta'


def tag(s):
    """YouTube hashtags: no spaces or punctuation."""
    return '#' + re.sub(r'[\s\.\-、，,（）()／/·・&]+', '', s)


def pages(sb, ids):
    ps = sorted({sb['pages'].get(i) for i in ids or [] if sb['pages'].get(i)})
    return f"年報第 {'、'.join(map(str, ps))} 頁" if ps else '年報'


def basis(obj):
    return (obj.get('basis') or '').replace('（', '，').replace('）', '')   # 避免括號裡再有括號


def items(obj, n=4):
    return '、'.join(f'{a} {b}%' for a, b in obj['items'][:n])


def meta(t):
    sb = storyboard(t)
    name, fy = sb['name'], (sb.get('source') or {}).get('fy')
    hook = (sb.get('hook') or {}).get('text') or ''
    rest = hook[len(name):] if hook.startswith(name) else None
    short = rest.lstrip('：:，, 的') if rest is not None else hook          # 標題不重複公司名（「中鋼的煤…」→「煤…」）
    first = f'{name}（{t}）{rest.lstrip()}' if rest is not None else f'{name}（{t}）：{hook}'   # 說明欄首句保留完整語句
    head = f'{name} {t}'
    title = f'{head}｜{short}' if hook else f'{head}｜年報重點速覽'
    if len(title) > 100:
        title = title[:99] + '…'

    lines = [f'{first}。' if hook else f'{name}（{t}）年報重點速覽。', '']
    pts = []
    fin = sb.get('fin') or {}
    ys = sorted(fin)
    if ys:
        last = ys[-1]
        rev = fin[last]['revenue_k'] / 1e5
        s = f'{last} 營收 {round(rev):,} 億元' if rev >= 100 else f'{last} 營收 {rev:.1f} 億元'
        if len(ys) > 1:
            g = (fin[last]['revenue_k'] / fin[ys[0]]['revenue_k'] - 1) * 100
            s += f'，年增 {g:+.1f}%'
        if fin[last].get('gross_margin_pct') is not None:
            s += f'，毛利率 {fin[last]["gross_margin_pct"]}%'
        pts.append(s + '（公開資訊觀測站 綜合損益表彙總；年增率由本站計算）')
    if sb.get('mix'):
        m = sb['mix']
        pts.append(f"營收結構（{m['year']} 年度，{basis(m)}）：{items(m)}（{pages(sb, m.get('facts'))}）")
    if sb.get('regions'):
        r = sb['regions']
        pts.append(f"銷售地區（{r['year']} 年度，{basis(r)}）：{items(r, 3)}（{pages(sb, r.get('facts'))}）")
    for c in (sb.get('cards') or [])[:2]:
        pts.append(f"{c['text']}（{'公司自述，' if c.get('self') else ''}{pages(sb, c.get('facts'))}）")
    if pts:
        lines += ['這支影片的重點'] + [f'・{p}' for p in pts] + ['']
    src = sb.get('source') or {}
    lines += ['資料來源',
              f"・{sb.get('legal_name') or name} {fy} 年度年報：{src.get('url', '')}",
              '・財務數字：公開資訊觀測站 綜合損益表彙總', '',
              '股.tw 研究室｜1,733 家台股公司，每一句都附年報頁碼。',
              '製作：尼奧天馬 @tenmalog',
              '※ 內容整理自公開資訊，僅供研究參考，不構成投資建議。', '']
    tags = ['#股tw研究室', tag(name)]
    if sb.get('industry_zh'):
        tags.append(tag(sb['industry_zh']))
    tags += ['#台股', '#年報']
    lines.append(' '.join(dict.fromkeys(tags)))
    desc = '\n'.join(lines)
    return {'ticker': t, 'title': title, 'description': desc, 'hashtags': list(dict.fromkeys(tags))}


def main(ts):
    OUT.mkdir(parents=True, exist_ok=True)
    for t in ts:
        m = meta(t)
        (OUT / f'{t}.json').write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding='utf-8')
        (OUT / f'{t}.txt').write_text(f"【標題】\n{m['title']}\n\n【說明】\n{m['description']}\n", encoding='utf-8')
        print(t, len(m['title']), 'chars')


if __name__ == '__main__':
    main(sys.argv[1:])
